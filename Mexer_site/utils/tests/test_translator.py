from django.test import TestCase

from utils.lookup import LookupManager


class TranslatorTests(TestCase):
    def test_get_all(self):
        translator = LookupManager("default")
        translations = translator.attribute("energytype")

        self.assertIn("Energy", translations)
        self.assertIn("Exergy", translations)

    def test_translations(self):
        translator = LookupManager("default")
        energy_translation = translator.energytype_translate("Energy")
        exergy_translation = translator.energytype_translate("Exergy")

        self.assertEqual(energy_translation, 1)
        self.assertEqual(exergy_translation, 2)

        reverse_energy_translation = translator.energytype_translate(1)

        self.assertEqual(reverse_energy_translation, "Energy")

    def test_invalid_translation(self):
        translator = LookupManager("default")

        with self.assertRaises(KeyError):
            _ = translator.energytype_translate("InvalidType")
