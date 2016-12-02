from django.contrib import admin

from .models import Personal,Administradores,Eventos ,Minutas, Event


admin.site.register(Personal)
admin.site.register(Administradores)
admin.site.register(Minutas)
admin.site.register(Event)
