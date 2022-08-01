#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    if os.environ.get('DJANGO_DEVELOPMENT'):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
