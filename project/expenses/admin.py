from django.contrib import admin
from expenses.models import Summary, Detail
# Register your models here

class SummaryAdmin(admin.ModelAdmin): # Creates a 'SummaryAdmin' class that is tied to 'summary'
    list_display = ("office", "program", "category", "amount") #choose what variables to display
    list_filter = ("category", "program") # adds a filter function
    search_fields = ("program",) # add search field # comma creates 'tuple' (an immutable list)


class DetailAdmin(admin.ModelAdmin):
    list_display = ("office", "program", "category", "payee", "purpose", "amount")
    list_filter = ("category", "program", "purpose")
    search_fields = ("program", "payee")

admin.site.register(Summary, SummaryAdmin)
admin.site.register(Detail, DetailAdmin)
