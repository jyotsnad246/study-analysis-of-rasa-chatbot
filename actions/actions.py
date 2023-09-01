from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from datetime import date as dt, timedelta

class ActionWeatherTracker1(Action):

    def name(self) -> Text:
        return "action_weather_tracker_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "5d7f3058157d9c9e54b4b60f488e7045"
        city = ""
        weather_desc = ""
        wind_speed = ""
        humidity = ""
        temperature = ""
        #end_point = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'city':
                city = tracker['value']

        end_point = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

        response = requests.get(end_point).json()
        #print(response)

        weather_desc = response['weather'][0]['description']
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        temperature = response['main']['temp']

        message = "It's " + weather_desc + " weather and temperature is " + str(temperature) + " of Celcius. The wind speed is " + str(wind_speed) + "metre/sec and the humidity is " + str(humidity) + "% at " + city
        dispatcher.utter_message(text = message)

        return []
    
class ActionWeatherTracker2(Action):

    def name(self) -> Text:
        return "action_weather_tracker_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "5f39ac098bfb1d20edb29bbc65746da8"
        city = ""
        weather_desc = ""
        wind_speed = ""
        humidity = ""
        temperature = ""
        #end_point = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'city':
                city = tracker['value']

        end_point = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

        response = requests.get(end_point).json()
        #print(response)

        weather_desc = response['weather'][0]['description']
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        temperature = response['main']['temp']

        message = "Sure! It's " + weather_desc + " weather and temperature is " + str(temperature) + " of Celcius. The wind speed is " + str(wind_speed) + "metre/sec and the humidity is " + str(humidity) + "% at " + city
        dispatcher.utter_message(text = message)

        return []
    
class ActionWeatherForecast1(Action):

    def name(self) -> Text:
        return "action_weather_forecast_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "5f39ac098bfb1d20edb29bbc65746da8"
        city = ""
        weather_desc = ""
        weather_desc_2 = ""
        temperature = ""
        message = ""
        #end_point = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

        trackers = tracker.latest_message['entities']
        print(trackers)

        item = tracker.get_slot("item")
        date = tracker.get_slot("date")

        print(item)
        print(date)

        current_date = dt.today()
        tomorrow_date = current_date + timedelta(days=1)
        print("Tomorrow's date:", tomorrow_date)

        for tracker in trackers:
            if tracker['entity'] == 'city':
                city = tracker['value']

        end_point = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + api_key + "&units=metric"

        response = requests.get(end_point).json()
        #print(response)

        dt_txt = response["list"][6]["dt_txt"]
        weather_desc = response["list"][6]['weather'][0]['main']
        weather_desc_2 = response["list"][6]['weather'][0]['description']
        temperature = response["list"][6]['main']['temp']

        if date == "tomorrow":
            if item == "umbrella":
                if weather_desc == "Rain":
                    message = "Yes!, you better take an umbrella tomorrow"
                else:
                    message = "No. You don't need to take an umbrella tomorrow"
            else:
                message = "Tomorrow will be " + weather_desc_2 + " weather with " + str(temperature) + " Celcius of temperature at " + city
        elif date == "today":
            if item == "umbrella":
                if weather_desc == "Rain":
                    message = "Yes!, you better take an umbrella today"
                else:
                    message = "No. You don't need to take an umbrella today"

        dispatcher.utter_message(text = message)

        return [SlotSet("item", None)]
    
class ActionWeatherForecast2(Action):

    def name(self) -> Text:
        return "action_weather_forecast_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "5f39ac098bfb1d20edb29bbc65746da8"
        date = ""
        item = ""
        city = ""
        weather_desc = ""
        weather_desc_2 = ""
        wind_speed = ""
        humidity = ""
        temperature = ""
        message = ""
        #end_point = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

        trackers = tracker.latest_message['entities']
        print(trackers)

        current_date = dt.today()
        tomorrow_date = current_date + timedelta(days=1)
        print("Tomorrow's date:", tomorrow_date)

        for tracker in trackers:
            if tracker['entity'] == 'city':
                city = tracker['value']
            if tracker["entity"] == 'date':
                date = tracker["value"]
            if tracker["entity"] == 'item':
                item = tracker["value"]
        
        print(date)
        print(item)

        end_point = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + api_key + "&units=metric"

        response = requests.get(end_point).json()
        #print(response)

        dt_txt = response["list"][6]["dt_txt"]
        weather_desc = response["list"][6]['weather'][0]['main']
        weather_desc_2 = response["list"][6]['weather'][0]['description']
        temperature = response["list"][6]['main']['temp']

        if date == "tomorrow":
            if item == "umbrella":
                if weather_desc == "Rain":
                    message = "Yes!, you better take an umbrella tomorrow"
                else:
                    message = "No. You don't need to take an umbrella tomorrow"
            else:
                message = "Tomorrow will be " + weather_desc_2 + " weather with " + str(temperature) + " Celcius of temperature at " + city
        elif date == "today":
            if item == "umbrella":
                if weather_desc == "Rain":
                    message = "Yes!, you better take an umbrella today"
                else:
                    message = "No. You don't need to take an umbrella today"

        dispatcher.utter_message(text = message)

        return []
    
class ActionWeatherForecast3(Action):

    def name(self) -> Text:
        return "action_weather_forecast_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "5f39ac098bfb1d20edb29bbc65746da8"
        city = ""
        weather_desc = ""
        weather_desc_2 = ""
        wind_speed = ""
        humidity = ""
        temperature = ""
        message = ""
        #end_point = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

        trackers = tracker.latest_message['entities']
        print(trackers)

        date = tracker.get_slot("date")
        condition = tracker.get_slot("condition")
        item = tracker.get_slot("item")

        print(item)
        print(date)
        print(condition)

        current_date = dt.today()
        tomorrow_date = current_date + timedelta(days=1)
        print("Tomorrow's date:", tomorrow_date)

        for tracker in trackers:
            if tracker['entity'] == 'city':
                city = tracker['value']

        end_point = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + api_key + "&units=metric"

        response = requests.get(end_point).json()
        #print(response)

        dt_txt = response["list"][6]["dt_txt"]
        weather_desc = response["list"][6]['weather'][0]['main']
        weather_desc_2 = response["list"][6]['weather'][0]['description']
        wind_speed = response["list"][6]['wind']['speed']
        humidity = response["list"][6]['main']['humidity']
        temperature = response["list"][6]['main']['temp']

        if date == "tomorrow":
            if condition == "temperature":
                message = "Tomorrow temperature will be " + str(temperature) + " of Celcius at " + city
            elif condition == "humid" or condition == "humidity":
                message = "Tomorrow Humidity will be " + str(humidity) + "% at " + city
            elif condition == "rainy" or condition == "rain":
                if weather_desc == "Rain":
                    message = "Tomorrow will be rainy weather at " + city
            elif condition == "cold" or condition == "hot":
                if temperature >= 10.0 and temperature < 18.0:
                    message = "Tomorrow will be cold weather at " + city
                elif temperature >= 0.0 and temperature < 10.0:
                    message = "Tomorrow will be moderate cold weather at " + city
                elif temperature < 0.0:
                    message = "Tomorrow will be very cold weather at " + city
                elif temperature >= 18.0 and temperature < 28.0:
                    message = "Tomorrow will be mild weather at " + city
                elif temperature >= 28.0 and temperature < 35.0:
                    message = "Tomorrow will be hot weather at " + city
                else:
                    message = "Tomorrow Humidity will be very hot weather outside at " + city
            elif condition == "windy":
                message = "The wind speed will be " +str(wind_speed) + "m/s at tomorrow at " + city

        elif date == "today":
            message = "triggered forecast 3"

        dispatcher.utter_message(text = message)

        return []
    
class ActionWeatherForecast4(Action):

    def name(self) -> Text:
        return "action_weather_forecast_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        api_key = "5f39ac098bfb1d20edb29bbc65746da8"
        date = ""
        city = ""
        condition = ""
        weather_desc = ""
        weather_desc_2 = ""
        wind_speed = ""
        humidity = ""
        temperature = ""
        message = ""
        #end_point = "https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

        trackers = tracker.latest_message['entities']
        print(trackers)

        current_date = dt.today()
        tomorrow_date = current_date + timedelta(days=1)
        print("Tomorrow's date:", tomorrow_date)

        for tracker in trackers:
            if tracker['entity'] == 'city':
                city = tracker['value']
            if tracker["entity"] == 'date':
                date = tracker["value"]
            if tracker["entity"] == 'condition':
                condition = tracker["value"]
        
        print(date)
        print(condition)

        end_point = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + api_key + "&units=metric"

        response = requests.get(end_point).json()
        #print(response)

        dt_txt = response["list"][6]["dt_txt"]
        weather_desc = response["list"][6]['weather'][0]['main']
        weather_desc_2 = response["list"][6]['weather'][0]['description']
        wind_speed = response["list"][6]['wind']['speed']
        humidity = response["list"][6]['main']['humidity']
        temperature = response["list"][6]['main']['temp']

        if date == "tomorrow":
            if condition == "temperature":
                message = "Tomorrow temperature will be " + str(temperature) + " of Celcius at " + city
            elif condition == "humid" or condition == "humidity":
                message = "Tomorrow Humidity will be " + str(humidity) + "% at " + city
            elif condition == "rainy" or condition == "rain":
                if weather_desc == "Rain":
                    message = "Tomorrow will be rainy weather at " + city
            elif condition == "cold" or condition == "hot":
                if temperature >= 10.0 and temperature < 18.0:
                    message = "Tomorrow will be cold weather at " + city
                elif temperature >= 0.0 and temperature < 10.0:
                    message = "Tomorrow will be moderate cold weather at " + city
                elif temperature < 0.0:
                    message = "Tomorrow will be very cold weather at " + city
                elif temperature >= 18.0 and temperature < 28.0:
                    message = "Tomorrow will be mild weather at " + city
                elif temperature >= 28.0 and temperature < 35.0:
                    message = "Tomorrow will be hot weather at " + city
                else:
                    message = "Tomorrow Humidity will be very hot weather outside at " + city
            elif condition == "windy":
                message = "The wind speed will be " +str(wind_speed) + "m/s at tomorrow at " + city

        elif date == "today":
            message = "triggered forecast 4"

        dispatcher.utter_message(text = message)

        return []
    
class ActionUpgradePackage(Action):

    def name(self) -> Text:
        return "action_package_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        trackers = tracker.latest_message['entities']
        print(trackers)

        name = tracker.get_slot("name")
        phone_no = tracker.get_slot("phone_no")
        email = tracker.get_slot("email")
        package = tracker.get_slot("package")

        message = "Here are the details you provided:\n\nName: "+name+"\nPhone No: "+phone_no+"\nEmail: "+email+"\nPackage: "+ package

        dispatcher.utter_message(text = message)

        return []