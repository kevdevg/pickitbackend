from django.contrib import admin

# Register your models here.
from entries.models import Entry

admin.site.register(Entry)
