from django.db.models.signals import pre_save

from .text_analysis import get_text_analysis_models, analyse


def pre_save_signal_handler(instance, *args, **kwargs):
    analyse(instance)


def register_signal_handlers():
    for model in get_text_analysis_models():
        pre_save.connect(
            pre_save_signal_handler,
            sender=model,
            dispatch_uid="wagtailtextanalysis.pre_save.{}".format(
                model.__module__,
            ),
        )
