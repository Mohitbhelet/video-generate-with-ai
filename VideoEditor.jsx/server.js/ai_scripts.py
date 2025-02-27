# ai_scripts.py
import requests
import openai

# ElevenLabs API for Text-to-Speech
def generate_voiceover(script, voice_id, api_key):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "text": script,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        print("Voiceover generated successfully!")
    else:
        print("Error generating voiceover:", response.text)

# OpenAI GPT-4 for Script Suggestions
openai.api_key = "your-api-key"

def suggest_script(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

# Example Usage
if __name__ == "__main__":
    script = suggest_script("Write a script for a marketing video.")
    print("Suggested Script:", script)
    generate_voiceover(script, "voice_id_here", "your-elevenlabs-api-key")