from django.contrib import admin

from polls.models import Pollsquestions, voter

# Register your models here.
admin.site.register(Pollsquestions)
admin.site.register(voter)