import random
from datetime import date

import faker  # генерация фейковых имен и фамилий
from django.core.management.base import BaseCommand

from hwapp_2.models import Client

fake = faker.Faker('ru_RU')


class Command(BaseCommand):
    help = "Create Clients (random fake)"

    def handle(self, *args, **kwargs):
        count = 10  # количество создаваемых товаров
        for i in range(count):
            # random_email=f'{translit(random_name, language_code="ru", reversed=True)}_{random.randint(100,1000)}@mail.ru'
            date_reg = date(year=random.randint(2022, 2024), month=random.randint(1, 12), day=random.randint(1, 30))
            client = Client(name=fake.name(),
                            email=fake.ascii_free_email(),
                            telephone=fake.phone_number(),
                            password=fake.lexify(text='Random Identifier: ??????????'),
                            address=fake.address(),
                            date_reg=date_reg)
            client.save()
            self.stdout.write(f'Create client: {client}')
        self.stdout.write(f'Total: {count} clients create')
