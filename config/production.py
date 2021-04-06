from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b"R\xde\x8a\x86\xf4\xd4q\x15`_\xd9U'\x94\xd9\x8a"