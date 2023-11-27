from pathlib import Path

from django.core.management.base import BaseCommand

from api.models import *  # noqa
import csv

class Command(BaseCommand):
    help = "Seeds the database."

    def handle(self, *args, **options):
        try:
            path = Path(__file__).resolve().parent / "fixtures"
            for fixture in path.iterdir():
                if fixture.suffix == ".csv":
                    fixture_path = str(fixture)
                    self.stdout.write(f"Seeding: {fixture_path}")
                    if fixture.stem == "book":
                        Book.objects.all().delete()
                        with fixture.open('r') as f:
                            reader = csv.DictReader(f)
                            for row in reader:
                                Book.objects.create(
                                    id=row['id'],
                                    title=row['title'],
                                    genre=row['genre'],
                                    year=row['year'],
                                )
                    self.stdout.flush()
        except Exception as e:
            print(e)
