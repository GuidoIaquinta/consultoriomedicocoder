from django.contrib import admin
from .views import Paciente,Enfermero,Medico,Administrativo
# Register your models here.
admin.site.register(Administrativo)
admin.site.register(Medico)
admin.site.register(Enfermero)
admin.site.register(Paciente)