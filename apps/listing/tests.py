## Zander B. Wells <zbwells@protonmail.com>
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

from django.test import TestCase
from django.utils import timezone
from .models import Animal

# No comprehensive testing, but guarantees at least the base-line for functionality of the project.

# Tests:
class AnimalTest(TestCase):
    def test_setup(self):
        Animal.objects.create(
            name = "Rocky",
            id_num = 32,
            species = "Cat",
            breed = "Domestic Shorthair",
            weight = "8 lbs",
            gender = "Male",
            intake_date = timezone.now(),
            estimated_age = 2,
            image = "static/animal_test.jpg",
            notes = "Test",
            visible_on_website = True,
        )        

        Animal.objects.create(
            name = "Mando",
            id_num = 35,
            species = "Cat",
            breed = "Domestic Shorthair",
            weight = "8 lbs",
            gender = "Male",
            intake_date = timezone.now(),
            estimated_age = 2,
            image = "static/animal_test.jpg",
            notes = "Test",
            visible_on_website = True,
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/listing/")
        self.assertEqual(response.status_code, 200)

    
