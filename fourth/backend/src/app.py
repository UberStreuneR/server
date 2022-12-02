from fastapi import FastAPI, Request, Cookie, Response, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_swagger_ui_html
)
import time
import uuid
import json
from redis import Redis


from src.fake import FixtureGenerator
from src.utils import get_redis


def create_app() -> FastAPI:
    app = FastAPI(docs_url=None)

    @app.get("/fake-data")
    async def get_fake_data():

        fixture_generator = FixtureGenerator()
        first, second, third = fixture_generator.get_images()

        return {"first": first, "second": second, "third": third}

    @ app.get("/crucial-data")
    async def get_crucial_data(request: Request):
        r: Redis = get_redis()
        session_id = request.cookies.get("session_id")
        crucial_data = r.get(session_id)
        return crucial_data

    @ app.middleware("http")
    async def session_middleware(request: Request, call_next):
        session_id = request.cookies.get("session_id")
        if session_id is not None:
            r: Redis = get_redis()
            username = request.cookies.get("username")
            theme = request.cookies.get("lightThemeOn")
            language = request.cookies.get("language")
            crucial_data = f"{username}:{theme}:{language}"
            r.set(session_id, str(crucial_data))
        response = await call_next(request)
        if session_id is None:
            response.set_cookie("session_id", uuid.uuid4())
        return response

    @ app.get("/files/{filename}")
    async def get_file(filename: str):
        try:
            with open(f"src/files/{filename}.pdf", "rb") as file:
                data = file.read()
                if str(data).find("%PDF-") == -1:
                    raise HTTPException(
                        status_code=500, detail="File content type is not incorrect")
                return {"file_size": len(data), "file_data": str(data)}
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="File not found")

    @ app.post("/files", status_code=201)
    async def create_file(file: UploadFile):
        if file.filename[-3:] != "pdf":
            raise HTTPException(
                status_code=400, detail="Uploaded file does not have pdf format")
        with open(f"src/files/{file.filename}", "wb") as new_file:
            data = await file.read()
            new_file.write(data)

        return {"file_name": file.filename}

    @app.get("/cookie")
    async def cookie_endpoint(request: Request, response: Response, username=Cookie("Guest"), lightThemeOn=Cookie(True), language=Cookie("rus")):
        content = {"message": f"Your selected language is {language}. Enjoy, {username}!",
                   "lightThemeOn": lightThemeOn}
        headers = {
            "Set-Cookie": f"lightThemeOn={lightThemeOn}"
        }
        response.body = json.dumps(content)
        response.status_code = 233
        response.set_cookie("mycrazycookie", "hellooooooooooo")
        response.headers.update(headers)
        return response

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

    @app.middleware("http")
    async def add_elapsed_time_header(request: Request, call_next):
        start = time.perf_counter()

        response = await call_next(request)
        end = time.perf_counter()
        response.headers['X-Response-Time'] = "{:.2f}".format(end-start) + "s"
        return response

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
