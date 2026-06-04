from devscripts.generate_models import generate_models
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = """
    Generates models.py based on an
    Excel spreadsheet file describing the schema.
    """

    def add_arguments(self, parser):
        parser.add_argument("dest", help="Destination of the models file")

        parser.add_argument("base", help="Source of the base models file")

    def handle(self, *args, **options):
        dest = options["dest"]
        base = options["base"]
        generate_models(dest=dest, base_models=base, output=self.stdout.write)
