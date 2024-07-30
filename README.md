# TextToGameAI

## Clone the repository:
https://github.com/pshiv24/TextToGameAI.git

## Go to the folder tect_to_image
cd text_to_image

## Make migrations
python manage.py makemigrations
python manage.py migrate


## Run the Application
# Start Redis server:
redis-server

# Start Celery worker:
celery -A text_to_image worker --loglevel=info

# Start the Django server:
python manage.py runserver
