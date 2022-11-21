from faker import Faker
from faker.providers import DynamicProvider
import matplotlib.pyplot as plt
import numpy as np
import random
from typing import List
import io
from PIL import Image

fake = Faker()

professions_provider = DynamicProvider(provider_name="job", elements=[
    "Programmer", "Surgeon", "Director", "Chief Executive Officer", "Cashier"
])
fake.add_provider(professions_provider)

family_status_provider = DynamicProvider(provider_name="family_status", elements=[
    "Married", "Single", "Engaged", "Divorced"
])
fake.add_provider(family_status_provider)

life_satisfaction_provider = DynamicProvider(provider_name="life_satisfaction", elements=[
    "Happy", "Satisfied", "Moreless", "So-so", "Unhappy", "Depressed"
])
fake.add_provider(life_satisfaction_provider)


def generate_fixtures() -> List[dict]:
    fixtures = []
    for _ in range(50):
        person = {}
        person['name'] = fake.name()
        person['job'] = fake.job()
        person['age'] = random.randint(20, 55)
        person['salary'] = random.randint(50000, 250000)
        person['family'] = fake.family_status()
        person['life_satisfaction'] = fake.life_satisfaction()
        fixtures.append(person)
    return fixtures


def get_salary_to_age(fixtures: List[dict]) -> io.BytesIO:
    x = [person['age'] for person in fixtures]
    y = [person['salary'] for person in fixtures]
    return zip(*sorted(zip(x, y)))


def get_life_sat_to_salary(fixtures: List[dict]) -> io.BytesIO:
    x = [person['salary'] for person in fixtures]
    y = [person['life_satisfaction'] for person in fixtures]
    return zip(*sorted(zip(x, y)))


def get_salary_to_job(fixtures: List[dict]) -> io.BytesIO:
    x = [person['salary'] for person in fixtures]
    y = [person['job'] for person in fixtures]
    return zip(*sorted(zip(x, y)))


def get_chart_from_x_y(x: List, y: List) -> io.BytesIO:
    fig, ax = plt.subplots()
    ax.plot(x, y)
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    return buffer


def get_pie_chart_from_x_y(x: List, y: list) -> io.BytesIO:
    data = {}
    for label in set(y):
        data[label] = 0
    for index, value in enumerate(x):
        data[y[index]] += value
    fig, ax = plt.subplots()
    # print(x, y)
    ax.pie(list(data.values()), labels=list(data.keys()))
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    return buffer


def get_bar_chart_from_x_y(x: List, y: List) -> io.BytesIO:
    data = {}
    for label in set(y):
        data[label] = 0
    for index, value in enumerate(x):
        data[y[index]] += value
    fig, ax = plt.subplots()
    ax.xaxis.set_tick_params(labelsize=7)
    ax.bar(list(data.keys()), list(data.values()))
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    return buffer


def show_image_from_buffer(img_buf: io.BytesIO):
    image = Image.open(img_buf)
    image.show()


def add_watermark_to_img(img_buf: io.BytesIO):
    image = Image.open(img_buf)
    # mark = Image.open("./files/watermark.png")
    mark = Image.open("./src/files/watermark.png")
    mark = mark.resize((50, 50))
    image.paste(mark, (20, 20), mark)
    buffer = io.BytesIO()
    image.save(buffer, 'png')
    return buffer
    # image.show()


fixtures = generate_fixtures()
# data = get_salary_to_age(fixtures)
# data = get_life_sat_to_salary(fixtures)
data = get_salary_to_job(fixtures)
# buffer = get_chart_from_x_y(*data)
# buffer = get_pie_chart_from_x_y(*data)
buffer = get_bar_chart_from_x_y(*data)
img = add_watermark_to_img(buffer)
img = Image.open(img)
img.show()
# show_image_from_buffer(buffer)
# show_image_with_watermark(buffer)
