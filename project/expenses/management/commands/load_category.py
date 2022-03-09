import csv
from expenses.models import Category
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "./summary.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['CATEGORY'] != '':
                obj = Category.objects.create(name=row['CATEGORY'], slug=slugify(row['CATEGORY']))
                print(obj)
