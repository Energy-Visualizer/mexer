from django.test import TestCase
from Mexer import models

from utils.lookup import LookupManager


class TranslatorTests(TestCase):
    def test_get_all(self):
        lookups = LookupManager("default")
        energy_types = lookups[models.EnergyType].objects

        self.assertTrue(any(et.full_name == "Energy" for et in energy_types))
        self.assertTrue(any(et.full_name == "Exergy" for et in energy_types))

    def test_translations(self):
        lookups = LookupManager("default")
        translator = lookups[models.EnergyType].translator
        energy_translation = translator["Energy"]
        exergy_translation = translator["Exergy"]

        self.assertEqual(energy_translation, 1)
        self.assertEqual(exergy_translation, 2)

        reverse_energy_translation = translator[1]

        self.assertEqual(reverse_energy_translation, "Energy")

    def test_invalid_translation(self):
        lookups = LookupManager("default")
        translator = lookups[models.EnergyType].translator

        with self.assertRaises(KeyError):
            _ = translator["InvalidType"]
