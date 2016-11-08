from django.contrib import admin
from .models import Post

admin.site.register(Post)  #el modelo que teniamos en models.py lo registramos aca para poder verlo en el adminsite
