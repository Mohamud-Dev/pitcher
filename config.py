import os


class Config:

    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vector:12345q@localhost/pitcher'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
   
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}