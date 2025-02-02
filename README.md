# Django FAQ Project

This project implements a multilingual FAQ system using Django, with support for WYSIWYG editing, caching, and automatic translations.

## Features

- Multilingual FAQs (English, Hindi, Bengali)
- WYSIWYG editor for FAQ answers using CKEditor
- Automatic translation using Google Translate
- Caching with Redis
- RESTful API for FAQ management
- Dockerized deployment with Nginx and Gunicorn

## Prerequisites

- Docker
- Docker Compose

## Installation and Setup

1. Clone the repository:
   git clone [https://github.com/yourusername/django-faq-project.git](https://github.com/yourusername/django-faq-project.git)
   cd django-faq-project
3. Create a `.env` file in the project root and add the following:
   DJANGO_SECRET_KEY=your_very_secret_key_here
   DJANGO_DEBUG=False

4. In a new terminal window, apply migrations:
   docker-compose exec web python manage.py migrate

5. Create a superuser:
   docker-compose exec web python manage.py createsuperuser

6. Collect static files:
   docker-compose exec web python manage.py collectstatic --noinput

## Usage

1. Access the admin panel at `http://localhost/admin/` to add FAQs.

2. Use the API to fetch FAQs:
- Fetch FAQs in English (default)
- Fetch FAQs in Hindi
- Fetch FAQs in Bengali

## API Endpoints

- `GET /api/faqs/`: List all FAQs
- `POST /api/faqs/`: Create a new FAQ
- `GET /api/faqs/{id}/`: Retrieve a specific FAQ
- `PUT /api/faqs/{id}/`: Update a specific FAQ
- `DELETE /api/faqs/{id}/`: Delete a specific FAQ

## Running Tests

To run the tests:
docker-compose exec web pytest

## Development

For development purposes, you can run the Django development server instead of Gunicorn. Update the `docker-compose.yml` file:

```yaml
services:
  web:
    command: python manage.py runserver 0.0.0.0:8000
# Stopping the Application
docker-compose down

