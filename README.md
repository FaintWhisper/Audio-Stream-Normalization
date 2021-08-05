<p align="center">
  <h3 align="center">Audio Stream Normalization (ASN)</h3>

  <p align="center">
    Real-time audio output normalization for Windows, macOS and Linux.
    <br/>
    <a href="https://github.com/RYSKZ/Audio-Stream-Normalization/issues">Report a Bug</a>
    ·
    <a href="https://github.com/RYSKZ/Audio-Stream-Normalization/issues">Request a Feature</a>
  </p>
</p>


<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project started from the idea of developing a dynamic compressor that reduces abrupt acoustic differences in the amplitude of an audio signal in real time alongside a limiter that tottaly prevents loud noises which can lead to soft or hard clipping situations that may damage your hearing or your audio output device

The combination of these two features can be especially useful for those people that suffer of some mental or hearind disorder, such as hyperacusis or phonophobia. By reducing the exposure to harmful noise, people affected by such condititons may feel more safe and calm while using their computer, greatly reducing the anxiety and anguish that these situations can generate.

I built this project for my personal use, however, I thought I could share it publicly so, hopefully, more people can benefit from this.

<!-- GETTING STARTED -->
## Getting Started

In this section you can find all the steps required to install and run this software in your computer.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python version 3.x (https://www.python.org/downloads/).
* A virtual audio device, personally, I recommend Virtual Audio Cable (VAC) from VB-Audio Software (https://vb-audio.com/Cable/), there is a free version available which is more than enough to make use of this project. As a side note, if you choosed to install VAC, I suggest you to open VAC Control Panel and check the "Volume Control" box that appears at the upper right section, this will allow you to manually control the volume of the audio that goes through the virtual device whenever you require.

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
   
2. Install the dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```
3. Select the virtual audio device you installed earlier as the default output device.
  
4. Check your input and output device IDs:
   ```sh
   python main.py -l
   ```
   Write down the numbers that appear at the left of your desired input and output devices names.
   
5. Open start.bat, if you are on Windows, or start.sh, if you are on Linux or MacOS, with a text editor and replace the IDs you wrote down in the last step for the ones present in the file, especifically replace the number after "-i" for the ID of your input device and the number after "-o" with your output device ID.
As you may notice there are more parameters you can set, you can check what they do in the help message:
   ```sh
   python main.py -h
   ```
   
5. Done! Keep in mind that it will take a bit before the program starts streaming the audio back to your output device, so, naturally, there will be some latency, keep trying different values for the latency parameter, I recommend to set the same values for latency and buffer size, otherwise there would be some input/output underflows/overflows situations, and the audio quality may degrade heavily if the difference between those two values are too high.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/RYSKZ/Audio-Stream-Normalization/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the project.
2. Create a new branch for your feature (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Added YourFeature'`).
4. Push them to the branch you created before (`git push origin feature/YourFeature`).
5. Open a pull request.
6. Wait for it to be accepted (Thank you!).


<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Amit Karamchandani Batra - [@PollitoRex_](https://twitter.com/PollitoRex_)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [python-sounddevice](https://github.com/spatialaudio/python-sounddevice)
