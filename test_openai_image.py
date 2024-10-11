import os
import openai
import random

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_random_prompt():
    subjects = ["a cat", "a robot", "a wizard", "a spaceship", "a dragon"]
    actions = ["riding", "fighting", "dancing with", "cooking", "exploring"]
    settings = ["on the moon", "in a futuristic city", "underwater", "in a magical forest", "on a floating island"]
    
    prompt = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(settings)}"
    return prompt

def generate_image():
    try:
        prompt = generate_random_prompt()
        print(f"Generated prompt: {prompt}")
        
        response = openai.images.generate(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        image_url = response.data[0].url
        print(f"Generated image URL: {image_url}")
        return image_url, prompt
    except Exception as e:
        print(f"Error generating image: {e}")
        return None, None

if __name__ == "__main__":
    image_url, prompt = generate_image()
    if image_url:
        print("Image generation successful!")
        print(f"Prompt: {prompt}")
        print(f"Image URL: {image_url}")
    else:
        print("Image generation failed.")
