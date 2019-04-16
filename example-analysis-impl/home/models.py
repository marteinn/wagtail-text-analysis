from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtailtextanalysis.text_analysis import (
    TextAnalysis,
    KeyPhrasesField,
)


class HomePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='tagged_items'
    )


class HomePage(Page, TextAnalysis):
    wysiwyg = RichTextField(blank=True, null=True, verbose_name=_("Wysiwyg"))
    tags = ClusterTaggableManager(through=HomePageTag, blank=True)

    content_panels = Page.content_panels + [
        RichTextFieldPanel("wysiwyg"),
        FieldPanel('tags'),
    ]

    text_analysis_fields = [
        KeyPhrasesField('title'),
        KeyPhrasesField('wysiwyg'),
    ]

    def update_key_phrases(self, phrases):
        page_revision = self.get_latest_revision_as_page()
        page_revision.tags.add(*phrases)

        revision = self.get_latest_revision()
        revision.content_json = page_revision.to_json()
        revision.save()
