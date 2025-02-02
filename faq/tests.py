from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework."
        )

    def test_faq_creation(self):
        self.assertTrue(isinstance(self.faq, FAQ))
        self.assertEqual(self.faq.__str__(), self.faq.question)

    def test_get_translated_text(self):
        
        self.assertEqual(self.faq.get_question(), "What is Django?")
        
        
        hindi_question = self.faq.get_question('hi')
        self.assertNotEqual(hindi_question, "What is Django?")
        self.assertEqual(self.faq.question_hi, hindi_question)

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework."
        )

    def test_api_list_faqs(self):
        response = self.client.get(reverse('faq-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_api_list_faqs_with_language(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data[0]['question'], "What is Django?")

