import ez_setup # From http://peak.telecommunity.com/DevCenter/setuptools
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "Django",
    version = "0.90",
    url = 'http://www.djangoproject.com/',
    author = 'Lawrence Journal-World',
    author_email = 'holovaty@gmail.com',
    description = 'A high-level Python Web framework that encourages rapid development and clean, pragmatic design.',
    license = 'BSD',
    packages = find_packages(),
    package_data = {
        '': ['*.TXT'],
        'django.conf': ['locale/bn/LC_MESSAGES/*',
                        'locale/cs/LC_MESSAGES/*',
                        'locale/cy/LC_MESSAGES/*',
                        'locale/da/LC_MESSAGES/*',
                        'locale/de/LC_MESSAGES/*',
                        'locale/en/LC_MESSAGES/*',
                        'locale/es/LC_MESSAGES/*',
                        'locale/fr/LC_MESSAGES/*',
                        'locale/gl/LC_MESSAGES/*',
                        'locale/is/LC_MESSAGES/*',
                        'locale/it/LC_MESSAGES/*',
                        'locale/no/LC_MESSAGES/*',
                        'locale/pt_BR/LC_MESSAGES/*',
                        'locale/ro/LC_MESSAGES/*',
                        'locale/ru/LC_MESSAGES/*',
                        'locale/sk/LC_MESSAGES/*',
                        'locale/sr/LC_MESSAGES/*',
                        'locale/sv/LC_MESSAGES/*',
                        'locale/zh_CN/LC_MESSAGES/*'],
        'django.contrib.admin': ['templates/admin/*.html', 'templates/admin_doc/*.html',
                        'templates/registration/*.html',
                        'media/css/*.css', 'media/img/admin/*.gif',
                        'media/img/admin/*.png', 'media/js/*.js',
                        'media/js/admin/*js'],
    },
    scripts = ['django/bin/django-admin.py'],
    zip_safe = False,
)
