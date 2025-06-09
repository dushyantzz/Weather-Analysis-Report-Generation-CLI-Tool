#!/usr/bin/env python3
"""
Weather Analysis & Report Generation CLI Tool

A Python CLI tool that fetches weather data for multiple cities,
analyzes the data, and generates comprehensive reports.
"""
import click
import os
import sys
from typing import List, Optional

from weather_api import WeatherAPI
from data_handler import DataHandler
from analyzer import WeatherAnalyzer
from report_generator import ReportGenerator
from config import DEFAULT_CITIES_FILE, DEFAULT_DATA_FILE, DEFAULT_REPORT_FILE, API_KEY


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Weather Analysis & Report Generation CLI Tool"""
    pass


@cli.command()
@click.option('--cities-file', '-f', default=DEFAULT_CITIES_FILE,
              help=f'Path to cities file (default: {DEFAULT_CITIES_FILE})')
@click.option('--output', '-o', default=DEFAULT_DATA_FILE,
              help=f'Output data file (default: {DEFAULT_DATA_FILE})')
@click.option('--format', '-fmt', type=click.Choice(['csv', 'json']), default='csv',
              help='Output format (default: csv)')
def fetch(cities_file: str, output: str, format: str):
    """Fetch weather data for cities and save to file."""
    
    # Check API key
    if not API_KEY:
        click.echo("❌ Error: Please set your OpenWeatherMap API key in the .env file")
        click.echo("Get your free API key from: https://openweathermap.org/api")
        sys.exit(1)
    
    # Initialize components
    data_handler = DataHandler(output)
    weather_api = WeatherAPI()
    
    # Read cities
    cities = data_handler.read_cities_file(cities_file)
    if not cities:
        click.echo(f"❌ No cities found in {cities_file}. Please create the file with city names (one per line).")
        sys.exit(1)
    
    click.echo(f"🌤️  Starting weather data collection for {len(cities)} cities...")
    
    # Fetch weather data
    weather_data = weather_api.fetch_multiple_cities(cities)
    
    if not weather_data:
        click.echo("❌ No weather data collected. Please check your API key and internet connection.")
        sys.exit(1)
    
    # Save data
    if format == 'json':
        success = data_handler.save_to_json(weather_data, output)
    else:
        success = data_handler.save_to_csv(weather_data)
    
    if success:
        click.echo(f"✅ Successfully saved weather data for {len(weather_data)} cities to {output}")
    else:
        click.echo("❌ Failed to save weather data.")
        sys.exit(1)


@cli.command()
@click.option('--data-file', '-d', default=DEFAULT_DATA_FILE,
              help=f'Input data file (default: {DEFAULT_DATA_FILE})')
@click.option('--report-file', '-r', default=DEFAULT_REPORT_FILE,
              help=f'Output report file (default: {DEFAULT_REPORT_FILE})')
@click.option('--show-table', '-t', is_flag=True,
              help='Include detailed data table in report')
def analyze(data_file: str, report_file: str, show_table: bool):
    """Analyze weather data and generate report."""
    
    # Initialize components
    data_handler = DataHandler(data_file)
    report_generator = ReportGenerator(report_file)
    
    # Load data
    df = data_handler.load_from_csv()
    if df is None or df.empty:
        click.echo(f"❌ No data found in {data_file}. Run 'fetch' command first.")
        sys.exit(1)
    
    click.echo(f"📊 Analyzing weather data for {len(df)} cities...")
    
    # Analyze data
    analyzer = WeatherAnalyzer(df)
    analysis = analyzer.get_comprehensive_analysis()
    
    # Generate report
    raw_data = df.to_dict('records') if show_table else None
    report_content = report_generator.generate_report(analysis, raw_data)
    
    # Save and display report
    report_generator.save_report(report_content)
    report_generator.print_report(report_content)
    
    click.echo(f"✅ Analysis complete! Report saved to {report_file}")


@cli.command()
@click.option('--cities-file', '-f', default=DEFAULT_CITIES_FILE,
              help=f'Path to cities file (default: {DEFAULT_CITIES_FILE})')
@click.option('--output', '-o', default=DEFAULT_DATA_FILE,
              help=f'Output data file (default: {DEFAULT_DATA_FILE})')
@click.option('--report-file', '-r', default=DEFAULT_REPORT_FILE,
              help=f'Output report file (default: {DEFAULT_REPORT_FILE})')
@click.option('--format', '-fmt', type=click.Choice(['csv', 'json']), default='csv',
              help='Data output format (default: csv)')
@click.option('--show-table', '-t', is_flag=True,
              help='Include detailed data table in report')
def run(cities_file: str, output: str, report_file: str, format: str, show_table: bool):
    """Run complete workflow: fetch data, analyze, and generate report."""
    
    click.echo("🚀 Starting complete weather analysis workflow...")
    
    # Step 1: Fetch data
    ctx = click.get_current_context()
    ctx.invoke(fetch, cities_file=cities_file, output=output, format=format)
    
    # Step 2: Analyze and report
    ctx.invoke(analyze, data_file=output, report_file=report_file, show_table=show_table)
    
    click.echo("🎉 Complete workflow finished successfully!")


@cli.command()
def setup():
    """Setup the project with sample files and instructions."""
    
    click.echo("🔧 Setting up Weather Analysis CLI Tool...")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write('OPENWEATHER_API_KEY=your_api_key_here\n')
        click.echo("📝 Created .env file. Please add your OpenWeatherMap API key.")
    
    # Check if cities file exists
    if not os.path.exists(DEFAULT_CITIES_FILE):
        click.echo(f"📝 Cities file {DEFAULT_CITIES_FILE} already exists with sample cities.")

    click.echo("\n📋 Setup Instructions:")
    click.echo("1. Get a free API key from: https://openweathermap.org/api")
    click.echo("2. Add your API key to the .env file:")
    click.echo("   OPENWEATHER_API_KEY=your_actual_api_key")
    click.echo(f"3. Edit {DEFAULT_CITIES_FILE} to add your desired cities (one per line)")
    click.echo("4. Run: python weather_cli.py run")
    click.echo("\n✅ Setup complete!")


if __name__ == '__main__':
    cli()
