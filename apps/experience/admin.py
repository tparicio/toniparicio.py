from django.contrib import admin
from .models import Experience
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Experience, SummernoteModelAdmin)
