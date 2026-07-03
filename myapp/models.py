from django.db import models

class homeService(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class OurService(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='our_services/')

    def __str__(self):
        return self.title

class PriceItem(models.Model):
    name = models.CharField(max_length=100)
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name