#Jamie Sosnowski
#Project

#import required modules
import json, requests

#display welcome message
print("Welcome to my weather forecast program.")

def main():
    # Ask the user for their city
    location = input("Please enter your city or zipcode: ") 
    
    # Use the city name to obtain weather forecast data from openweathermap.org
    try:
        api_key = "7772ea8499128e22e78566292a20a525" #identify api_key
      #create complete_url
        complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}" #use f string to complete url. f string = base url, personal api key, unit measurement, and the location/User input
        response = requests.get(complete_url) #get method of requests module return response object
        
        # Validate whether the user entered valid data
        if response.status_code != 200:
            print("Invalid location. Please try again.")
            return
        
        # Display the weather forecast in a readable format to the user
        data = response.json()
        print("Weather forecast for", data["name"] + ":")
        print("Temperature:", data["main"]["temp"], "degrees Fahrenheit")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Description:", data["weather"][0]["description"])
        
    except requests.exceptions.RequestException as e:
        # Print a message to the user indicating whether or not the connection was successful
        print("Error: Unable to establish connection to the webservice.")

if __name__ == "__main__":
    while True:
        main()
        # Allow the user to run the program multiple times
        run_again = input("Do you want to run the program again? (y/n) ")
        if run_again.lower() != "y":
          break
#display farewell message          
print("Thank you for using my weather forecast program.")