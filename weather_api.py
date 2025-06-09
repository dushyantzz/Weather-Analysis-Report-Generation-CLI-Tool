"""
Weather API integration module for fetching weather data from OpenWeatherMap.
"""
import requests
import time
from typing import Dict, Optional, List
from config import API_KEY, BASE_URL, API_TIMEOUT, API_UNITS, API_RATE_LIMIT_DELAY, MAX_RETRIES


class WeatherAPI:
    """Class to handle weather API operations."""
    
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.timeout = API_TIMEOUT
        self.units = API_UNITS
    
    def fetch_weather_data(self, city: str) -> Optional[Dict]:
        """
        Fetch weather data for a specific city.
        
        Args:
            city (str): Name of the city
            
        Returns:
            Dict: Weather data or None if failed
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': self.units
            }
            
            response = requests.get(
                self.base_url,
                params=params,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                return self._parse_weather_data(data, city)
            elif response.status_code == 404:
                print(f"City '{city}' not found.")
                return None
            else:
                print(f"Error fetching data for {city}: {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Network error for {city}: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error for {city}: {e}")
            return None
    
    def _parse_weather_data(self, data: Dict, city: str) -> Dict:
        """
        Parse raw API response into structured weather data.
        
        Args:
            data (Dict): Raw API response
            city (str): City name
            
        Returns:
            Dict: Parsed weather data
        """
        return {
            'city': city,
            'temperature': round(data['main']['temp'], 1),
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].title(),
            'wind_speed': round(data['wind']['speed'], 1),
            'country': data['sys']['country'],
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def fetch_multiple_cities(self, cities: List[str]) -> List[Dict]:
        """
        Fetch weather data for multiple cities.
        
        Args:
            cities (List[str]): List of city names
            
        Returns:
            List[Dict]: List of weather data dictionaries
        """
        weather_data = []
        total_cities = len(cities)
        
        print(f"Fetching weather data for {total_cities} cities...")
        
        for i, city in enumerate(cities, 1):
            print(f"Processing {i}/{total_cities}: {city}")
            
            data = self.fetch_weather_data(city.strip())
            if data:
                weather_data.append(data)
            
            # Add small delay to avoid hitting API rate limits
            if i < total_cities:
                time.sleep(API_RATE_LIMIT_DELAY)
        
        print(f"Successfully fetched data for {len(weather_data)} cities.")
        return weather_data
