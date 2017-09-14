# -- Configuration base, for all environments --
class Config(object):
    ###############################################################################
    # Configuration Overall
    #
    # :param object:                The application object
    ###############################################################################
    # -- Mongo DB --
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = ""


# -- Production Configuration --
class ProductionConfig(Config):
    ###############################################################################
    # Configuration for Production
    #
    # :param object:                The application object
    ###############################################################################
    DEBUG = False


# -- Development Configuration --
class DevelopmentConfig(Config):
    ###############################################################################
    # Configuration for Development
    #
    # :param object:                The application object
    ###############################################################################
    DEBUG = True
