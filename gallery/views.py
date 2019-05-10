from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location, Category

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

class Location(models.Model):
    photo_location = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.photo_location = update
        self.save()
    
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

    def __str__(self):
        return self.photo_location
