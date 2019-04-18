from django.apps import apps
from django.utils.html import strip_tags
from wagtail.search import index

from wagtailtextanalysis.providers import azure_text_analytics


class KeyPhrasesField(index.SearchField):
    pass


class TextAnalysis:
    text_analysis_fields = []

    def get_text_to_analyse(self, field_type):
        fields = filter(
            lambda field: isinstance(field, field_type),
            self.text_analysis_fields,
        )
        fields = list(fields)
        if not len(fields):
            return None

        values = [field.get_value(self) for field in fields]
        if not len(values):
            return None

        values = filter(lambda x: x, values)
        text = "\n".join(values)
        return strip_tags(text)

    def update_key_phrases(self, phrases):
        raise NotImplementedError()


def analyse(instance):
    key_phrases_text = instance.get_text_to_analyse(KeyPhrasesField)
    if key_phrases_text:
        phrases = azure_text_analytics.get_key_phrases(
            key_phrases_text,
            identifier=instance.pk,
        )
        instance.update_key_phrases(phrases)


def get_text_analysis_models():
    return [
        model for model in apps.get_models()
        if issubclass(model, TextAnalysis) and not model._meta.abstract
    ]
