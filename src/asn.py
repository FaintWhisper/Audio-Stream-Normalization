import args_parser
import platform
import sounddevice as sd
import numpy as np
from pydub import AudioSegment


class AudioStreamNormalization:
    def __init__(self):
        self.parser, self.args = args_parser.parse()
        self.data = np.empty(shape=(0, self.args.channels), dtype=self.args.audio_data_type)
        self.buffer_max_samples = self.args.sample_rate / self.args.buffer_size
        self.buffer_num_samples = 0

    def normalize(self, audio_segment, target_dBFS):
        profiles = {
            "soft": 0.08,
            "medium": 0.06,
            "hard": 0.04
        }

        if (audio_segment.dBFS >= self.args.normalization_threshold):
            change_in_dBFS = ((1 / (1 + np.exp(-target_dBFS + audio_segment.dBFS))) - 0.5) / (profiles[self.args.normalization_profile] * np.log(abs(audio_segment.dBFS)))
            #audio_segment = audio_segment.apply_gain(change_in_dBFS)

            if (self.args.debug == True):
                print(f"Normalization threshold exceeded:\nAudio segment (dbFS): {audio_segment.dBFS} # Applied Gain (dBFS): {change_in_dBFS}\n")

        if (audio_segment.dBFS > self.args.limiter_threshold):
            change_in_dBFS = (target_dBFS - audio_segment.dBFS)
            #audio_segment = audio_segment.apply_gain(change_in_dBFS)

            if (self.args.debug == True):
                print(f"Limiter threshold exceeded:\nAudio segment (dbFS): {audio_segment.dBFS} # Applied Gain (dBFS): {change_in_dBFS}\n")

        return audio_segment

    def stream_callback(self, indata, outdata, frames, time, status):
        if (status):
            print(status)
        
        self.data = np.vstack((self.data, indata))

        if ((self.data.shape[0] > 0) and (self.data.shape[0] % self.buffer_max_samples == 0)):
            stacked_channels_data = np.vstack([np.array(channel_data, dtype=self.args.audio_data_type)
                                              for channel_data in np.hsplit(self.data, self.args.channels)]).flatten()
            audio_segment = AudioSegment(
                stacked_channels_data.tobytes(),
                frame_rate=self.args.sample_rate,
                sample_width=self.data.dtype.itemsize,
                channels=self.args.channels
            )
            normalized_audio_segment = self.normalize(audio_segment, self.args.normalization_target)
            normalized_audio_data = np.array(normalized_audio_segment.get_array_of_samples())
            self.data = np.column_stack([np.array(normalized_audio_channel_data, dtype=self.args.audio_data_type)
                                        for normalized_audio_channel_data in np.array_split(normalized_audio_data, self.args.channels)])

            self.buffer_num_samples = self.buffer_max_samples

        if (self.buffer_num_samples > 0):
            outdata[:] = self.data[0:self.args.block_size]
            self.data = self.data[self.args.block_size:]
            self.buffer_num_samples -= self.args.block_size

    def start(self):
        if (platform != "Darwin"):
            print("Press Ctrl-C to stop.\n")
        else:
            print("Press Command-C to stop.\n")
          
        try:
            with sd.Stream(device=(self.args.input_device, self.args.output_device),
                           samplerate=self.args.sample_rate, blocksize=self.args.block_size,
                           dtype=self.args.audio_data_type, latency=self.args.latency,
                           channels=self.args.channels, callback=self.stream_callback):
                input()
        except KeyboardInterrupt:
            self.parser.exit('')
        except Exception as e:
            self.parser.exit(type(e).__name__ + ': ' + str(e))
