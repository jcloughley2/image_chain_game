from django.utils import timezone
from .models import Image, Description
from .utils import generate_image
import logging

def generate_daily_image():
    today = timezone.now().date()
    latest_image = Image.objects.filter(created_at=today).order_by('-id').first()

    if not latest_image or latest_image.has_been_described:
        last_description = Description.objects.order_by('-id').first()
        prompt = last_description.text if last_description else None
        image_url, generated_prompt = generate_image(prompt)
        if image_url and generated_prompt:
            Image.objects.create(url=image_url, created_at=today, prompt=generated_prompt)
            logging.info(f"Generated new image with prompt: {generated_prompt}")
        else:
            logging.error("Failed to generate new image")
    else:
        logging.info("Using existing undescribed image")