from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_swagger_ui_html
)
from src.config import get_settings


def create_app() -> FastAPI:
    app = FastAPI(docs_url=None)

    @app.get("/health")
    async def healthcheck():
        return "Hello world"

    @app.get("/settings")
    async def settings_test():
        return get_settings()

    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.14.0/swagger-ui-bundle.js",
            swagger_css_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.14.0/swagger-ui.css",
        )

    from src.routers import client, account, line
    app.include_router(client.router)
    app.include_router(account.router)
    app.include_router(line.router)
    return app
