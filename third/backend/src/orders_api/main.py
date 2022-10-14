from orders_api.app import create_app
from a2wsgi import ASGIMiddleware

app = create_app()
application = ASGIMiddleware(app)