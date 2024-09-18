#1. Refactoring a Weather Forecast Application into Classes and Modules
#Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. 
#Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

# Weather Forecast Application Script

class WeatherFetcher: # created class that focuses on fetching the weather, kept the fetch weather function
    def __init__(self):
        # Simulated data based on city
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})

class WeatherParser: # created a class that focus on parsing the weather, kept the parse weather data function
    def parse_short_data(self, data):
        # added this function to parse shortened weather data, to go along with the choice of detailed or not
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        return f"Weather in {city}: {temperature} degrees"
    def parse_detailed_data(self, data):
        # Function to parse full weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class WeatherDisplay: # created a class that focuses on displaying the weather, either detailed or shortened. Kept both functions the same
    def __init__(self):
        self.fetcher = WeatherFetcher()
        self.parser = WeatherParser()
    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_detailed_data(data)
    def get_short_forecast(self, city):
        # Function to display the basic weather forecast for a city
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_short_data(data)
            print(weather_report)

def main():
    while True:
        try:
            display_function = WeatherDisplay()
            city = input("For the weather, enter city (New York, London or Tokyo) or enter 'exit' to quit: ").title()
            if city == 'Exit':
                break
            elif city is "New York" or "London" or "Tokyo":
                detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
                if detailed == 'yes':
                    forecast = display_function.get_detailed_forecast(city)
                    print(forecast)
                elif detailed == 'no':
                    forecast = display_function.get_short_forecast(city)
                else:
                    print("Please type yes or no")
            else:
                print(f"Sorry, '{city}' isn't on the list. Please choose New York, London or Tokyo.")
        except Exception as e:
            print(f"Error message: '{e}' - please try again.")

if __name__ == "__main__":
    main()