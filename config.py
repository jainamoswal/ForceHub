import os
# define all env vars in config class.
class var:
    API_HASH =os.environ.get('API_HASH')
    APP_ID = os.environ.get('APP_ID')
    BOT_TOKEN =os.environ.get('BOT_TOKEN')
    APP_DOMAIN = os.environ.get('APP_DOMAIN')
    GITHUB_USERNAME =  os.environ.get('GITHUB_USERNAME')
    MONGO_URL =  os.environ.get('MONGO_URL')
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    GITHUB_OAUTH_CLIENT_ID = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
    GITHUB_OAUTH_CLIENT_SECRET = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")
    PORT = os.environ.get('PORT', 6969)
