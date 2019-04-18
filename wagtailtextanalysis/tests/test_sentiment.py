from unittest import mock

from django.test import TestCase, override_settings

from wagtailtextanalysis.tests.demosite.factories import CommentFactory


class SentimentTest(TestCase):
    @override_settings(
        AZURE_TEXT_ANALYTICS_API_KEY="random-key",
        AZURE_TEXT_ANALYTICS_REGION="northeurope",
    )
    @mock.patch(
        "wagtailtextanalysis.providers.azure_text_analytics.get_sentiment",
    )
    def test_page_retrives_phrases(self, test_patch):
        test_patch.return_value = 1

        comment = CommentFactory(
            title="Wonderful little place",
            content="Found this place through this fog. Fatastic cherry pie",
        )

        self.assertTrue(comment.sentiment, 1)

        # test_patch.assert_called_once_with("A title about horses and dogs", 1)
