from django.contrib import admin
from .models import Job, Quote

admin.site.register([Job, Quote])