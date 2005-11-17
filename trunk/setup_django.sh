#!/bin/sh

export PATH=`pwd`/support/django_src/django/bin:$PATH
export DJANGO_SETTINGS_MODULE=gappy.settings
export PYTHONPATH=`pwd`:$PYTHONPATH
if [ $HOST != 'zippy.dorm.duke.edu' ]; then
	export PYTHONPATH=`pwd`/support/django_src/django:$PYTHONPATH
fi