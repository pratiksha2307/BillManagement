from django.contrib import admin
from .models import Work, ChallanNumber, HSCNumber, Report, QuantityRate, MeltReport, MeltChallanNumber

class MeltReportAdmin(admin.ModelAdmin):
    list_display =('challan_number','particular','date','total','rate')


admin.site.register(Work)
admin.site.register(ChallanNumber)
admin.site.register(MeltChallanNumber)
admin.site.register(HSCNumber)
admin.site.register(Report)
admin.site.register(MeltReport,MeltReportAdmin)
admin.site.register(QuantityRate)