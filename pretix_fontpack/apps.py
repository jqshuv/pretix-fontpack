from django.apps import AppConfig
from . import __version__


class PluginApp(AppConfig):
    name = 'pretix_fontpack'
    verbose_name = 'Fontpack'

    class PretixPluginMeta:
        name = 'Fontpack'
        author = 'Joshua Schmitt'
        description = 'Pack of free fonts for pretix\' ticket editor'
        visible = False
        version = __version__
        compatibility = "pretix>=4.16.0"

    def ready(self):
        from . import signals  # NOQA

