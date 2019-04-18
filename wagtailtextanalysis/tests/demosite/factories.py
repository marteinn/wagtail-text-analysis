import wagtail_factories
import factory

from . import models


class ArticlePageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = models.ArticlePage


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Comment
