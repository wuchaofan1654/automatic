"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 1.11.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import datetime

from application.env import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e_oys7mc+)18%qyx93jx+$byuf%#24%5ftnaql8n7nq+tc=p&j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'channels',
    'captcha',
    'frames',
    'apps.permission',
    'apps.system',
    'apps.api',
    'apps.point',
    'apps.duplex',
    'apps.shortcut',
    'apps.testcase',
    'apps.performance',
    'apps.celery',
    'apps.monitor',
    'apps.packageAnalyse'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'frames.middleware.ApiLoggingMiddleware',  # 用于记录API访问日志
    'frames.middleware.PermissionModeMiddleware',  # 权限中间件
    'frames.middleware.EncryptMiddleware'
]

# 允许跨域源
CORS_ORIGIN_ALLOW_ALL = CORS_ORIGIN_ALLOW_ALL
# 允许ajax请求携带cookie
CORS_ALLOW_CREDENTIALS = CORS_ALLOW_CREDENTIALS
X_FRAME_OPTIONS = "ALLOW-FROM"

ROOT_URLCONF = 'application.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'
ASGI_APPLICATION = 'application.routing.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# ...
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/4'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# channels channel_layers 使用 redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        }
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
"""
静态目录、多媒体配置
"""
# 收集静态文件，必须将 MEDIA_ROOT,STATICFILES_DIRS先注释
# python manage.py collectstatic
# STATIC_ROOT=os.path.join(BASE_DIR,'static')
# # 设置django的静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
if not os.path.exists(os.path.join(BASE_DIR, 'media')):
    os.makedirs(os.path.join(BASE_DIR, 'media'))
# 访问上传文件的url地址前缀
MEDIA_URL = "/media/"
# 项目中存储上传文件的根目录
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

"""
日志配置
"""
# log 配置部分BEGIN #
SERVER_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'server.log')
ERROR_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'error.log')
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

# 格式:[2020-04-22 23:33:01][micoservice.apps.ready():16] [INFO] 这是一条日志:
# 格式:[日期][模块.函数名称():行号] [级别] 信息
STANDARD_LOG_FORMAT = '[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s'
CONSOLE_LOG_FORMAT = '[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': STANDARD_LOG_FORMAT
        },
        'console': {
            'format': CONSOLE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'file': {
            'format': CONSOLE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': SERVER_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,  # 最多备份5个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ERROR_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 3,  # 最多备份3个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        }
    },
    'loggers': {
        # default日志
        '': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        # 数据库相关日志
        'django.db.backends': {
            'handlers': [],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

# channels channel_layers 使用 redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)],
        }
    },
}

# ================================================= #
# ************** 数据库 配置  ************** #
# ================================================= #

if DATABASE_TYPE == "MYSQL":
    # Mysql数据库
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": os.getenv('DATABASE_HOST') or DATABASE_HOST,
            "PORT": DATABASE_PORT,
            "USER": DATABASE_USER,
            "PASSWORD": DATABASE_PASSWORD,
            "NAME": DATABASE_NAME,
        }
    }
else:
    # sqlite3 数据库
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# redis 缓存
REDIS_URL = f'redis://:{REDIS_PASSWORD if REDIS_PASSWORD else ""}@{os.getenv("REDIS_HOST") or REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
# 是否启用redis
if locals().get("REDIS_ENABLE", True):
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },
    }
# ================================================= #
# ******************** JWT配置  ******************** #
# ================================================= #
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60 * 60 * 24),  # JWT有效时间24小时
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',  # JWT的Header认证头以'JWT '开始
    'JWT_AUTH_COOKIE': 'AUTH_JWT',
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_PAYLOAD_HANDLER': 'frames.utils.jwt_util.jwt_payload_handler',
    'JWT_GET_USER_SECRET_KEY': 'frames.utils.jwt_util.jwt_get_user_secret_key',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'frames.utils.jwt_util.jwt_response_payload_handler',
}

# ================================================= #
# ************** REST_FRAMEWORK 配置  ************** #
# ================================================= #
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'frames.utils.authentication.RedisOpAuthJwtAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ),

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'frames.pagination.Pagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'EXCEPTION_HANDLER': 'frames.utils.exceptions.op_exception_handler',
}
# ================================================= #
# ************** 登录方式配置  ************** #
# ================================================= #
AUTHENTICATION_BACKENDS = (
    'frames.utils.backends.CustomBackend',
    'frames.utils.backends.SessionAuthentication',
)
AUTH_USER_MODEL = 'permission.UserProfile'
# username_field
USERNAME_FIELD = 'username'

# ================================================= #
# ************** 登录验证码配置  ************** #
# ================================================= #
CAPTCHA_STATE = CAPTCHA_STATE
# 字母验证码
CAPTCHA_IMAGE_SIZE = (160, 60)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
# 加减乘除验证码
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_FONT_SIZE = 40  # 字体大小
CAPTCHA_FOREGROUND_COLOR = '#0033FF'  # 前景色
CAPTCHA_BACKGROUND_COLOR = '#F5F7F4'  # 背景色
CAPTCHA_NOISE_FUNCTIONS = (
    # 'captcha.helpers.noise_arcs', # 线
    # 'captcha.helpers.noise_dots', # 点
)
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

API_LOG_ENABLE = True
# API_LOG_METHODS = 'ALL' # ['POST', 'DELETE']
# API_LOG_METHODS = ['POST', 'DELETE'] # ['POST', 'DELETE']
BROKER_URL = f'redis://:{REDIS_PASSWORD if REDIS_PASSWORD else ""}@{os.getenv("REDIS_HOST") or REDIS_HOST}:' \
             f'{REDIS_PORT}/{locals().get("CELERY_DB", 2)}'  # Broker使用Redis
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'  # Backend数据库
# ================================================= #
# ************** 其他配置  ************** #
# ================================================= #
# 接口权限
INTERFACE_PERMISSION = locals().get("INTERFACE_PERMISSION", False)
DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_TIMEZONE = 'Asia/Shanghai'  # celery 时区问题

