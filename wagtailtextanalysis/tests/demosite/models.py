from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

from wagtailtextanalysis.text_analysis import (
    TextAnalysis,
    KeyPhrasesField,
    SentimentField,
)


class ArticlePage(Page, TextAnalysis):
    wysiwyg = models.TextField(blank=True, null=True, verbose_name=_("Wysiwyg"))
    key_phrases = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("wysiwyg"),
        FieldPanel("key_phrases"),
    ]

    text_analysis_fields = [KeyPhrasesField("title"), KeyPhrasesField("wysiwyg")]

    def update_key_phrases(self, phrases):
        self.key_phrases = " ".join(phrases)


class Comment(models.Model, TextAnalysis):
    title = models.CharField(max_length=255)
    content = models.TextField()
    sentiment = models.DecimalField(max_digits=7, decimal_places=6, default=0)

    text_analysis_fields = [SentimentField("title"), SentimentField("wysiwyg")]

    def update_sentiment(self, sentiment):
        self.sentiment = sentiment
