from django.contrib import admin
from golos.models import Candidat,UserD
# Register your models here.

@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','middle_name','votes')
    readonly_fields = ('votes',)

@admin.register(UserD)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    readonly_fields = ('is_voted',)