from django.contrib import admin

# Register your models here.
from .models import TalkList, Talk
admin.site.register(TalkList)

admin.site.register(Talk)

