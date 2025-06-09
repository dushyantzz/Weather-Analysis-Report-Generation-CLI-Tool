"""
Configuration settings for the Weather Analysis CLI tool.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenWeatherMap API configuration
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# File paths (can be overridden via CLI arguments)
DEFAULT_CITIES_FILE = 'cities.txt'
DEFAULT_DATA_FILE = 'weather_data.csv'
DEFAULT_REPORT_FILE = 'weather_report.txt'

# API settings
API_TIMEOUT = 10  # seconds
API_UNITS = 'metric'  # for Celsius temperature
API_RATE_LIMIT_DELAY = 0.1  # seconds between API calls

# Application settings
MAX_RETRIES = 3
VERBOSE_OUTPUT = True

# Temperature ranges for categorization (in Celsius)
TEMP_RANGES = {
    'very_hot': 35,
    'hot': 30,
    'warm': 25,
    'moderate': 15,
    'cool': 10
}
