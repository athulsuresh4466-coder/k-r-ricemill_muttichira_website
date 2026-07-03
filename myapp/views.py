from django.shortcuts import render
from .models import homeService, OurService, PriceItem, ContactMessage

def home(request):

    # Fetch data for homepage
    home_services = homeService.objects.all()
    our_services = OurService.objects.all()
    prices = PriceItem.objects.all()

    # Handle Contact Form Submission
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "new.html", {
            "home_services": home_services,
            "our_services": our_services,
            "prices": prices,
            "success": True
        })

    # Normal page load
    return render(request, "new.html", {
        "home_services": home_services,
        "our_services": our_services,
        "prices": prices
    })