from django.contrib import admin
from .models import ResumeData
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class ResumeAdmin(ImportExportModelAdmin):
    pass

admin.site.register(ResumeData,ResumeAdmin)