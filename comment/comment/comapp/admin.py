from django.contrib import admin
from comapp.models import *
# Register your models here.


admin.site.register(comment)

admin.site_header = 'Comment System'