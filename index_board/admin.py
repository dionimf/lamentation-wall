from django.contrib import admin

from index_board import models

admin.site.register(models.LamentModel)
admin.site.register(models.CounselModel)
admin.site.register(models.VisitModel)
