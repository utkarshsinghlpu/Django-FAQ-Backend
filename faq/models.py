from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Translations
    question_hi = models.TextField(_("Question (Hindi)"), blank=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True)

    def __str__(self):
        return self.question

    def get_translated_text(self, field, lang):
        cache_key = f"faq_{self.id}_{field}_{lang}"
        cached_text = cache.get(cache_key)

        if cached_text:
            return cached_text

        if lang == 'en':
            text = getattr(self, field)
        elif hasattr(self, f"{field}_{lang}"):
            text = getattr(self, f"{field}_{lang}")
        else:
            # Fallback to English
            text = getattr(self, field)

        if not text:
            # Translate if the field is empty
            translator = Translator()
            original_text = getattr(self, field)
            translation = translator.translate(original_text, dest=lang)
            text = translation.text

            # Save the translation
            setattr(self, f"{field}_{lang}", text)
            self.save(update_fields=[f"{field}_{lang}"])

        # Cache the result
        cache.set(cache_key, text, timeout=3600)  # Cache for 1 hour

        return text

    def get_question(self, lang='en'):
        return self.get_translated_text('question', lang)

    def get_answer(self, lang='en'):
        return self.get_translated_text('answer', lang)

