"""
Django settings for Gonghangguize project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
## 旧的目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

###修改后的目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#print("pppppppppppppppppppppppppppppppppppppppppppppppppppppppppp")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qcb%nds7i63n-=e3%@4+939m89m@_912xaj6f03%fv^ll#j!^w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ghrule',
     'akamx',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Gonghangguize.urls'

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

WSGI_APPLICATION = 'Gonghangguize.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'riskcontrol_acard',
        'USER':'riskcontrol_app',
        'PASSWORD':'htEu3erj#',
        'HOST':"rm-2zen1r8lhtu0f6cv4.mysql.rds.aliyuncs.com",
        'PORT':3306,
        'init_command': 'SET default_storage_engine=MyISAM',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE =  'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# import datetime
# today = datetime.datetime.today()
# aa = today.strftime("%Y-%m-%d")

#filename =aa+'.log'
#print('BASE_DIRBASE_DIRBASE_DIR',BASE_DIR)

# 日志日志
# 日志日志
filename ='riwsehngchang'
LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOGGING = {
    'version': 1,
    # 日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s: %(thread)d]'
                      '%(pathname)s:%(funcName)s:%(lineno)d %(levelname)s - %(message)s',
            'datefmt': '%d/%b/%Y %H:%M'
            # 'datefmt': '%d/%b/%Y %H'
        }
    },

    'filters': {
        'test': {
            '()': 'ops.TestFilter'
        }
    },

    'handlers':{
        'console_handler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file_handler': {
            'level': 'INFO',
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, filename),
            'when': 'H',
            'interval':1,
            # 'maxBytes': 1024*1024*1024,
            # 'backupCount': 5,
            'formatter': 'standard',
            # 'formatter': 'verbose',
            'encoding': 'utf-8',
            #'suffix' :  '%Y%m%d-%H%M.log'
        },


    },

    'loggers': {
        'django': {
            'handlers': ['console_handler', 'file_handler'],
            'filters': ['test'],
            'level': 'DEBUG',
             'file_handler.suffix':'%Y%m%d-%H%M'

        }
    }
}



##调用方法
## pboc调用的方法
hsa_method ="credit.credit_single_query"
hsa_version= "v1.0.0"




###正式账号

hsa_account_code_zs= "hshc_ywfk",
hsa_account_key_zs="d364129b4fdb134c2c78919fe4290978",



url_zs = 'http://credit.huashenghaoche.com:80/hshccredit/gateway/request'


