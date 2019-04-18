from unittest import mock

from django.test import TestCase, override_settings

from wagtailtextanalysis.tests.demosite.factories import ArticlePageFactory


class KeyPhrasesTest(TestCase):
    @override_settings(
        AZURE_TEXT_ANALYTICS_API_KEY="random-key",
        AZURE_TEXT_ANALYTICS_REGION="northeurope",
    )
    @mock.patch(
        "wagtailtextanalysis.providers.azure_text_analytics.get_key_phrases",
    )
    def test_page_retrives_phrases(self, test_patch):
        test_patch.return_value = ["horses", "dogs"]

        page = ArticlePageFactory(title="A title about horses and dogs")
        self.assertTrue(page.key_phrases, "horses, dogs")

        # test_patch.assert_called_once_with("A title about horses and dogs", 1)
