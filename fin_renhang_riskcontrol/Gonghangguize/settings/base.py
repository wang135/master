"""
Django settings for Gonghangguize project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
#print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

## 旧的目录
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
##修改后的路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qcb%nds7i63n-=e3%@4+939m89m@_912xaj6f03%fv^ll#j!^w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
        'NAME': 'wangzhe',
        'USER': 'root',
        'PASSWORD': '1160329981wang',
        'HOST': '58edd9c77adb6.bj.cdb.myqcloud.com',
        'PORT': 5432,
        'init_command': 'SET default_storage_engine=MyISAM',

    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'riskcontrol_acard',
#         'USER': 'riskcontrol_app',
#         'PASSWORD': 'htEu3erj#',
#         'HOST': "test.mysql.proxysql.rw.huashenghaoche.net",
#         'PORT': 3306,
#         'init_command': 'SET default_storage_engine=MyISAM',
#
#     }
# }


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

# 日志日志
filename ='riw'
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
            'when': 'M',
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


###设置参数
##测试账号
hsa_account_code_cs= "hshc_zhangxl",
hsa_account_key_cs="fff68e025c8743e14bbe398eaaee8ae6",




url_cs = "http://test-credit.huashenghaoche.com/hshccredit/gateway/request"






# ##新增邮箱账号
# username='1160329981@qq.com'
# passwd='idjvjcsuwtyefjca'
# recv=['jingwang28@huashenghaoche.com']
# title='错误提示'
# content='工行规则项目报错'
# file= os.path.join(LOG_DIR, filename)
# ssl=True