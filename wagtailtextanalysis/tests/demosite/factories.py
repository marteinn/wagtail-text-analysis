import wagtail_factories
from . import models


class ArticlePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.ArticlePage
