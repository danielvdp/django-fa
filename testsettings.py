import django.conf.global_settings as DEFAULT_SETTINGS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'ishalltellyouonlyonce'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fa',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    },
]

# Django >= 1.7 complains if this is not set
MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES

FONT_AWESOME = {
    'tag': 'span',
}