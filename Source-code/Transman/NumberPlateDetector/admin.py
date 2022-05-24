from django.contrib import admin

from .models import carEntry
from .models import carExit
from .models import carDetails
# from .models import Test

admin.site.register(carEntry)
admin.site.register(carExit)
admin.site.register(carDetails)
# admin.site.register(Test)