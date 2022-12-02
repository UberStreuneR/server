from faker import Faker
from faker.providers import DynamicProvider
import matplotlib.pyplot as plt
import numpy as np
import random
from typing import List, Tuple
import io
from PIL import Image
from base64 import b64encode

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


class FixtureGenerator:
    def __init__(self):
        self.fixtures = self.generate_fixtures()
        self.images = self.generate_images()

    def create_x_and_y(self, x_label: str, y_label: str):
        x = [person[x_label] for person in self.fixtures]
        y = [person[y_label] for person in self.fixtures]
        return zip(*sorted(zip(x, y)))

    def get_images(self):
        return self.images

    def generate_fixtures(self) -> List[dict]:
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

    def get_chart_from_x_y(self, x: List, y: List) -> io.BytesIO:
        fig, ax = plt.subplots()
        ax.plot(x, y)
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        return self.add_watermark_to_img(buffer)

    def get_pie_chart_from_x_y(self, x: List, y: list) -> io.BytesIO:
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
        return self.add_watermark_to_img(buffer)

    def get_bar_chart_from_x_y(self, x: List, y: List) -> io.BytesIO:
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
        buffer.seek(0)
        return self.add_watermark_to_img(buffer)

    def add_watermark_to_img(self, img_buf: io.BytesIO):
        # img_buf.seek(0)
        image = Image.open(img_buf)
        # mark = Image.open("./files/watermark.png")
        mark = Image.open("./src/files/watermark.png")
        mark = mark.resize((50, 50))
        image.paste(mark, (20, 20), mark)
        buffer = io.BytesIO()
        image.save(buffer, 'png')
        buffer.seek(0)
        return buffer

    def generate_images(self) -> Tuple[str, str, str]:
        age_to_salary = self.create_x_and_y("age", "salary")
        salary_to_life_sat = self.create_x_and_y("salary", "life_satisfaction")
        salary_to_job = self.create_x_and_y("salary", "job")

        salary_to_age_plot = self.get_chart_from_x_y(*age_to_salary)
        life_sat_pie = self.get_pie_chart_from_x_y(*salary_to_life_sat)
        salary_to_job_bar = self.get_bar_chart_from_x_y(*salary_to_job)

        return b64encode(salary_to_age_plot.read()), b64encode(
            life_sat_pie.read()), b64encode(salary_to_job_bar.read())
