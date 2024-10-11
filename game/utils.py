import openai
import os
import logging
import random
from django.conf import settings

# Make sure your OpenAI API key is correctly set up from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_random_prompt():
    subjects = ["a cat", "a robot", "a wizard", "a spaceship", "a dragon"]
    actions = ["riding", "fighting", "dancing with", "cooking", "exploring"]
    settings = ["on the moon", "in a futuristic city", "underwater", "in a magical forest", "on a floating island"]
    
    prompt = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(settings)}"
    return prompt

def generate_image(prompt=None):
    try:
        if not prompt:
            prompt = generate_random_prompt()
        logging.info(f"Generated prompt: {prompt}")
        response = openai.images.generate(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        image_url = response.data[0].url
        return image_url, prompt
    except Exception as e:
        logging.error(f"Error generating image: {e}")
        return None, None

