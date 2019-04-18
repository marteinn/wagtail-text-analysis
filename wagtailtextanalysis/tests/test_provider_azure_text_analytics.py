from unittest import mock

from django.test import TestCase, override_settings

from wagtailtextanalysis.providers import azure_text_analytics


class ProviderAzureTextAnalyticsTest(TestCase):
    def test_loading_failes_if_missing_props(self):
        with self.assertRaises(AttributeError):
            azure_text_analytics.get_key_phrases("My text", "mytext")

    @override_settings(
        AZURE_TEXT_ANALYTICS_API_KEY="random-key",
        AZURE_TEXT_ANALYTICS_REGION="northeurope",
    )
    @mock.patch(
        "wagtailtextanalysis.providers.azure_text_analytics.get_key_phrases_impl",
    )
    def test_key_phrases_gets_retrived(self, test_patch):
        test_patch.return_value = {
            "documents": [{"keyPhrases": ["cats", "dogs"]}]
        }

        phrases = azure_text_analytics.get_key_phrases(
            "A text about cats and dogs", "cats-dogs"
        )

        self.assertEquals(phrases, ["cats", "dogs"])
