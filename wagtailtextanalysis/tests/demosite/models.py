from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel

from wagtailtextanalysis.text_analysis import (
    TextAnalysis,
    KeyPhrasesField,
)


class ArticlePage(Page, TextAnalysis):
    wysiwyg = models.TextField(blank=True, null=True, verbose_name=_("Wysiwyg"))
    key_phrases = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("wysiwyg"),
        FieldPanel('key_phrases'),
    ]

    text_analysis_fields = [
        KeyPhrasesField('title'),
        KeyPhrasesField('wysiwyg'),
    ]

    def update_key_phrases(self, phrases):
        self.key_phrases = " ".join(phrases)
