#!/usr/bin/env python3
"""
Installation script for Jarvis Voice Assistant
This script helps set up the required dependencies
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def install_dependencies():
    """Install required Python packages"""
    print("Installing dependencies...")
    
    # Check if pip is available
    success, stdout, stderr = run_command("pip --version")
    if not success:
        print("Error: pip is not available. Please install Python and pip first.")
        return False
    
    # Install packages from requirements.txt
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        success, stdout, stderr = run_command(f"pip install -r {requirements_file}")
        if success:
            print("✓ Dependencies installed successfully!")
            return True
        else:
            print(f"✗ Error installing dependencies: {stderr}")
            return False
    else:
        print("✗ requirements.txt not found")
        return False

def check_audio_dependencies():
    """Check and install system audio dependencies"""
    print("\nChecking audio dependencies...")
    
    # For Linux systems
    if sys.platform.startswith('linux'):
        print("Installing PortAudio (required for audio input)...")
        success, stdout, stderr = run_command("sudo apt-get update && sudo apt-get install -y portaudio19-dev python3-pyaudio")
        if success:
            print("✓ PortAudio installed successfully!")
        else:
            print(f"✗ Error installing PortAudio: {stderr}")
    
    # For macOS
    elif sys.platform == 'darwin':
        print("macOS detected - audio dependencies should be available")
    
    # For Windows
    elif sys.platform == 'win32':
        print("Windows detected - audio dependencies should be available")
    
    return True

def setup_environment():
    """Set up environment configuration"""
    print("\nSetting up environment...")
    
    env_file = ".env"
    if not os.path.exists(env_file):
        print("✓ .env file created (please update with your API keys)")
    else:
        print("✓ .env file already exists")
    
    print("\nPlease update the .env file with your OpenWeatherMap API key:")
    print("1. Go to https://openweathermap.org/api")
    print("2. Sign up for a free account")
    print("3. Get your API key")
    print("4. Update WEATHER_API_KEY in the .env file")
    
    return True

def main():
    """Main installation function"""
    print("=" * 50)
    print("Jarvis Voice Assistant - Installation")
    print("=" * 50)
    
    # Install Python dependencies
    if not install_dependencies():
        return
    
    # Check audio dependencies
    check_audio_dependencies()
    
    # Setup environment
    setup_environment()
    
    print("\n" + "=" * 50)
    print("Installation complete!")
    print("Next steps:")
    print("1. Update the .env file with your API keys")
    print("2. Run: python jarvis.py")
    print("3. Say 'Jarvis' to activate the assistant")
    print("=" * 50)

if __name__ == "__main__":
    main()
