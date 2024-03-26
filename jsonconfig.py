import json
import os

# Retrieve the API_KEY from the environment
api_key = os.environ.get("GEMINI_API_KEY")

# Create a dictionary to be converted into JSON
data = {
    "api_key": api_key,
    # Other data...
}

# Convert the dictionary to a JSON string and write it to a file
with open("config.json", "w") as json_file:
    json.dump(data, json_file)