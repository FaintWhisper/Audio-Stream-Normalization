import argparse
import sounddevice as sd


def int_or_str(input):
    try:
        return int(input)
    except ValueError:
        return input


def parse():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-l', '--list-devices', action='store_true', help='Show a list of available audio devices')
    args, remaining = parser.parse_known_args()

    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])

    parser.add_argument('-i', '--input-device', type=int_or_str, help='Input device (numeric ID or substring)')
    parser.add_argument('-o', '--output-device', type=int_or_str, help='Output device (numeric ID or substring)')
    parser.add_argument('-c', '--channels', type=int, default=2, help='Number of channels')
    parser.add_argument('--audio_data_type', default="int32", help='Audio data type')
    parser.add_argument('--sample_rate', type=float, default=44100, help='Sampling rate')
    parser.add_argument('--block_size', type=int, default=882, help='Block size')
    parser.add_argument('--latency', type=float, default=1, help='Latency (in seconds)')
    parser.add_argument('--buffer_size', type=float, help='Buffer size (in seconds)')
    parser.add_argument('--normalization_target', type=float, default=-32, help='Target dbFS')
    parser.add_argument('--normalization_threshold', type=int, default=-35, help='Normalization threshold (in dBFS)')
    parser.add_argument('--normalization_profile', type=str.lower,
                        choices=["soft", "medium", "hard"], default="medium", help='Normalization intensity ("soft", "medium" or "hard")')
    parser.add_argument('--limiter_threshold', type=int, default=-20, help='Limiter threshold (in dBFS)')
    parser.add_argument('--debug', type=bool, default=False, help='Enable or disable debug mode')

    args = parser.parse_args(remaining)

    return parser, args
