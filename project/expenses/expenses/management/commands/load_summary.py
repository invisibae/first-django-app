import csv
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "./summary.csv"
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
