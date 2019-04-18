from django.apps import AppConfig

from wagtailtextanalysis.signal_handlers import register_signal_handlers


class TextAnslysisAppConfig(AppConfig):
    name = "wagtailtextanalysis"
    verbose_name = "Text Analysis"

    def ready(self):
        register_signal_handlers()
