# pip install llama-index-agent-openai
from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
import json
import random

import requests
import json

def get_weather_for_city_API(city):
    """Get the current weather in a given city"""
    print(f"Calling local get_weather_for_city for {city}")
    
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '15d469b93a5cda754f58c861c795c58e'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
                # Convert temperature from Kelvin to Celsius
        temperature = data['main']['temp']
        
        return json.dumps({"city": city, "temperature": temperature})
    else:
        return json.dumps({"city": city, "error": data.get('message', 'Error fetching weather data')})
    
def get_weather_for_city(city):
    """Get the current weather in a given city"""
    print(f"Calling local get_weather_for_city for {city}")
    return json.dumps({"city": city, "temperature": random.randint(1,50)})

llm = OpenAI(model="gpt-3.5-turbo-1106")
tool = FunctionTool.from_defaults(fn=get_weather_for_city_API)
agent = OpenAIAgent.from_tools([tool], llm=llm, verbose=True)
response = agent.chat(
    "What's the weather like in Miami?"
)

print(response)
