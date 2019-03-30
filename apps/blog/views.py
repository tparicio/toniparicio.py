from django.shortcuts import render
from django.http import HttpResponse
from apps.quotes.models import Quote
from apps.socials.models import SocialNetwork
from apps.skills.models import Category
from apps.projects.models import Project
from apps.courses.models import Course
from apps.experience.models import Experience


def index(request):
    data = {
        'quote': Quote.objects.order_by('?').first(),
        'socials': SocialNetwork.objects.all(),
        'projects': Project.objects.all(),
        'categories': Category.objects.all(),
        'courses': Course.objects.all(),
        'experience': Experience.objects.all()
    }
    return render(request, 'blog/index.html', data)

