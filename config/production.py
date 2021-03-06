from logging.config import dictConfig
from config.default import *

# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
  user='postgres',
  pw='0000',
  url='192.168.0.250',
  db='flask_pybo'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b"R\xde\x8a\x86\xf4\xd4q\x15`_\xd9U'\x94\xd9\x8a"

dictConfig({
  'version': 1,
  'formatters': {
    'default': {
      'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }
  },
  'handlers': {
    'file': {
      'level': 'INFO',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
      'maxBytes': 1024 * 1024 * 5,    # 5MB
      'backupCount': 5,
      'formatter': 'default',
    },
  },
  'root': {
    'level': 'INFO',
    'handlers': ['file']
  }
})