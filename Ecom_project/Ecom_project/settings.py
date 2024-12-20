"""
Django settings for Ecom_project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k1qpm$5m7ypxa!w$2rzmg*k=xol%*_$9i-dng+mvv$^&8k5^i_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'social_django',
    
    
]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'Ecom_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                 
            ],
        },
    },
]

WSGI_APPLICATION = 'Ecom_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
       'default': {
<<<<<<< HEAD
           'ENGINE': 'You database engine',
           'NAME': 'Your database name',
           'USER': 'Your database user',
           'PASSWORD': 'Your database password',
           'HOST': 'Your database host',
           'PORT': 'Your database port',
=======
           'ENGINE': 'Specify the backend',
           'NAME': 'Your database name',
           'USER': 'Your database username',
           'PASSWORD': 'Your database password',
           'HOST': 'Set to empty string for localhost',
           'PORT': 'Default PostgreSQL port',
>>>>>>> ca18e9e1cc13694fabadaceda20db127ac7c267d
       }
   }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

# Directory where Django will collect static files during deployment
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Or another directory of your choice

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Google authentication
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
# Google OAuth2 configuration
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'  
LOGIN_REDIRECT_URL = '/'  
LOGOUT_REDIRECT_URL = '/'  

# Google OAuth2 client ID and secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-oauth2-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-oauth2-client-secret'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'REDIRECT_URI': 'http://localhost:8000/social-auth/complete/google-oauth2/',  # Make sure this matches exactly
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Reset password throug email - console

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Razorpay payment KEY ID AND KEY SECRET
RAZORPAY_KEY_ID = 'Your Key Id'
RAZORPAY_KEY_SECRET = 'Your Key Secret'

# Jazzmin admin settings
JAZZMIN_SETTINGS = {
    "site_title": "Admin",
    "copyright": "PawsomePicksome",
    "site_brand": "PawsomePicksome",
    "site_logo": "/app/images/banner/PawsomePicks.png",
    "welcome_sign": "Welcome to the PAWSOMEPICKSOME  Admin Panel",
     "search_model": ["auth.User"],
     "custom_css": "app/css/custom_admin.css",
     "show_ui_builder": False,
     
     # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "app"},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-warning",
    "accent": "accent-orange",
    "navbar": "navbar-warning navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}


