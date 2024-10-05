# This file is a part of ThreatMatrix https://github.com/khulnasoft/ThreatMatrix
# See the file 'LICENSE' for copying permission.

from django.apps import AppConfig


class PlaybooksManagerConfig(AppConfig):
    name = "api_app.playbooks_manager"

    @staticmethod
    def ready() -> None:
        from . import signals  # noqa
