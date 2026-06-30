class Config:
    SECRET_KEY = "your-secret-key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/performance_management"

    SQLALCHEMY_TRACK_MODIFICATIONS = False