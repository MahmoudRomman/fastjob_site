from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.JobCategory)
admin.site.register(models.Job)
admin.site.register(models.Employee_Detail)
admin.site.register(models.Contact)
admin.site.register(models.Comment)

