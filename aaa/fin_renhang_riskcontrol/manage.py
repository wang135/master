#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #系统配置的
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gonghangguize.settings")
    ##新的
    # 新修改的
    # profile = os.environ.get('TYPEIDEA_PROFILE', )
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gonghangguize.settingss.%s' % profile)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
