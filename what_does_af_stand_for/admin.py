"""Administration configuration"""

from django.contrib import admin

from what_does_af_stand_for import models

admin.site.register(models.AWord)
admin.site.register(models.FWord)
