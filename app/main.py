from flask import Flask, request

from app import connection_manager, setup_db
from app.api import audiobooks, users
from app.config import oauth2
from app.config.config_objects import Config
# from app.middleware import login_required


def create_app(config: Config=Config()):
	app = Flask( __name__ )
	app.config.from_object(config)
	setup_db(resource_package='app.resources.sql', cm=connection_manager)
	register_blueprints(app)
	register_routes(app)
	return app


def register_blueprints(app):
	app.register_blueprint( audiobooks, url_prefix='/api/audiobooks' )
	app.register_blueprint( users, url_prefix='/api/users')

# def register_middleware(app):
# 	@app.route('/api', defaults={'path': ''})
# 	@app.route('')
	


# def register_extensions(app):
# 	oauth2.init_app(app)


def register_routes(app):
	@app.route('/')
	def index():
		app.logger.info("BeforeRequest: {}".format(app.before_request))
        # app.logger.info(dir(before_request))
        # app.logger.info('Creds {}'.format(request.headers))
		return 'Welcome to the Audiobooks Application!'

if __name__ == '__main__':
	from app.config import config
	app = create_app(config=config)
	app.run( host='0.0.0.0', debug=True )