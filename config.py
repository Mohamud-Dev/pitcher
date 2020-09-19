class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vector:2547Viki@localhost/pitcher'



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