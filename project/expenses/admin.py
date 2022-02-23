from django.contrib import admin
from expenses.models import Summary
# Register your models here

class SummaryAdmin(admin.ModelAdmin): # Creates a 'SummaryAdmin' class that is tied to 'summary'
    list_display = ("office", "program", "category", "amount") #choose what variables to display

admin.site.register(Summary, SummaryAdmin)
