"""
Django settings for lcr project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from django.conf.urls import include, url
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE_DIR = os.path.join(BASE_DIR, "datafiles")
# Directoy used to store cts vts result files
FILES_DIR = os.path.join(DATA_FILE_DIR, "files/cts-vts")


######################################################################
############ DEFAULT SETTINGS ########################################
######################################################################

db_name = "" ## TO BE UPDATED
db_username = "" ## TO BE UPDATED
db_passwd = "" ## TO BE UPDATED
bind_user = "" ## TO BE UPDATED
bind_passwd = "" ## TO BE UPDATED
jenkins_user = None ## TO BE UPDATED
jenkins_token = "" ## TO BE UPDATED
qareport_token = "" ## TO BE UPDATED
lava_production_user = "" ## TO BE UPDATED
lava_production_token = "" ## TO BE UPDATED
lava_lkft_user = "" ## TO BE UPDATED
lava_lkft_token = "" ## TO BE UPDATED
lava_staging_user = "" ## TO BE UPDATED
lava_stagin_token = "" ## TO BE UPDATED
irc_channel = "#linaro-lkft-report" ## TO BE UPDATED
irc_botnick = "android-bot" ## TO BE UPDATED
irc_botpass = "" ## TO BE UPDATED

BUGZILLA_API_KEY = '' ## TO BE UPDATED

# old file might be removed from archive.validation.linaro.org already
# so only list numbers for the recent 20 builds
BUILD_WITH_JOBS_NUMBER = 10

# indicate if the instance is deployed with apache or run as single django instance
DEPLOYED_WITH_APACHE = False

DB_USE_POSTGRES = False
######################################################################
############VALUE TO OVERRIDE THE DEFAULT SETTINGS     ###############
######################################################################

######################################################################
############BETTER TO NOT UPDATE THE FOLLOWING SETTINGS###############
######################################################################
IRC_CONFIG = {
    'enable': False,
    'configs': {
        'server': "chat.freenode.net", # Provide a valid server IP/Hostname
        #port = 6697
        'port': 6667,
        'channel': irc_channel,
        'botnick': irc_botnick,
        'botpass': irc_botpass,
    }
}

JENKINS = {
    'default': {
                'domain': 'ci.linaro.org',
                'user': jenkins_user, ## TO BE UPDATED
                'token': jenkins_token, ## TO BE UPDATED
                },
}

QA_REPORT = {
    'production': {
                    'nick': 'production',
                    'domain': 'qa-reports.linaro.org',
                    'token': qareport_token, ## TO BE UPDATED
                    },
    }
LAVA_SERVERS = {
    'lkft': {
                'nick':'lkft',
                'hostname': 'lkft.validation.linaro.org',
                'username': lava_lkft_user, ## TO BE UPDATED
                'token': lava_lkft_token, ## TO BE UPDATED
            },
    'production': {
                'nick': 'production',
                'hostname': 'validation.linaro.org',
                'username': lava_production_user, ## TO BE UPDATED
                'token': lava_production_token, ## TO BE UPDATED
                },
    'staging': {
                'nick': 'staging',
                'hostname': 'staging.validation.linaro.org',
                'username': lava_staging_user, ## TO BE UPDATED
                'token': lava_stagin_token, ## TO BE UPDATED
                },
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if DB_USE_POSTGRES:
    DATABASES = { ## TO BE UPDATED
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '%s' % db_name,
            'USER': '%s' % db_username,
            'PASSWORD': '%s' % db_passwd,
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = { ## TO BE UPDATED
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DATA_FILE_DIR, 'db.sqlite3'),
            'OPTIONS': {
                'timeout': 60,  # in seconds
                # see also
                # https://docs.python.org/3.7/library/sqlite3.html#sqlite3.connect
            },
        }
    }

APPS_TOBE_ADDED = [
    'lkft',
    'lcr',
    'crispy_forms',
]

ENABLE_APP_REPORT = False ## TO BE UPDATED, to uncomment when you want to enabled the report for lcr builds
if ENABLE_APP_REPORT:
    APPS_TOBE_ADDED = APPS_TOBE_ADDED + [ 'report' ]

########################################################################
### PLEASE DO NOT CHANGE ANYTHIN IN THE BELOW ##########################
########################################################################

QA_REPORT_DEFAULT = 'production'
JENKINS_DEFAULT = 'default'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dr663lyqjd_b-a*0ttwcycp5wfm7&$0-#l6odw#^==ewq!s51s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'127.0.0.1',
                 u'android.linaro.org',
                 ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + APPS_TOBE_ADDED

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lcr.urls'

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

WSGI_APPLICATION = 'lcr.wsgi.application'




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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

if DEPLOYED_WITH_APACHE:
    # python  manage.py collectstatic
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(DATA_FILE_DIR, "logfiles/logfile"),
            'maxBytes': 5000000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },

    'loggers': {
        'django': {
            'handlers':['console', 'logfile'],
            'propagate': True,
            'level':'WARN',
        },
        'django.request': {
            #'handlers': ['mail_admins'],
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            'propagate': False,
        },

        #'django.db.backends': {
        #    'handlers': ['console'],
        #    'level': 'DEBUG',
        #    'propagate': False,
        #},
        'report': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            #'level': 'DEBUG',
        },
        'lkft': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            #'level': 'DEBUG',
        },
        'lcr': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            #'level': 'DEBUG',
        },
    }
}

#DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000

CRISPY_TEMPLATE_PACK = 'bootstrap3'

#######################################################################
#######################################################################
## Setting to use linaro login
INSTALLED_APPS.append('ldap')
INSTALLED_APPS.append('django_auth_ldap')
import ldap
from django_auth_ldap.config import (LDAPSearch, LDAPSearchUnion)

AUTHENTICATION_BACKENDS = ['django_auth_ldap.backend.LDAPBackend',
                           'django.contrib.auth.backends.ModelBackend']

AUTH_LDAP_SERVER_URI = "ldap://login.linaro.org"
AUTH_LDAP_BIND_DN = "uid=%s,ou=staff,ou=accounts,dc=linaro,dc=org" % (bind_user)
AUTH_LDAP_BIND_PASSWORD = "%s" % ( bind_passwd )
# AUTH_LDAP_USER_SEARCH and AUTH_LDAP_USER_DN_TEMPLATE are mutually
#AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=staff,ou=accounts,dc=linaro,dc=org"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=staff,ou=accounts,dc=linaro,dc=org",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_USER_ATTR_MAP = {
  "first_name": "givenName",
  "email": "mail"
}
