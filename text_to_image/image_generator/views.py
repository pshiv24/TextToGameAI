from django.http import JsonResponse
from django.conf import settings
from PIL import Image
import base64
import io
import os
import logging

logger = logging.getLogger(__name__)

def save_image_from_base64(base64_str, image_name):
    try:
        # Decode the base64 string
        image_data = base64.b64decode(base64_str)
        
        # Create a BytesIO object and open it as an image
        image = Image.open(io.BytesIO(image_data))
        
        # Ensure the directory exists
        image_path = os.path.join(settings.MEDIA_ROOT, 'images', image_name)
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        
        # Save the image
        image.save(image_path)
        return image_path
    except Exception as e:
        logger.error(f"Error saving image: {e}")
        return None

def generate_images(request):
    # Replace with actual API request and response handling
    response_data = {
        'artifacts': [
            {'base64': 'your_base64_encoded_string_here'}
        ]
    }

    image_paths = []
    if 'artifacts' in response_data:
        for artifact in response_data['artifacts']:
            base64_str = artifact.get('base64')
            if base64_str:
                image_name = "image.png"  # Adjust naming as needed
                image_path = save_image_from_base64(base64_str, image_name)
                if image_path:
                    image_paths.append(image_path)
    
    return JsonResponse({'image_paths': image_paths})

from django.shortcuts import render

def display_images(request):
    # Replace with actual API request and response handling
    response_data = {
        'artifacts': [
            {'base64': 'your_base64_encoded_string_here'}
        ]
    }

    images = [artifact.get('base64') for artifact in response_data.get('artifacts', [])]
    
    return render(request, 'display_images.html', {'images': images})

