from django.contrib import admin

# Register your models here.
from .models import Position, Club, Player

#admin.site.register(Position)
#admin.site.register(Player)
#admin.site.register(Club)
# Define the admin class
class PlayerInline(admin.TabularInline):
    model = Player
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'trophies', 'information')
    list_filter = ('trophies', 'country')
    fields = ['name', 'country', 'information', ('trophies',)]
    inlines = [PlayerInline]
# Register the admin class with the associated model
admin.site.register(Club, ClubAdmin)
# Register the Admin classes for Book using the decorator
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('Full_name', 'current_club', 'position')
class PlayerInline(admin.TabularInline):
    model = Player
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...