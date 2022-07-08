"""
Django commands to wait for the database to be available.
it will keep pinging db to get ready. Then starts the app.
"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

import time


class Command(BaseCommand):
    # Django command to wait for the database
    def handle(self, *args, **options):
        # entry point for the command
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
