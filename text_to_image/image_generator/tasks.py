# image_generator/tasks.py
from celery import shared_task
import requests
from .models import GeneratedImage
import logging
import json
import base64
from PIL import Image
from io import BytesIO
import os

STABILITY_API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
STABILITY_API_KEY = "sk-AsI9wWV76rqWZkSfvjhtupKiexTOJNrGIV5V6hIVYJOyClGh"
IMAGE_SAVE_PATH = "text_to_image/image_generator/Images"

logger = logging.getLogger(__name__)

@shared_task
def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "text_prompts": [{"text": prompt}],
        "samples": 1,
        "width": 1024,
        "height": 1024
    }

    try:
        response = requests.post(STABILITY_API_URL, json=data, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        
        logger.info(f"Response Data: {response_data}")
        return response_data
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None
