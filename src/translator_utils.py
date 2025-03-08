import os
import json
import requests

# Get the absolute path to the config file
working_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(working_dir, "config.json")

# Load configuration
try:
    with open(config_path, 'r') as f:
        config = json.load(f)
    mistral_config = config.get("mistral", {})
    API_KEY = mistral_config.get("api_key")
    API_URL = mistral_config.get("api_url")
except Exception as e:
    raise RuntimeError("Failed to load config.json") from e


def translate(input_language, output_language, input_text):
    # Language mapping (same as before)
    lang_code = {
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'German': 'de',
        'Latin': 'la',
        'Hindi': 'hi',
        'Bengali': 'bn',
        'Tamil': 'ta',
        'Telugu': 'te'
    }

    input_code = lang_code.get(input_language, 'en')
    output_code = lang_code.get(output_language, 'en')

    # Translation prompt
    prompt = f"Translate the following {input_code} text to {output_code}: {input_text}"

    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-tiny",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 512
            }
        )
        response.raise_for_status()
        translated_text = response.json()["choices"][0]["message"]["content"]
        return translated_text.strip()
    except Exception as e:
        return f"Error: {str(e)}"