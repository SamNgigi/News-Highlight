class Config:
    """
    General Configurations parent class
    """
    pass


class ProdConfig(Config):
    """
    Production Configurations child class

    Args:
        Config parent class with the general app configurations
    """
    pass


class DevConfig(Config):
    """
    Development Configurations child class

    Args:
        Config parent class with the general app configurations
    """
    DEBUG = True
