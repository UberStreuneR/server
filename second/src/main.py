from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse, Response, PlainTextResponse
from io import BytesIO
from PIL import Image
import os
from .image_utils import generate_image, shape_params
from .sort_utils import shell_sort

from typing import List

app = FastAPI()


"""
170 -> blue circle
26 -> green rectangle
10 -> red rect
"""
@app.get("/image")
def image_response(num: int):
    params = shape_params(num)
    image_bytes = generate_image(*params)
    img_io = BytesIO()
    b = Image.frombytes("RGB", params[2], image_bytes)
    b.save(img_io, "PNG")
    img_io.seek(0)
    img = img_io.read()
    return Response(content=img, media_type="image/png")


"""
http://localhost:8000/sort?array=3&array=2&array=1&array=10&array=7
"""
@app.get("/sort")
def sort_array(array: List[int] = Query(default=None)):
    return shell_sort(array)

@app.get("/server-info", response_class=PlainTextResponse)
def server_info():
    data = {}
    # commands = ["dir"]
    commands = ["dir", "whoami", "tasklist"]
    for command in commands:
        data.update({command: os.popen(command).read()})
    result = """"""
    for key, value in data.items():
        result += f"____________________________________________\n>{key}\n\n{value}\n"
    return result