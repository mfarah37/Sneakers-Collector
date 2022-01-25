from django.contrib import admin
from .models import Sneaker, Resale, Condition, Photo
# Register your models here.
admin.site.register(Sneaker)
admin.site.register(Resale)
admin.site.register(Condition)
admin.site.register(Photo)