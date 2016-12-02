from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, UpdateView, FormView,ListView,DetailView, DeleteView
from .models import Donadores,Donaciones_Monetarias, Donaciones_Especie
from django.core.urlresolvers import reverse_lazy
from pacientes.forms import HistorialMedico_Form

class Donadores_register_view(TemplateView):
	template_name = 'donadores_register.html'

class Register_Donadores(CreateView):
	template_name ='donadores_register.html'
	model = Donadores
	fields = '__all__'
	success_url = reverse_lazy('Index_view')
class Register_Donaciones_Monetarias(CreateView):
	template_name ='donadores_monetarias_register.html'
	model = Donaciones_Monetarias
	fields = '__all__'
	success_url = reverse_lazy('Index_view')
class Register_Donaciones_Especie(CreateView):
	template_name ='donadores_especie_register.html'
	model = Donaciones_Especie
	fields = '__all__'
	success_url = reverse_lazy('Index_view')
class donadores_report(ListView):
	template_name = 'donadores_report.html'
	model = Donadores
class donaciones_monetarias_report(ListView):
	template_name = 'donaciones_monetarias_report.html'
	model = Donaciones_Monetarias
class donaciones_especie_report(ListView):
	template_name = 'donaciones_especie_report.html'
	model = Donaciones_Especie
class Eliminar_Donador(UpdateView):
  	model=Donadores
  	fields='__all__'
  	template_name='eliminar_donadores.html'
  	success_url=reverse_lazy('reporte_eventos')

class Eliminar_Donaciones_monetarias(UpdateView):
  	model=Donaciones_Monetarias
  	fields='__all__'
  	template_name='eliminar_donaciones_monetarias.html'
  	success_url=reverse_lazy('Donaciones_monetarias_eliminar_view')

class Eliminar_Donaciones_especie(UpdateView):
  	model=Donaciones_Especie
  	fields='__all__'
  	template_name='eliminar_donaciones_especie.html'
  	success_url=reverse_lazy('Donadores_especie_eliminar_view')