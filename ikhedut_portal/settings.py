from mimetypes import init
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

import os

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "1b604c7567ae32d0bf02685eb94bb43e"
)

# DEBUG = os.environ.get("DEBUG", "False") == "True"
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    # "jazzmin",
    'unfold',
    # "suit",
    "rest_framework", 
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'ikhedut',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "adminsortable2",
    'ckeditor',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.locale.LocaleMiddleware', 
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'ikhedut_portal.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "ikhedut_portal" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'ikhedut_portal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'ikhedut_portal_db',
#         'USER': 'root',              
#         'PASSWORD': 'Prince@123',   
#         'HOST': '127.0.0.1',        
#         'PORT': '3306',
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
 
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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGES = [
    ('en', 'English'),
]

LANGUAGE_CODE = 'en'
USE_I18N = True


TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/


STATIC_URL = '/static/'

# Where collectstatic puts files (production)
STATIC_ROOT = BASE_DIR / 'staticfiles'
    
# Where your source static files live (development)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ------------- this is only for django admin panel UI change --------------------

UNFOLD = {
    "SITE_TITLE": "IKhedut Portal Admin Panel",
    "SITE_HEADER": "Ikhedut Portal",
    "SITE_SYMBOL": "Ikhedut Portal",

    "SITE_ICON": {
        "light": lambda request: "/static/img/favicon.png",
        "dark": lambda request: "/static/img/favicon.png",
    },

    "SITE_LOGO": {
        "light": lambda request: "/static/img/header.png",
        "dark": lambda request: "/static/img/header.png",
    },

    "COLORS": {
        "primary": {
            "50": "254 242 242",
            "100": "254 226 226",
            "200": "254 202 202",
            "300": "252 165 165",
            "400": "248 113 113",
            "500": "239 68 68",
            "600": "220 38 38",
            "700": "185 28 28",
            "800": "153 27 27",
            "900": "127 29 29",
        },
    },

    # ✅ ADD THIS (IMPORTANT)
    "STYLES": [
        lambda request: "/static/css/admin_fix.css",
    ],
}
# JAZZMIN_SETTINGS = {
#     "site_title": "Admin Panel",
#     "site_header": "My Project",    
#     "site_brand": "Ikhedut Portal",
#     "welcome_sign": "Welcome to Ikhedut Portal",
#     "show_sidebar": True,
#     "navigation_expanded": False,
#     "copyright": "Ikhedut Portal",
#     "icons": {
#         "auth.user": "fas fa-user",
#         "auth.group": "fas fa-users",
#     },
#     "site_logo": "img/header.png",
#     "site_icon": "img/favicon.png",
#     # for login image
#     "custom_css": "css/admin_custom.css",
# }

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}

SITE_NAME = "Ikhedut Portal"
SITE_DOMAIN = "ikhedut-portal-latest.onrender.com"


CSRF_TRUSTED_ORIGINS = [
    "https://ikhedut-portal-latest.onrender.com",
]

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/userprofile/"
LOGOUT_REDIRECT_URL = "/login/"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_JWT = {  
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "ON_LOGIN_SUCCESS": "rest_framework_simplejwt.serializers.default_on_login_success",
    "ON_LOGIN_FAILED": "rest_framework_simplejwt.serializers.default_on_login_failed",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",

    "CHECK_REVOKE_TOKEN": False,
    "REVOKE_TOKEN_CLAIM": "hash_password",
    "CHECK_USER_IS_ACTIVE": True,
}


LOGIN_URL = "login"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "infoikhedutportal@gmail.com"
EMAIL_HOST_PASSWORD = 'ygdg unzo sxik pely'


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



# import os

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = "apikey"
# EMAIL_HOST_PASSWORD = os.environ.get("SENDGRID_API_KEY")

# DEFAULT_FROM_EMAIL = "infoikhedutportal@gmail.com"
