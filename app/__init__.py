from app.routes import home, dashboard, api
from app.db import init_db
# from app.utils import filters
from flask import Flask

# def create_app(test_config=None):
  # app = Flask(__name__, static_url_path='/')
  # app.url_map.strict_slashes = False
  # app.config.from_mapping(
  #   SECRET_KEY='super_secret_key'
  # )


  # app.register_blueprint(home)
  # app.register_blueprint(dashboard)
  # app.register_blueprint(api)

  # app.jinja_env.filters['format_url'] = filters.format_url
  # app.jinja_env.filters['format_date'] = filters.format_date
  # app.jinja_env.filters['format_plural'] = filters.format_plural

  # init_db(app)

  # return app
def create_app(test_config=None):
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='discovery_secret_key'
  )

  app.register_blueprint(home)

  @app.route('/tests')
  def test():
    return {"tests":["Test1", "Test2", "Test3"]}
    
  if __name__ == "__main__":
    app.run(debug=True)

  init_db(app)

  return app