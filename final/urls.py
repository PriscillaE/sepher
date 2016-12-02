"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bases.views import Index_view, Registro_Minutas, Detalle_minuta, Reporte_Minutas, Registro_Eventos, Eliminar_Eventos, Editar_Evento, Reporte_Eventos, Detalle_eventos, Registro_Personal, Eliminar_Personal, Editar_Personal, Reporte_Personal
from donaciones.views import Donadores_register_view, Register_Donadores, Register_Donaciones_Monetarias, Register_Donaciones_Especie, donadores_report, donaciones_monetarias_report, donaciones_monetarias_report, donaciones_especie_report, Eliminar_Donador, Eliminar_Donaciones_monetarias, Eliminar_Donaciones_especie
from pacientes.views import Registro_Apoyo, Reporte_Apoyo, Registro_Defunciones, Reporte_Defunciones, Eliminar_Defunciones, Registro_paciente
from pacientes.views import Reporte_Paciente, Eliminar_Paciente, EditarPaciente, Paciente_detalle, Update_paciente, Registro_Historial
from pacientes.views import consulta
from django.contrib.auth.views import login, logout_then_login
from bases.views import calendar,calendar_eventadded,calendar_add_event, calendar_auth_return

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index_view.as_view(), name = 'Index_view'),
    url(r'^Donadores_register/$', Register_Donadores.as_view(), name = 'Donadores_register_view'),
    url(r'^Donadores_monetarias_register/$', Register_Donaciones_Monetarias.as_view(), name = 'Donadores_monetarias_register_view'),
    url(r'^Donadores_especie_register/$', Register_Donaciones_Especie.as_view(), name = 'Donadores_especie_register_view'),
    url(r'^Donadores_ediar/$', donadores_report.as_view(), name = 'Donadores_eliminar_view'),
    url(r'^Donaciones_monetarias_editar/$', donaciones_monetarias_report.as_view(), name = 'Donaciones_monetarias_eliminar_view'),\
    url(r'^Donaciones_especie_editar/$', donaciones_especie_report.as_view(), name = 'Donadores_especie_eliminar_view'),
    url(r'^editar_donador/(?P<pk>\d+)$',Eliminar_Donador.as_view(),name='eliminar_donador_view'),
    url(r'^editar_donaciones_monetarias/(?P<pk>\d+)$',Eliminar_Donaciones_monetarias.as_view(),name='eliminar_donaciones_monetarias_view'),
    url(r'^editar_donaciones_especie/(?P<pk>\d+)$',Eliminar_Donaciones_especie.as_view(),name='eliminar_donaciones_especie_view'),
    url(r'^registro_paciente/$',Registro_paciente.as_view(),name='RegistroPac_view'),
    url(r'^reporte_pacientes/$',Reporte_Paciente.as_view(),name='reporte_pacientes'),
    url(r'^editar_paciente/(?P<pk>\d+)$',EditarPaciente.as_view(),name='editar_paciente_view'),
    url(r'^detalle_paciente/(?P<pk>\d+)$',Paciente_detalle,name='paciente_detalle_view'),
    url(r'^registro_medico/$',Registro_Historial.as_view(),name='RegistroMed_view'),
    url(r'^registro_minutas/$',Registro_Minutas.as_view(),name='RegistroMin_view'),
    url(r'^detalle_minuta/(?P<pk>\d+)$',Detalle_minuta.as_view(),name='DetalleMin_view'),
    url(r'^reporte_minutas/$',Reporte_Minutas.as_view(),name='ReporteMin_view'),
    url(r'^registro_defunciones/$',Registro_Defunciones.as_view(),name='RegistroDef_view'),
    url(r'^registro_apoyo/$',Registro_Apoyo.as_view(),name='RegistroApy_view'),
    url(r'^reporte_defunciones/$',Reporte_Defunciones.as_view(),name='ReporteDef_view'),
    url(r'^eliminar_defunciones/(?P<pk>\d+)$',Reporte_Defunciones.as_view(),name='EliminarDef_view'),
    url(r'^registro_eventos/$',Registro_Eventos.as_view(),name='RegitroEve_view'),
    url(r'^eliminar_eventos/(?P<pk>\d+)$',Eliminar_Eventos.as_view(),name='EliminarEve_view'),
    url(r'^editar_evento/(?P<pk>\d+)$',Editar_Evento.as_view(),name='editar_evento_view'),
    url(r'^reporte_eventos/$',Reporte_Eventos.as_view(),name='ReporteEve_view'),
    url(r'^detalle_evento/(?P<pk>\d+)$',Detalle_eventos.as_view(),name='DetalleEve_view'),
    url(r'^registro_personal/$',Registro_Personal.as_view(),name='RegitroPer_view'),
    url(r'^eliminar_personal/(?P<pk>\d+)$',Eliminar_Personal.as_view(),name='EliminarPer_view'),
    url(r'^editar_personal/(?P<pk>\d+)$',Editar_Personal.as_view(),name='editar_personal_view'),
    url(r'^reporte_personal/$',Reporte_Personal.as_view(),name='ReportePer_view'),
    url(r'^consultas/$', consulta, name= 'consultas2'),
    url(r'^calendar/$', calendar, name="calendar"),
    url(r'^calendar/event_added/$', calendar_eventadded, name="calendar_eventadded"),
    url(r'^calendar/add_event/(?P<event_id>[0-9]+)/$', calendar_add_event, name="add_event"),
    url(r'^calendar/oauth2callback$', calendar_auth_return, name="calendar_auth_return"),
    
]
