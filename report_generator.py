"""
Report generation module for creating formatted weather reports.
"""
import os
from datetime import datetime
from typing import Dict, List
from tabulate import tabulate
from config import DEFAULT_REPORT_FILE


class ReportGenerator:
    """Class to generate formatted weather reports."""
    
    def __init__(self, report_file: str = DEFAULT_REPORT_FILE):
        self.report_file = report_file
    
    def generate_report(self, analysis: Dict, raw_data: List[Dict] = None) -> str:
        """
        Generate a comprehensive weather report.
        
        Args:
            analysis (Dict): Analysis results from WeatherAnalyzer
            raw_data (List[Dict]): Raw weather data (optional)
            
        Returns:
            str: Formatted report content
        """
        report_lines = []
        
        # Header
        report_lines.append("=" * 60)
        report_lines.append("WEATHER ANALYSIS REPORT")
        report_lines.append("=" * 60)
        report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Total cities analyzed: {analysis.get('total_cities', 0)}")
        report_lines.append("")
        
        # Temperature Analysis
        temp_stats = analysis.get('temperature_stats', {})
        if temp_stats:
            report_lines.append("TEMPERATURE ANALYSIS")
            report_lines.append("-" * 30)
            report_lines.append(f"Highest Temperature: {temp_stats.get('highest_temp', 'N/A')}°C - {temp_stats.get('highest_temp_city', 'N/A')}")
            report_lines.append(f"Lowest Temperature: {temp_stats.get('lowest_temp', 'N/A')}°C - {temp_stats.get('lowest_temp_city', 'N/A')}")
            report_lines.append(f"Average Temperature: {temp_stats.get('average_temp', 'N/A')}°C")
            report_lines.append(f"Median Temperature: {temp_stats.get('median_temp', 'N/A')}°C")
            report_lines.append("")
        
        # Weather Categories
        weather_cats = analysis.get('weather_categories', {})
        if weather_cats:
            report_lines.append("WEATHER CONDITIONS")
            report_lines.append("-" * 30)
            
            clear_cities = weather_cats.get('clear', [])
            if clear_cities:
                report_lines.append(f"Clear Weather Cities: {len(clear_cities)}")
                for city in clear_cities:
                    report_lines.append(f"  • {city}")
                report_lines.append("")
            
            rain_cities = weather_cats.get('rain', [])
            if rain_cities:
                report_lines.append(f"Rain in Cities: {len(rain_cities)}")
                for city in rain_cities:
                    report_lines.append(f"  • {city}")
                report_lines.append("")
            
            cloud_cities = weather_cats.get('clouds', [])
            if cloud_cities:
                report_lines.append(f"Cloudy Cities: {len(cloud_cities)}")
                for city in cloud_cities:
                    report_lines.append(f"  • {city}")
                report_lines.append("")
        
        # Temperature Ranges
        temp_ranges = analysis.get('temperature_ranges', {})
        if temp_ranges:
            report_lines.append("TEMPERATURE RANGES")
            report_lines.append("-" * 30)
            
            range_labels = {
                'very_hot': 'Very Hot (>35°C)',
                'hot': 'Hot (30-35°C)',
                'warm': 'Warm (25-30°C)',
                'moderate': 'Moderate (15-25°C)',
                'cool': 'Cool (10-15°C)',
                'cold': 'Cold (<10°C)'
            }
            
            for range_key, cities in temp_ranges.items():
                if cities:
                    label = range_labels.get(range_key, range_key.title())
                    report_lines.append(f"{label}: {len(cities)} cities")
                    for city in cities:
                        report_lines.append(f"  • {city}")
                    report_lines.append("")
        
        # Humidity and Wind Analysis
        humidity_stats = analysis.get('humidity_stats', {})
        wind_stats = analysis.get('wind_stats', {})
        
        if humidity_stats or wind_stats:
            report_lines.append("ADDITIONAL METRICS")
            report_lines.append("-" * 30)
            
            if humidity_stats:
                report_lines.append("Humidity:")
                report_lines.append(f"  Highest: {humidity_stats.get('highest_humidity', 'N/A')}% - {humidity_stats.get('highest_humidity_city', 'N/A')}")
                report_lines.append(f"  Lowest: {humidity_stats.get('lowest_humidity', 'N/A')}% - {humidity_stats.get('lowest_humidity_city', 'N/A')}")
                report_lines.append(f"  Average: {humidity_stats.get('average_humidity', 'N/A')}%")
                report_lines.append("")
            
            if wind_stats:
                report_lines.append("Wind Speed:")
                report_lines.append(f"  Highest: {wind_stats.get('highest_wind', 'N/A')} m/s - {wind_stats.get('highest_wind_city', 'N/A')}")
                report_lines.append(f"  Lowest: {wind_stats.get('lowest_wind', 'N/A')} m/s - {wind_stats.get('lowest_wind_city', 'N/A')}")
                report_lines.append(f"  Average: {wind_stats.get('average_wind', 'N/A')} m/s")
                report_lines.append("")
        
        # Raw data table (if provided)
        if raw_data:
            report_lines.append("DETAILED WEATHER DATA")
            report_lines.append("-" * 30)
            
            table_data = []
            for item in raw_data:
                table_data.append([
                    item.get('city', 'N/A'),
                    f"{item.get('temperature', 'N/A')}°C",
                    f"{item.get('humidity', 'N/A')}%",
                    item.get('description', 'N/A'),
                    f"{item.get('wind_speed', 'N/A')} m/s"
                ])
            
            headers = ['City', 'Temperature', 'Humidity', 'Description', 'Wind Speed']
            table = tabulate(table_data, headers=headers, tablefmt='grid')
            report_lines.append(table)
            report_lines.append("")
        
        report_lines.append("=" * 60)
        report_lines.append("End of Report")
        report_lines.append("=" * 60)
        
        return "\n".join(report_lines)
    
    def save_report(self, report_content: str) -> bool:
        """
        Save report to file.
        
        Args:
            report_content (str): Report content to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(self.report_file, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            print(f"Report saved to {self.report_file}")
            return True
            
        except Exception as e:
            print(f"Error saving report: {e}")
            return False
    
    def print_report(self, report_content: str):
        """
        Print report to console.
        
        Args:
            report_content (str): Report content to print
        """
        print(report_content)
