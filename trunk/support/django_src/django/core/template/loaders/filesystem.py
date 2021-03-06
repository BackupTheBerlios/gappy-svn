# Wrapper for loading templates from the filesystem.

from django.conf.settings import TEMPLATE_DIRS, TEMPLATE_FILE_EXTENSION
from django.core.template import TemplateDoesNotExist
import os

def load_template_source(template_name, template_dirs=None):
    if not template_dirs:
        template_dirs = TEMPLATE_DIRS
    tried = []
    for template_dir in template_dirs:
        filepath = os.path.join(template_dir, template_name) + TEMPLATE_FILE_EXTENSION
        try:
            return open(filepath).read()
        except IOError:
            tried.append(filepath)
    if template_dirs:
        error_msg = "Tried %s" % tried
    else:
        error_msg = "Your TEMPLATE_DIRS setting is empty. Change it to point to at least one template directory."
    raise TemplateDoesNotExist, error_msg
load_template_source.is_usable = True
