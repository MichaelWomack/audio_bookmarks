from flask import Flask, request

from app import connection_manager, setup_db
from app.api import audiobooks
from app.config import oauth2
from app.config.config_objects import Config


def create_app(config: Config=Config()):
	app = Flask( __name__ )
	app.config.from_object(config)
	setup_db(resource_package='app.resources.sql', cm=connection_manager)
	register_extensions(app)
	register_blueprints(app)
	register_routes(app)
	return app


def register_blueprints(app):
	app.register_blueprint( audiobooks, url_prefix='/api/audiobooks' )


def register_extensions(app):
	oauth2.init_app(app)


def register_routes(app):
	@app.route('/')
	@oauth2.required
	def index():
		app.logger.info('Creds {}'.format(request.headers))
		return 'Welcome to the Audiobooks Application! {}'.format(oauth2.email)

if __name__ == '__main__':
	from app.config import config
	app = create_app(config=config)
	app.run( host='0.0.0.0', debug=True )