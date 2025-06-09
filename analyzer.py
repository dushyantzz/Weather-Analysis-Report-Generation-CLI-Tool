"""
Data analysis module for weather data insights.
"""
import pandas as pd
from typing import Dict, List, Tuple, Optional
from collections import Counter
from config import TEMP_RANGES


class WeatherAnalyzer:
    """Class to analyze weather data and generate insights."""
    
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def get_temperature_stats(self) -> Dict:
        """
        Calculate temperature statistics.
        
        Returns:
            Dict: Temperature statistics
        """
        if self.data.empty:
            return {}
        
        temp_stats = {
            'highest_temp': self.data['temperature'].max(),
            'lowest_temp': self.data['temperature'].min(),
            'average_temp': round(self.data['temperature'].mean(), 1),
            'median_temp': round(self.data['temperature'].median(), 1)
        }
        
        # Find cities with highest and lowest temperatures
        highest_city = self.data.loc[self.data['temperature'].idxmax(), 'city']
        lowest_city = self.data.loc[self.data['temperature'].idxmin(), 'city']
        
        temp_stats['highest_temp_city'] = highest_city
        temp_stats['lowest_temp_city'] = lowest_city
        
        return temp_stats
    
    def get_humidity_stats(self) -> Dict:
        """
        Calculate humidity statistics.
        
        Returns:
            Dict: Humidity statistics
        """
        if self.data.empty:
            return {}
        
        return {
            'highest_humidity': self.data['humidity'].max(),
            'lowest_humidity': self.data['humidity'].min(),
            'average_humidity': round(self.data['humidity'].mean(), 1),
            'highest_humidity_city': self.data.loc[self.data['humidity'].idxmax(), 'city'],
            'lowest_humidity_city': self.data.loc[self.data['humidity'].idxmin(), 'city']
        }
    
    def get_wind_stats(self) -> Dict:
        """
        Calculate wind speed statistics.
        
        Returns:
            Dict: Wind speed statistics
        """
        if self.data.empty:
            return {}
        
        return {
            'highest_wind': self.data['wind_speed'].max(),
            'lowest_wind': self.data['wind_speed'].min(),
            'average_wind': round(self.data['wind_speed'].mean(), 1),
            'highest_wind_city': self.data.loc[self.data['wind_speed'].idxmax(), 'city'],
            'lowest_wind_city': self.data.loc[self.data['wind_speed'].idxmin(), 'city']
        }
    
    def categorize_weather(self) -> Dict[str, List[str]]:
        """
        Categorize cities by weather conditions.
        
        Returns:
            Dict: Weather categories with city lists
        """
        if self.data.empty:
            return {}
        
        weather_categories = {
            'clear': [],
            'rain': [],
            'clouds': [],
            'snow': [],
            'other': []
        }
        
        for _, row in self.data.iterrows():
            description = row['description'].lower()
            city = row['city']
            
            if any(word in description for word in ['clear', 'sunny']):
                weather_categories['clear'].append(city)
            elif any(word in description for word in ['rain', 'drizzle', 'shower']):
                weather_categories['rain'].append(city)
            elif any(word in description for word in ['cloud', 'overcast']):
                weather_categories['clouds'].append(city)
            elif any(word in description for word in ['snow', 'blizzard']):
                weather_categories['snow'].append(city)
            else:
                weather_categories['other'].append(city)
        
        return weather_categories
    
    def get_weather_distribution(self) -> Dict[str, int]:
        """
        Get distribution of weather descriptions.
        
        Returns:
            Dict: Weather description counts
        """
        if self.data.empty:
            return {}
        
        weather_counts = Counter(self.data['description'])
        return dict(weather_counts.most_common())
    
    def get_temperature_ranges(self) -> Dict[str, List[str]]:
        """
        Categorize cities by temperature ranges.
        
        Returns:
            Dict: Temperature range categories
        """
        if self.data.empty:
            return {}
        
        temp_ranges = {
            'very_hot': [],    # > configured threshold
            'hot': [],         # configured range
            'warm': [],        # configured range
            'moderate': [],    # configured range
            'cool': [],        # configured range
            'cold': []         # < configured threshold
        }

        for _, row in self.data.iterrows():
            temp = row['temperature']
            city = row['city']

            if temp > TEMP_RANGES['very_hot']:
                temp_ranges['very_hot'].append(city)
            elif temp > TEMP_RANGES['hot']:
                temp_ranges['hot'].append(city)
            elif temp > TEMP_RANGES['warm']:
                temp_ranges['warm'].append(city)
            elif temp > TEMP_RANGES['moderate']:
                temp_ranges['moderate'].append(city)
            elif temp > TEMP_RANGES['cool']:
                temp_ranges['cool'].append(city)
            else:
                temp_ranges['cold'].append(city)
        
        return temp_ranges
    
    def get_comprehensive_analysis(self) -> Dict:
        """
        Get comprehensive analysis of all weather data.
        
        Returns:
            Dict: Complete analysis results
        """
        return {
            'temperature_stats': self.get_temperature_stats(),
            'humidity_stats': self.get_humidity_stats(),
            'wind_stats': self.get_wind_stats(),
            'weather_categories': self.categorize_weather(),
            'weather_distribution': self.get_weather_distribution(),
            'temperature_ranges': self.get_temperature_ranges(),
            'total_cities': len(self.data)
        }
