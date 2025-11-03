# Speech Recognition Application

A simple yet powerful speech recognition application built with Python that uses Google's Speech Recognition API to convert speech to text in real-time.

## Features

- 🎤 Real-time speech recognition using Google Speech API
- 🖥️ Clean and intuitive GUI built with Tkinter
- 🔍 Keyword detection - highlights when the word "stop" is detected
- 📝 Console output for all recognized speech
- ⚡ Easy to use - just click and speak

## Requirements

- Python 3.6 or higher
- Internet connection (for Google Speech Recognition API)
- Microphone

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Speech-Recognition.git
cd Speech-Recognition
```

2. Install required dependencies:
```bash
pip install SpeechRecognition
pip install pyaudio
```

**Note for Windows users:** If you encounter issues installing PyAudio, download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using:
```bash
pip install path/to/PyAudio-x.x.x-cpxx-cpxx-win_xxx.whl
```

**Note for macOS users:**
```bash
brew install portaudio
pip install pyaudio
```

**Note for Linux users:**
```bash
sudo apt-get install python3-pyaudio
```

## Usage

Run the application:
```bash
python speechrecognition.py
```

1. A window will appear with a "Speak" button
2. Click the "Speak" button
3. Start speaking into your microphone
4. The recognized text will appear in the console
5. If you say "stop", the label will update to show "Stop"

## How It Works

The application uses the following technologies:

- **SpeechRecognition library**: Provides easy access to speech recognition APIs
- **Google Speech Recognition API**: Converts audio to text
- **Tkinter**: Creates the graphical user interface
- **PyAudio**: Handles microphone input


## Code Overview

The application consists of:

1. **GUI Setup**: Creates a 600x600 window with a black background
2. **Speech Recognition**: Uses the SpeechRecognition library to capture and process audio
3. **Keyword Detection**: Checks if the word "stop" is present in the recognized text
4. **Error Handling**: Manages cases where audio cannot be understood or API errors occur


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Contact

If you have any questions or suggestions, please open an issue on GitHub.

---

**Note**: This application requires an active internet connection as it uses Google's cloud-based Speech Recognition API.
