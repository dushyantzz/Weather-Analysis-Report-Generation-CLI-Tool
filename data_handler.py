"""
Data handling module for saving and loading weather data.
"""
import pandas as pd
import json
import os
from typing import List, Dict, Optional
from config import DEFAULT_DATA_FILE


class DataHandler:
    """Class to handle data storage and retrieval operations."""
    
    def __init__(self, data_file: str = DEFAULT_DATA_FILE):
        self.data_file = data_file
    
    def save_to_csv(self, weather_data: List[Dict]) -> bool:
        """
        Save weather data to CSV file.
        
        Args:
            weather_data (List[Dict]): List of weather data dictionaries
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not weather_data:
                print("No data to save.")
                return False
            
            df = pd.DataFrame(weather_data)
            df.to_csv(self.data_file, index=False)
            print(f"Data saved to {self.data_file}")
            return True
            
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
            return False
    
    def save_to_json(self, weather_data: List[Dict], filename: str = None) -> bool:
        """
        Save weather data to JSON file.
        
        Args:
            weather_data (List[Dict]): List of weather data dictionaries
            filename (str): Optional custom filename
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not weather_data:
                print("No data to save.")
                return False
            
            json_file = filename or self.data_file.replace('.csv', '.json')
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(weather_data, f, indent=2, ensure_ascii=False)
            
            print(f"Data saved to {json_file}")
            return True
            
        except Exception as e:
            print(f"Error saving data to JSON: {e}")
            return False
    
    def load_from_csv(self) -> Optional[pd.DataFrame]:
        """
        Load weather data from CSV file.
        
        Returns:
            pd.DataFrame: Weather data or None if failed
        """
        try:
            if not os.path.exists(self.data_file):
                print(f"Data file {self.data_file} not found.")
                return None
            
            df = pd.read_csv(self.data_file)
            print(f"Data loaded from {self.data_file}")
            return df
            
        except Exception as e:
            print(f"Error loading data from CSV: {e}")
            return None
    
    def load_from_json(self, filename: str = None) -> Optional[List[Dict]]:
        """
        Load weather data from JSON file.
        
        Args:
            filename (str): Optional custom filename
            
        Returns:
            List[Dict]: Weather data or None if failed
        """
        try:
            json_file = filename or self.data_file.replace('.csv', '.json')
            
            if not os.path.exists(json_file):
                print(f"Data file {json_file} not found.")
                return None
            
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"Data loaded from {json_file}")
            return data
            
        except Exception as e:
            print(f"Error loading data from JSON: {e}")
            return None
    
    def read_cities_file(self, cities_file: str) -> List[str]:
        """
        Read city names from text file.
        
        Args:
            cities_file (str): Path to cities file
            
        Returns:
            List[str]: List of city names
        """
        try:
            if not os.path.exists(cities_file):
                print(f"Cities file {cities_file} not found.")
                return []
            
            with open(cities_file, 'r', encoding='utf-8') as f:
                cities = [line.strip() for line in f if line.strip()]
            
            print(f"Loaded {len(cities)} cities from {cities_file}")
            return cities
            
        except Exception as e:
            print(f"Error reading cities file: {e}")
            return []
