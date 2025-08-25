# Jarvis Voice Assistant

A Python-based voice assistant inspired by Iron Man's Jarvis, capable of voice recognition and various tasks.

## Features

- **Voice Recognition**: Listen and respond to voice commands
- **Text-to-Speech**: Speak responses back to you
- **Time and Date**: Get current time and date
- **Wikipedia Search**: Search for information on Wikipedia
- **YouTube Playback**: Play videos on YouTube
- **Jokes**: Tell random jokes
- **Weather Information**: Get weather updates (requires API key)
- **Customizable**: Easy to extend with new features

## Installation

1. Clone or download this project
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Update the `.env` file with your API key

## Usage

Run the assistant:
```bash
python jarvis.py
```

## Voice Commands

- "Jarvis" - Wake word to activate the assistant
- "what time is it" - Get current time
- "what's the date" - Get current date
- "search for [topic] on wikipedia" - Search Wikipedia
- "play [song/video] on youtube" - Play on YouTube
- "tell me a joke" - Hear a random joke
- "what's the weather in [city]" - Get weather information
- "exit" or "quit" - Stop the assistant

## Customization

You can easily add new features by:

1. Adding new command patterns in the `process_command` method
2. Creating new methods for specific functionalities
3. Adding new API integrations

## Dependencies

- `speechrecognition` - Voice recognition
- `pyttsx3` - Text-to-speech
- `pywhatkit` - YouTube integration
- `wikipedia` - Wikipedia search
- `pyjokes` - Jokes
- `requests` - API calls
- `python-dotenv` - Environment variables

## Notes

- Make sure you have a working microphone
- Internet connection required for most features
- For weather functionality, you need to set up an OpenWeatherMap API key
