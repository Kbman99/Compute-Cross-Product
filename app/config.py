import logging


class BaseConfig(object):
    SITE_NAME = 'Compute Cross Product'

    SECRET_KEY = 'houdini'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_BINDS = {
    #     # These binds allow you to add in multiple databases
    #     'alias': 'postgresql://postgres:password@localhost:5432/alias'
    # }

    CLIENT_AUTH_TIMEOUT = 9999

    LOG_LEVEL = logging.INFO
    LOG_FILENAME = 'activity.log'


class DevConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    WTF_CSRF_ENABLED = False
