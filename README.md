[![Build Status](https://travis-ci.org/marteinn/wagtail-text-analysis.svg?branch=develop)](https://travis-ci.org/marteinn/wagtail-text-analysis)

# Wagtail Text Analysis

Detect key phrases from your Wagtail content using powerful ML Apis.


## Features

- Key phrase generation using Azure Text Analytics


## Supported providers

- [Azure Text Analytics](#azure-text-analytics)


## Requirements

- Python 3.6+
- Wagtail 2+
- Access to any of the [supported providers](#providers)


## Providers

### Azure Text Analytics

Azure's Text Analytics Api. [Docs](https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/)


#### Settings

- `AZURE_TEXT_ANALYTICS_API_KEY`: Azure Computer Vision API key
- `AZURE_TEXT_ANALYTICS_REGION`: The default region to use, e.g. westus, northeurope, etc


## Where to go from here?

We recommend you to check out our [Getting Started Guide](https://github.com/marteinn/wagtail-text-analysis/blob/develop/docs/getting-started.md).


## Contributing

Want to contribute? Awesome. Just send a pull request.


## License

Wagtail Text Analysis is released under the [MIT License](http://www.opensource.org/licenses/MIT).
