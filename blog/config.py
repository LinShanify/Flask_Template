class Config:
    # Setup a Sectet Key
    SECRET_KEY='dadc98d2ce2925035ffc2bdc6ce3c190'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # Email Address
    MAIL_USERNAME = 'your email address'
    # Email Password
    MAIL_PASSWORD = 'your email password'