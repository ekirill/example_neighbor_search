import os


class BaseConfig(object):
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///neighbours.db'


class TestingConfig(BaseConfig):
    """Configuration for tests"""
    TESTING = True
    # :memory: sqlite database
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
