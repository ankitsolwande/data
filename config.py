class Config:
    SQLALCHEMY_DATABASE_URI="mysql://root:ankit@localhost/kiara"
    SECRET_KEY="abcxyz"
    SQLALCHEMY_TRACK_MODIFICATIONS=True
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MYSQL_ECHO=True
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI="mysql://root:ankit@localhost/kiara_test"
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    DEBUG=True
class ProductionConfig(Config):
    DEBUG=False
    MYSQL_ECHO=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
app_config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}