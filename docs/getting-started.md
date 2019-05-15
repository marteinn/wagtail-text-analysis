# Getting started guide

This is a guide to help you to implement `key phrases` using the Text Analytics Api.


## Requirements

- A working Wagtail site


## Setup a Azure account, add Cognitive Services and fetch a api key

- Go to [Microsoft Azure Text Analytics](https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/) and klick on "Try Text Analytics", or login if you have an existing account.
- Open [your portal](https://portal.azure.com)
- Click on `All resources`
- Add a new resource with Cognitive Services as a service

    - Name: A name for your resource group (such as `testing-wagtail-text-analytics`
    - Subscription: Choose free trial if you only want to try out
    - Location: Choose a location that is closest to you or your users
    - Pricing tier: Choose `F0` for trial
    - Resource group: It can be the same as your `name` For more details go to the [docs](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview#resource-groups)

- After your resource has been created, retrieve your keys


## Installing wagtail-text-analysis

- Its a regular pypi package so just run `pip install wagtailtextanalysis`
- Add it to installed apps in your django settings

    ```python
    INSTALLED_APPS = [
        ...
        "wagtail-text-analysis"
        ...
    ]
    ```

- Add the following configuration to your Wagtail setting
    ```
    AZURE_TEXT_ANALYTICS_API_KEY = "Your key"
    AZURE_TEXT_ANALYTICS_REGION = "Your region"
    ```


## Connect your Wagtail page with wagtail-text-analysis and let it autogenerate key phrases

- Import `wagtailtextanalysis.text_analysis.TextAnalysis` and extend your page with it

    ```python
    class HomePage(Page, TextAnalysis):
        ...
    ```

- Next step is to instruct which fields you want to extract key phrases from, you do this by adding the member `text_analysis_fields` to your model that contains the fields you want to include. (It works pretty much the same was as searching in Wagtail)

    ```python
    from wagtailtextanalysis.text_analysis import TextAnalysis, KeyPhrasesField


    class HomePage(Page, TextAnalysis):
        ...

        text_analysis_fields = [
            KeyPhrasesField('title'),
            KeyPhrasesField('wysiwyg'),
        ]
    ```

- Now finally we add a method that retrives the key phrases

    ```python
    class HomePage(Page, TextAnalysis):
        ...

        def update_key_phrases(self, phrases):
            print(phrases)  # Example: ["dog", "forest", "sunny stockholm"]
    ```

- From here you can either choose to save the fields to your model or pass them on to elasticsearch, here we use a field called tags to store the values

    ```python
    from django.contrib.postgres.fields import ArrayField
    from django.db import models

    class HomePage(Page, TextAnalysis):
        ...
        tags = ArrayField(models.CharField(max_length=200), blank=True)

        def update_key_phrases(self, phrases):
            self.tags = phrases
            self.save()
    ```

- Full example

    ```python
    from wagtail.core.models import Page
    from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
    from wagtailtextanalysis.text_analysis import (
        TextAnalysis,
        KeyPhrasesField,
    )

    class HomePage(Page, TextAnalysis):
        wysiwyg = RichTextField(blank=True, null=True, verbose_name=_("Wysiwyg"))

        content_panels = Page.content_panels + [
            RichTextFieldPanel("wysiwyg"),
        ]

        text_analysis_fields = [
            KeyPhrasesField('title'),
            KeyPhrasesField('wysiwyg'),
        ]

        def update_key_phrases(self, phrases):
            self.tags = phrases
            self.save()
    ```


## Troubleshooting

If you have any problem getting the library up and running, please let me know by filing an issue and we will help you out.
