from django.shortcuts import render,redirect,get_object_or_404

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,   # From email
            ['manojggm14@gmail.com'],      # To email (change this)
            fail_silently=False,
        )

        return render(request, "home.html", {"success": True})

    return render(request, "home.html")
