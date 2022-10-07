from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_swagger_ui_html
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

def create_app() -> FastAPI:
    app = FastAPI(
        title="orders",
        description="Simple API to order products from different stores.",
        version="1.0",
        docs_url=None
    )
    
    origins = [
    "http://localhost:5173",
]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # app.mount('/static', StaticFiles(directory="src/orders_api/static"), name="static")

    @app.get("/health")
    async def health() -> str:
        return "ok"

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.14.0/swagger-ui-bundle.js",
            swagger_css_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.14.0/swagger-ui.css",
        )

    from orders_api.routers import orders, products, stores

    app.include_router(orders.router)
    app.include_router(products.router)
    app.include_router(stores.router)
    return app
