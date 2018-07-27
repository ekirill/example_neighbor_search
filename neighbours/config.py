class BaseConfig(object):
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///neighbours.db'


class TestingConfig(BaseConfig):
    """Configuration for tests"""
    DEBUG = True
    TESTING = True
    # :memory: sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
