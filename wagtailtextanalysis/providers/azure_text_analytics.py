from django.conf import settings
from django.utils.translation import get_language
import requests


def get_sentiment(text, identifier):
    lang_and_country_code = get_language()
    lang_code = lang_and_country_code.split("-")[0]

    json_data = {
        "documents": [
            {"id": identifier, "language": lang_code, "text": text}
        ]
    }

    json_response = get_sentiment_impl(json_data)
    documents = json_response["documents"]

    if len(documents) == 0:
        return 0

    return documents[0]["score"]


def get_sentiment_impl(json_data):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': settings.AZURE_TEXT_ANALYTICS_API_KEY,
    }


    domain = get_api_domain(settings.AZURE_TEXT_ANALYTICS_REGION)
    url = "{}/text/analytics/v2.0/sentiment".format(domain)

    response = requests.post(
        url,
        headers=headers,
        json=json_data,
    )

    response.raise_for_status()
    return response.json()


def get_key_phrases(text, identifier):
    lang_and_country_code = get_language()
    lang_code = lang_and_country_code.split("-")[0]

    json_data = {
        "documents": [
            {"id": identifier, "language": lang_code, "text": text}
        ]
    }

    json_response = get_key_phrases_impl(json_data)
    documents = json_response["documents"]

    if len(documents) == 0:
        return []

    return documents[0]["keyPhrases"]


def get_key_phrases_impl(json_data):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': settings.AZURE_TEXT_ANALYTICS_API_KEY,
    }

    domain = get_api_domain(settings.AZURE_TEXT_ANALYTICS_REGION)
    response = requests.post(
        f'{domain}/text/analytics/v2.0/keyPhrases',
        headers=headers,
        json=json_data,
    )

    response.raise_for_status()
    return response.json()


def get_api_domain(region):
    return f'https://{region}.api.cognitive.microsoft.com'
