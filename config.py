class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'