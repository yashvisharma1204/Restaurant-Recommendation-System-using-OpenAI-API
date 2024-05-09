# basic code
from openai import OpenAI
import pandas as pd
import langchain 
import json
mykey = "your_api_key" #Your api key
client = OpenAI(api_key=mykey)
try:
    with open("Food Data.txt", "r", encoding="utf-8") as file:
        raw_data = file.readlines()

except UnicodeDecodeError:
    # If 'utf-8' fails, fallback to 'latin-1'
    with open("Food Data.txt", "r", encoding="latin-1") as file:
        raw_data = file.readlines()
food_extraction_function = [
    {
        "name": "extract_food_info",
        "description": "Extract name, favorite food, favorite restaurant, city, and monthly spending from text",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name of the student"},
                "favorite_food": {"type": "string", "description": "Favorite food"},
                "favorite_restaurant": {"type": "string", "description": "Favorite restaurant"},
                "city": {"type": "string", "description": "City of the student"},
                "monthly_spending": {"type": "integer", "description": "Monthly spending on eating out"},
            },
            "required": ["name", "favorite_food", "favorite_restaurant", "city", "monthly_spending"],
        },
    }
]
extracted_data = []
for line in raw_data:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": line}],
        functions=food_extraction_function,
        function_call={"name": "extract_food_info"},
    )

    response_data = json.loads(response.choices[0].message.function_call.arguments)
    extracted_data.append(response_data)
df = pd.DataFrame(extracted_data)
df
extracted_data = []
for line in raw_data:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": line}],
        functions=food_extraction_function,
        function_call={"name": "extract_food_info"},
    )

    response_data = json.loads(response.choices[0].message.function_call.arguments)
    extracted_data.append(response_data)
df = pd.DataFrame(extracted_data)
print(df)
def generate_suggestions(row):
    # Extract the favorite food and restaurant from the DataFrame row
    favorite_food = row["favorite_food"]
    favorite_restaurant = row["favorite_restaurant"]
    city = row["city"]
    
    # Create the prompt for OpenAI's GPT-3.5-turbo
    prompt = f"Suggest just a name of restaurant or place along with the city to eat based on the favorite food: {favorite_food},favorite restaurant: {favorite_restaurant} and city:{city}."
    
    # Generate the suggestion using OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10,
    )
    
    # Return the suggestion from OpenAI
    return response.choices[0].message.content.strip()
df["Suggestion"] = df.apply(generate_suggestions, axis=1)
print(df)
