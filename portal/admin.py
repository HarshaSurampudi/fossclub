from django.contrib import admin
from .models import TagElement, Profile,Project,JoinRequest
# Register your models here.
admin.site.register(TagElement)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(JoinRequest)
