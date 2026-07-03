from django.contrib import admin
from .models import homeService,OurService,PriceItem,ContactMessage

admin.site.register(homeService)
admin.site.register(OurService)
admin.site.register(PriceItem)
admin.site.register(ContactMessage)