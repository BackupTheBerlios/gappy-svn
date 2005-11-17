#!/bin/sh

export PATH=`pwd`/support/django_src/django/bin:$PATH
export DJANGO_SETTINGS_MODULE=gappy.settings
export PYTHONPATH=`pwd`:$PYTHONPATH
export PYTHONPATH=`pwd`/support/django_src:$PYTHONPATH
