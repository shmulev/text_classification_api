# -- Load library --
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask.ext.cors import CORS, cross_origin
import log

# -- Logger --
logger = log.setup_custom_logger('root')
logger.info('Starting Server')

# -- Init Configuration --
app = Flask(__name__, static_url_path='')
app.config.from_object('configuration.ProductionConfig')
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# -- Database --
# db = SQLAlchemy(app)
# logger.info('Database created')

# -- Trigger Server --
import server
