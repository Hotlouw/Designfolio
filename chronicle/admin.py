from django.contrib import admin
from .models import Projects, Library, Email, Certification, Blog, Other, OtherLibrary
from .models import UserProfile

admin.site.register(UserProfile)



admin.site.register(Projects)
admin.site.register(Library)
admin.site.register(Email)
admin.site.register(Certification)
admin.site.register(Blog)
admin.site.register(Other)
admin.site.register(OtherLibrary)

