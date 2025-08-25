"""
Advanced features for Jarvis Voice Assistant
Additional functionalities that can be integrated
"""

import os
import subprocess
import webbrowser
import random
from datetime import datetime

class AdvancedFeatures:
    def __init__(self):
        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
            "Stay hungry, stay foolish. - Steve Jobs",
            "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
        ]
        
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Greetings! I'm here to help.",
            "Hello! Ready to be productive?",
            "Hi! What's on your mind today?"
        ]

    def open_application(self, app_name):
        """Open system applications"""
        apps = {
            'calculator': 'calc' if os.name == 'nt' else 'gnome-calculator',
            'notepad': 'notepad' if os.name == 'nt' else 'gedit',
            'browser': 'start chrome' if os.name == 'nt' else 'google-chrome',
            'terminal': 'cmd' if os.name == 'nt' else 'gnome-terminal'
        }
        
        if app_name in apps:
            try:
                subprocess.Popen(apps[app_name], shell=True)
                return f"Opening {app_name}"
            except Exception as e:
                return f"Could not open {app_name}: {str(e)}"
        return f"Application {app_name} not found"

    def open_website(self, website):
        """Open websites in default browser"""
        websites = {
            'google': 'https://www.google.com',
            'youtube': 'https://www.youtube.com',
            'github': 'https://www.github.com',
            'netflix': 'https://www.netflix.com',
            'spotify': 'https://www.spotify.com'
        }
        
        if website in websites:
            webbrowser.open(websites[website])
            return f"Opening {website}"
        return f"Website {website} not configured"

    def system_info(self):
        """Get system information"""
        import platform
        import psutil
        
        info = {
            'system': platform.system(),
            'processor': platform.processor(),
            'memory': f"{psutil.virtual_memory().percent}% used",
            'disk': f"{psutil.disk_usage('/').percent}% used"
        }
        
        return f"System: {info['system']}, Processor: {info['processor']}, Memory: {info['memory']}, Disk: {info['disk']}"

    def random_quote(self):
        """Get a random inspirational quote"""
        return random.choice(self.quotes)

    def random_greeting(self):
        """Get a random greeting"""
        return random.choice(self.greetings)

    def set_reminder(self, task, time):
        """Set a simple reminder (basic implementation)"""
        # This is a basic implementation - in a real app, you'd use a scheduler
        return f"I'll remind you to {task} at {time}"

    def calculate(self, expression):
        """Simple calculator function"""
        try:
            # Basic safety check
            allowed_chars = '0123456789+-*/(). '
            if all(char in allowed_chars for char in expression):
                result = eval(expression)
                return f"The result is {result}"
            else:
                return "Invalid calculation expression"
        except Exception as e:
            return f"Calculation error: {str(e)}"

    def get_news_headlines(self):
        """Get news headlines (placeholder - would need news API)"""
        return "News feature requires a news API key. You can integrate with NewsAPI.org"

    def get_stock_price(self, symbol):
        """Get stock price (placeholder - would need stock API)"""
        return f"Stock price for {symbol} would require a financial API integration"

    def create_note(self, note_text):
        """Create a simple text note"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"note_{timestamp}.txt"
            with open(filename, 'w') as f:
                f.write(note_text)
            return f"Note saved as {filename}"
        except Exception as e:
            return f"Error saving note: {str(e)}"

# Example usage and integration with main Jarvis class
def integrate_advanced_features(jarvis_instance):
    """Integrate advanced features into the main Jarvis instance"""
    advanced = AdvancedFeatures()
    
    # Add new command processing
    def advanced_process_command(self, command):
        # Existing commands...
        if 'open' in command:
            if 'calculator' in command:
                return advanced.open_application('calculator')
            elif 'notepad' in command:
                return advanced.open_application('notepad')
            elif 'browser' in command:
                return advanced.open_application('browser')
            elif 'terminal' in command:
                return advanced.open_application('terminal')
        
        elif 'website' in command:
            site = command.replace('open website', '').replace('open', '').strip()
            return advanced.open_website(site)
        
        elif 'system info' in command:
            return advanced.system_info()
        
        elif 'quote' in command:
            return advanced.random_quote()
        
        elif 'calculate' in command:
            expression = command.replace('calculate', '').strip()
            return advanced.calculate(expression)
        
        elif 'create note' in command:
            note_text = command.replace('create note', '').strip()
            return advanced.create_note(note_text)
        
        # Fall back to original processing
        return None
    
    # Monkey patch the process_command method
    original_process_command = jarvis_instance.process_command
    
    def new_process_command(self, command):
        result = advanced_process_command(self, command)
        if result is not None:
            self.speak(result)
            return True
        return original_process_command(command)
    
    jarvis_instance.process_command = new_process_command.__get__(jarvis_instance, type(jarvis_instance))
    
    return jarvis_instance
