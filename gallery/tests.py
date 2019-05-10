from django.test import TestCase
from .models import Location, Category ,Image

# Create your tests here.
class LocationTestClass(TestCase):
    # Set Up Method
    def setUp(self):
        self.nairobi = Location(photo_location='Nairobi')
        self.nairobi.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.nairobi.id)
        location.update_location('Kitengela')
        location = Location.get_location_id(self.nairobi.id)
        self.assertTrue(location.photo_location == 'Kitengela')
    
    def tearDown(self):
        self.nairobi.delete_location()

