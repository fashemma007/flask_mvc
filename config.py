class Config(object):
   pass
class ProdConfig(Config):
   ENV = "production"
   DEVELOPMENT=False
   DEBUG=False
class DevConfig(Config):
   ENV = "development"
   DEVELOPMENT=True
   DEBUG=True