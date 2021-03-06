from django.conf.urls.defaults import *
from django.conf.settings import INSTALLED_APPS

urlpatterns = (
    ('^$', 'django.contrib.admin.views.main.index'),
    ('^logout/$', 'django.views.auth.login.logout'),
    ('^password_change/$', 'django.views.registration.passwords.password_change'),
    ('^password_change/done/$', 'django.views.registration.passwords.password_change_done'),
    ('^template_validator/$', 'django.contrib.admin.views.template.template_validator'),

    # Documentation
    ('^doc/$', 'django.contrib.admin.views.doc.doc_index'),
    ('^doc/bookmarklets/$', 'django.contrib.admin.views.doc.bookmarklets'),
    ('^doc/tags/$', 'django.contrib.admin.views.doc.template_tag_index'),
    ('^doc/filters/$', 'django.contrib.admin.views.doc.template_filter_index'),
    ('^doc/views/$', 'django.contrib.admin.views.doc.view_index'),
    ('^doc/views/jump/$', 'django.contrib.admin.views.doc.jump_to_view'),
    ('^doc/views/(?P<view>[^/]+)/$', 'django.contrib.admin.views.doc.view_detail'),
    ('^doc/models/$', 'django.contrib.admin.views.doc.model_index'),
    ('^doc/models/(?P<model>[^/]+)/$', 'django.contrib.admin.views.doc.model_detail'),
#    ('^doc/templates/$', 'django.views.admin.doc.template_index'),
    ('^doc/templates/(?P<template>.*)/$', 'django.contrib.admin.views.doc.template_detail'),
)

if 'ellington.events' in INSTALLED_APPS:
    urlpatterns += (
        ("^events/usersubmittedevents/(?P<object_id>\d+)/$", 'ellington.events.views.admin.user_submitted_event_change_stage'),
        ("^events/usersubmittedevents/(?P<object_id>\d+)/delete/$", 'ellington.events.views.admin.user_submitted_event_delete_stage'),
    )

if 'ellington.news' in INSTALLED_APPS:
    urlpatterns += (
        ("^stories/preview/$", 'ellington.news.views.admin.story_preview'),
        ("^stories/js/inlinecontrols/$", 'ellington.news.views.admin.inlinecontrols_js'),
        ("^stories/js/inlinecontrols/(?P<label>[-\w]+)/$", 'ellington.news.views.admin.inlinecontrols_js_specific'),
    )

if 'ellington.alerts' in INSTALLED_APPS:
    urlpatterns += (
        ("^alerts/send/$", 'ellington.alerts.views.admin.send_alert_form'),
        ("^alerts/send/do/$", 'ellington.alerts.views.admin.send_alert_action'),
    )

if 'ellington.media' in INSTALLED_APPS:
    urlpatterns += (
        ('^media/photos/caption/(?P<photo_id>\d+)/$', 'ellington.media.views.admin.get_exif_caption'),
    )

urlpatterns += (
    # Metasystem admin pages
    ('^(?P<app_label>[^/]+)/(?P<module_name>[^/]+)/$', 'django.contrib.admin.views.main.change_list'),
    ('^(?P<app_label>[^/]+)/(?P<module_name>[^/]+)/add/$', 'django.contrib.admin.views.main.add_stage'),
    ('^(?P<app_label>[^/]+)/(?P<module_name>[^/]+)/(?P<object_id>.+)/history/$', 'django.contrib.admin.views.main.history'),
    ('^(?P<app_label>[^/]+)/(?P<module_name>[^/]+)/(?P<object_id>.+)/delete/$', 'django.contrib.admin.views.main.delete_stage'),
    ('^(?P<app_label>[^/]+)/(?P<module_name>[^/]+)/(?P<object_id>.+)/$', 'django.contrib.admin.views.main.change_stage'),
)
urlpatterns = patterns('', *urlpatterns)
