import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Jarvis:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Speed of speech
        self.engine.setProperty('volume', 0.9)  # Volume level
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Weather API key (you can get one from openweathermap.org)
        self.weather_api_key = os.getenv('WEATHER_API_KEY', 'your_api_key_here')
        
        print("Jarvis initialized. Say 'Jarvis' to activate...")

    def speak(self, text):
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen for voice commands"""
        try:
            with self.microphone as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            command = self.recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            self.speak("Sorry, I'm having trouble with the speech recognition service.")
            return ""
        except sr.WaitTimeoutError:
            return ""

    def get_time(self):
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")

    def get_date(self):
        """Get current date"""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")

    def search_wikipedia(self, query):
        """Search Wikipedia"""
        try:
            result = wikipedia.summary(query, sentences=2)
            self.speak(f"According to Wikipedia: {result}")
        except wikipedia.exceptions.DisambiguationError as e:
            self.speak(f"There are multiple results for {query}. Please be more specific.")
        except wikipedia.exceptions.PageError:
            self.speak(f"Sorry, I couldn't find information about {query}.")

    def play_on_youtube(self, query):
        """Play video on YouTube"""
        self.speak(f"Playing {query} on YouTube")
        pywhatkit.playonyt(query)

    def tell_joke(self):
        """Tell a joke"""
        joke = pyjokes.get_joke()
        self.speak(joke)

    def get_weather(self, city="current location"):
        """Get weather information"""
        if city == "current location":
            # For simplicity, using a default city
            city = "New York"
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if data["cod"] != "404":
                main = data["main"]
                weather = data["weather"][0]
                temperature = main["temp"]
                description = weather["description"]
                self.speak(f"The temperature in {city} is {temperature}°C with {description}")
            else:
                self.speak(f"Sorry, I couldn't find weather information for {city}.")
        except Exception as e:
            self.speak("Sorry, I'm having trouble accessing weather information.")

    def process_command(self, command):
        """Process the voice command"""
        if 'time' in command:
            self.get_time()
        elif 'date' in command:
            self.get_date()
        elif 'wikipedia' in command or 'search for' in command:
            query = command.replace('wikipedia', '').replace('search for', '').strip()
            self.search_wikipedia(query)
        elif 'play' in command and 'youtube' in command:
            query = command.replace('play', '').replace('on youtube', '').strip()
            self.play_on_youtube(query)
        elif 'joke' in command:
            self.tell_joke()
        elif 'weather' in command:
            if 'in' in command:
                city = command.split('in')[-1].strip()
                self.get_weather(city)
            else:
                self.get_weather()
        elif 'exit' in command or 'quit' in command or 'stop' in command:
            self.speak("Goodbye! Have a great day!")
            return False
        else:
            self.speak("I'm sorry, I didn't understand that command. Please try again.")
        
        return True

    def run(self):
        """Main loop for Jarvis"""
        running = True
        while running:
            try:
                command = self.listen()
                if 'jarvis' in command:
                    self.speak("Yes, how can I help you?")
                    command = self.listen()
                    running = self.process_command(command)
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
