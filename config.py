import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY =  os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = '915593787@qq.com'
    MAIL_PASSWORD = 'sxauzx121'
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'Flasky Admin <915593787@qq.com>'
    FLASK_ADMIN = 'zhangxiang@rytx.com'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
