from django.contrib import admin
from expenses.models import Summary
# Register your models here.
admin.site.register(Summary)

class SummaryAdmin(admin.ModelAdmin): # Creates a 'SummaryAdmin' class that is tied to 'summary'
    list_display = ("office", "program", "category", "amount") #choose what variables to display

admin.site.register(Summary, SummaryAdmin)
    
