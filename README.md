# Weather Analysis & Report Generation CLI Tool

A comprehensive Python CLI tool that fetches real-time weather data for multiple cities, performs detailed analysis, and generates professional reports. Perfect for weather monitoring, data analysis projects, and learning API integration.

## 🌟 Features

- **🌤️ Real-time Weather Data**: Fetch current weather from OpenWeatherMap API
- **📊 Comprehensive Analysis**: Temperature statistics, weather patterns, and trends
- **📝 Professional Reports**: Generate detailed, formatted reports with insights
- **💾 Multiple Formats**: Save data in CSV or JSON format
- **🏙️ Batch Processing**: Process multiple cities from a simple text file
- **🔧 Configurable**: Easy customization of settings and thresholds
- **⚡ CLI Interface**: User-friendly command-line interface with multiple options
- **🛡️ Error Handling**: Robust error handling for API failures and invalid data

## 📋 Requirements

- Python 3.7 or higher
- OpenWeatherMap API key (free)
- Internet connection

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or download the project
git clone <repository-url>
cd weather-analysis-cli

# Install dependencies
pip install -r requirements.txt
```

### 2. Get API Key

1. Visit [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to "API keys" section
4. Generate a new API key
5. **Important**: New API keys may take up to 2 hours to activate

### 3. Configure API Key

Edit the `.env` file and replace the placeholder with your actual API key:

```env
OPENWEATHER_API_KEY=your_actual_api_key_here
```

### 4. Prepare Cities File

Edit `cities.txt` and add your desired cities (one per line):

```
Mumbai
Delhi
Bangalore
Chennai
Kolkata
```

### 5. Run the Tool

```bash
# Complete workflow: fetch data, analyze, and generate report
python weather_cli.py run --show-table
```

## 📖 Detailed Usage

### Command Overview

The CLI tool provides several commands for different workflows:

| Command | Description |
|---------|-------------|
| `setup` | Initialize project with sample files |
| `fetch` | Fetch weather data and save to file |
| `analyze` | Analyze existing data and generate report |
| `run` | Complete workflow (fetch + analyze) |

### Individual Commands

#### Setup Command
```bash
python weather_cli.py setup
```
- Creates sample configuration files
- Provides setup instructions
- Checks for required files

#### Fetch Command
```bash
# Basic usage
python weather_cli.py fetch

# Custom options
python weather_cli.py fetch --cities-file my_cities.txt --output my_data.csv --format json
```

**Options:**
- `--cities-file, -f`: Path to cities file (default: `cities.txt`)
- `--output, -o`: Output data file (default: `weather_data.csv`)
- `--format, -fmt`: Output format - `csv` or `json` (default: `csv`)

#### Analyze Command
```bash
# Basic analysis
python weather_cli.py analyze

# Include detailed data table
python weather_cli.py analyze --show-table

# Custom files
python weather_cli.py analyze --data-file my_data.csv --report-file my_report.txt
```

**Options:**
- `--data-file, -d`: Input data file (default: `weather_data.csv`)
- `--report-file, -r`: Output report file (default: `weather_report.txt`)
- `--show-table, -t`: Include detailed data table in report

#### Run Command (Recommended)
```bash
# Complete workflow with default settings
python weather_cli.py run

# Complete workflow with all options
python weather_cli.py run --cities-file cities.txt --output weather_data.csv --report-file report.txt --format csv --show-table
```

### Help and Version
```bash
# Get help for any command
python weather_cli.py --help
python weather_cli.py fetch --help

# Check version
python weather_cli.py --version
```

## 🏗️ Project Structure

```
weather-analysis-cli/
├── 📄 weather_cli.py          # Main CLI application entry point
├── 🌐 weather_api.py          # OpenWeatherMap API integration
├── 💾 data_handler.py         # Data storage and file operations
├── 📊 analyzer.py             # Weather data analysis engine
├── 📝 report_generator.py     # Report formatting and generation
├── ⚙️ config.py               # Configuration settings and constants
├── 📦 requirements.txt        # Python package dependencies
├── 🏙️ cities.txt              # Input cities list (one per line)
├── 🔐 .env                    # Environment variables (API key)
└── 📖 README.md               # This documentation
```

### Generated Files

When you run the tool, it creates:

```
├── 📊 weather_data.csv        # Raw weather data
├── 📋 weather_report.txt      # Formatted analysis report
└── 🗂️ weather_data.json       # Alternative JSON format (if requested)
```

## 📊 Sample Output

### Console Output
```
🚀 Starting complete weather analysis workflow...
Loaded 10 cities from cities.txt
🌤️  Starting weather data collection for 10 cities...
Fetching weather data for 10 cities...
Processing 1/10: Mumbai
Processing 2/10: Delhi
...
✅ Successfully saved weather data for 10 cities to weather_data.csv
📊 Analyzing weather data for 10 cities...
✅ Analysis complete! Report saved to weather_report.txt
🎉 Complete workflow finished successfully!
```

### Generated Report
```
============================================================
WEATHER ANALYSIS REPORT
============================================================
Generated on: 2024-01-15 14:30:25
Total cities analyzed: 10

TEMPERATURE ANALYSIS
------------------------------
Highest Temperature: 35.5°C - Delhi
Lowest Temperature: 7.0°C - Shimla
Average Temperature: 26.2°C
Median Temperature: 28.0°C

WEATHER CONDITIONS
------------------------------
Clear Weather Cities: 6
  • Mumbai
  • Delhi
  • Bangalore
  • Chandigarh
  • Jaipur
  • Pune

Rain in Cities: 2
  • Shimla
  • Ahmedabad

TEMPERATURE RANGES
------------------------------
Very Hot (>35°C): 1 cities
  • Delhi

Hot (30-35°C): 2 cities
  • Jaipur
  • Chennai

Warm (25-30°C): 4 cities
  • Mumbai
  • Pune
  • Ahmedabad
  • Kolkata

ADDITIONAL METRICS
------------------------------
Humidity:
  Highest: 85% - Shimla
  Lowest: 42% - Jaipur
  Average: 65.0%

Wind Speed:
  Highest: 4.5 m/s - Shimla
  Lowest: 1.8 m/s - Bangalore
  Average: 3.1 m/s
```

## ⚙️ Configuration

### Environment Variables (.env)
```env
# OpenWeatherMap API Configuration
OPENWEATHER_API_KEY=your_api_key_here
```

### Application Settings (config.py)

You can customize various settings by editing `config.py`:

```python
# API settings
API_TIMEOUT = 10              # Request timeout in seconds
API_UNITS = 'metric'          # Temperature units (metric/imperial)
API_RATE_LIMIT_DELAY = 0.1    # Delay between API calls

# Temperature ranges for categorization (Celsius)
TEMP_RANGES = {
    'very_hot': 35,    # > 35°C
    'hot': 30,         # 30-35°C
    'warm': 25,        # 25-30°C
    'moderate': 15,    # 15-25°C
    'cool': 10         # 10-15°C
}                      # < 10°C = cold

# File paths (can be overridden via CLI)
DEFAULT_CITIES_FILE = 'cities.txt'
DEFAULT_DATA_FILE = 'weather_data.csv'
DEFAULT_REPORT_FILE = 'weather_report.txt'
```

## 🔧 Advanced Usage

### Custom Temperature Ranges
Modify the `TEMP_RANGES` in `config.py` to customize temperature categorization:

```python
TEMP_RANGES = {
    'very_hot': 40,    # Adjust for your region
    'hot': 35,
    'warm': 30,
    'moderate': 20,
    'cool': 15
}
```

### Batch Processing Multiple City Lists
```bash
# Process different city lists
python weather_cli.py run --cities-file asian_cities.txt --output asia_weather.csv
python weather_cli.py run --cities-file european_cities.txt --output europe_weather.csv
```

### Automated Scheduling
You can schedule the tool to run automatically using cron (Linux/Mac) or Task Scheduler (Windows):

```bash
# Example cron job (runs daily at 8 AM)
0 8 * * * cd /path/to/weather-cli && python weather_cli.py run
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. API Key Errors (401 Unauthorized)
```
❌ Error: Please set your OpenWeatherMap API key in the .env file
```
**Solutions:**
- Verify your API key is correct in `.env` file
- Ensure no extra spaces or quotes around the API key
- New API keys may take up to 2 hours to activate
- Check your OpenWeatherMap account status

#### 2. No Cities Found
```
❌ No cities found in cities.txt. Please create the file with city names (one per line).
```
**Solutions:**
- Create `cities.txt` file in the project directory
- Add city names, one per line
- Ensure file encoding is UTF-8

#### 3. Network/Connection Issues
```
Network error for Mumbai: Connection timeout
```
**Solutions:**
- Check your internet connection
- Verify firewall settings allow outbound HTTPS connections
- Try increasing timeout in `config.py`

#### 4. Invalid City Names
```
City 'InvalidCityName' not found.
```
**Solutions:**
- Use correct city names (English)
- Try variations: "New York" vs "New York City"
- Check spelling and remove special characters

### Debug Mode
For detailed debugging, you can modify the code to enable verbose output or add print statements in the modules.

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | 2.31.0 | HTTP requests for API calls |
| `pandas` | 2.1.4 | Data manipulation and analysis |
| `click` | 8.1.7 | Command-line interface framework |
| `python-dotenv` | 1.0.0 | Environment variable management |
| `tabulate` | 0.9.0 | Table formatting for reports |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Click](https://click.palletsprojects.com/) for the excellent CLI framework
- [Pandas](https://pandas.pydata.org/) for powerful data analysis capabilities

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the OpenWeatherMap API documentation
3. Create an issue in the project repository
4. Ensure you're using the latest version of the tool

---

**Happy Weather Analyzing! 🌤️📊**
#
