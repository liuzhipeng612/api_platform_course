"""
Django settings for api_platform project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import datetime
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps设为根目录，下面两个二选一
sys.path.append(os.path.join(BASE_DIR, "apps"))
# sys.path.insert(0,os.path.join(BASE_DIR,"apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&q5@i4z6pg)l#9p!yjutkwoguwi&-rd!v&o)bj01=adad%k=#h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 设置允许访问的主机，默认只能使用本地地址访问项目
# ALLOWED_HOSTS = ["外网ip", "localhost", "127.0.0.1"]
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'configures.apps.ConfiguresConfig',
    'debugtalks.apps.DebugtalksConfig',
    'envs.apps.AppConfig',
    'interfaces.apps.InterfacesConfig',
    'projects.apps.ProjectsConfig',
    'reports.apps.ReportsConfig',
    'testcases.apps.TestcasesConfig',
    'testsuits.apps.TestsuitsConfig',
    'users.apps.UsersConfig',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 需要添加在ComonMiddleware中间件之前
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 临时关闭csr安全校验
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ORIGIN_ALLOW_ALL为True, 指定所有域名(ip)都可以访问后端接口, 默认为False
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST指定能够访问后端接口的ip或域名列表
# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:8080",
#     "http://localhost:8080",
#     "http://192.168.1.63:8080",
#     "http://127.0.0.1:9000",
#     "http://localhost:9000",
# ]

# 允许跨域时携带Cookie, 默认为False
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'api_platform.urls'

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

WSGI_APPLICATION = 'api_platform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'api_platform_stg',  # 数据库名
        'USER': 'api_platform_stg',  # 数据库用户名
        'PASSWORD': 'BjbrmnG2Z6Ym6pCG',  # 数据库密码
        'HOST': '111.229.64.99',  # 数据库主机域名或者IP
        'PORT': 3306  # 数据库端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# 设置语言
LANGUAGE_CODE = 'zh-hans'

# 设置时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# 覆盖REST_FRAMEWORK(DRF)默认配置
REST_FRAMEWORK = {
    # 默认响应渲染类
    'DEFAULT_RENDERER_CLASSES': (
        # json渲染类为第一条优先
        'rest_framework.renderers.JSONRenderer',
        # 可浏览的API渲染器为第二优先级
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    # 全局指定过滤引擎类
    'DEFAULT_FILTER_BACKENDS': [
        # 过滤引擎
        'django_filters.rest_framework.backends.DjangoFilterBackend',
        # 排序引擎
        'rest_framework.filters.OrderingFilter'
    ],

    # 全局指定分页引擎类
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS':
    #     'utils.pagination.ManualPageNumberPagination',
    # 'PAGE_SIZE':
    #     3,

    # 指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS':
        'rest_framework.schemas.coreapi.AutoSchema',

    # 指定认证类(指定的是认证的方式)
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 指定使用JWT Token认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # DRF框架默认情况下, 使用的是用户会话认证
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.permissions.AllowAny'
    ],

    # 授权类(指定的是认证成功之后能干嘛!)
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     # DRF框架默认的权限为AllowAny(允许所有用户来访问)
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
}
JWT_AUTH = {
    # 默认token的过期时间是5分钟，可以指定过期时间为1天
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 修改token值的前缀
    # 前端在传递token值时，Authorization作为key，值为：token前缀+空格+token值
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 指定返回前端数据的处理函数
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'utils.jwt_handler.jwt_response_payload_handler',
}
# 配置日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
                '%(asctime)s - [%(levelname)s] - %(name)s - [msg]%(message)s - [%(filename)s:%(lineno)d ]'
        },
        'simple': {
            'format': '%(asctime)s - [%(levelname)s] - [msg]%(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "logs/test.log"),  # 日志文件的位置
            'maxBytes': 100 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose',
            'encoding': 'utf-8'
        },
    },
    'loggers': {
        'test': {  # 定义了一个名为test的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',  # 日志器接收的最低日志级别
        },
    }
}
