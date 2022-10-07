from typing import Tuple
from PIL import Image, ImageDraw

def generate_image(shape: str, color: str, size: Tuple[int, int]) -> bytes:
    print(shape, color, size)
    image = Image.new('RGB', size, "white")
    draw = ImageDraw.Draw(image)
    if shape == 'circle':
        draw.ellipse((0, 0, *size), color)
    else:
        draw.rectangle((0, 0, *size), color)
    return image.tobytes()

shape_data = {
    'shape': {0: 'rect', 1: 'square', 2: 'circle'},
    'color': {0: 'red', 1: 'green', 2: 'blue'},
}

def shape_params(num: int) -> Tuple:
    shape_mask = 192 # 11000000
    color_mask = 48 # 00110000
    rect_width_mask = 12 # 00001100
    rect_height_mask = 3 # 00000011
    shape = (num & shape_mask) >> 6
    color = (num & color_mask) >> 4
    width = (num & rect_width_mask) >> 2
    height = num & rect_height_mask
    return shape_data['shape'][shape], shape_data['color'][color], (width*64, height*64)
