from django.contrib import admin
from .models import Post,Board,Topic

# Register your models here.
admin.site.register(Post)
admin.site.register(Board)
admin.site.register(Topic)