from django.db.models.signals import post_save, pre_save

from .text_analysis import get_text_analysis_models, analyse


def post_save_signal_handler(instance, **kwargs):
    analyse(instance)


def register_signal_handlers():
    for model in get_text_analysis_models():
        pre_save.connect(post_save_signal_handler, sender=model)
