# appmountain/management/commands/wait_for_db.py
import time
import psycopg2
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Ожидает готовности базы данных'

    def handle(self, *args, **options):
        self.stdout.write('Ожидание базы данных...')
        for _ in range(30):
            try:
                conn = psycopg2.connect(
                    dbname="mountains_db",
                    user="mountains",
                    password=1234,  # Замените на ваш пароль
                    host="dbps"
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS('База данных готова!'))
                return
            except psycopg2.OperationalError:
                self.stdout.write('База не готова, ожидание 1 сек...')
                time.sleep(1)
        self.stdout.write(self.style.ERROR('Не удалось подключиться к базе через 30 сек'))
        exit(1)