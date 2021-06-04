from django.contrib import admin
from .models import NoteCard
from .models import Collection
# Register your models here.

admin.site.register(NoteCard)
admin.site.register(Collection)