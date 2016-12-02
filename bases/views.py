import httplib2
from django.shortcuts import render, redirect
from django.views.generic import CreateView,TemplateView, UpdateView, FormView,ListView,DetailView, DeleteView


from .models import Personal,Administradores,Minutas,Eventos
from django.core.urlresolvers import reverse_lazy
from pacientes.forms import HistorialMedico_Form

from django.conf import settings

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib import xsrfutil
from oauth2client.contrib.django_util.storage import DjangoORMStorage

from .models import CredentialsModel, DriveCredentialsModel, Event



class Index_view(TemplateView):
	template_name = 'index.html'

# Create your views here.  



class Registro_Minutas(CreateView):
	template_name='registro_minutas.html'
	model=Minutas
	fields='__all__'
	success_url=reverse_lazy('reporte_minutas')

class Detalle_minuta(DetailView):
	template_name='detalle_minuta.html'
	model=Minutas

class Reporte_Minutas(ListView):
	template_name='reporte_minutas.html'
	model=Minutas



class Registro_Eventos(CreateView):
	template_name='registro_eventos.html'
	model=Eventos
	fields='__all__'
	success_url=reverse_lazy('reporte_eventos')

class Eliminar_Eventos(DeleteView):
    model = Eventos
    success_url = reverse_lazy('reporte_eventos')

class Editar_Evento(UpdateView):
  	model=Eventos
  	fields='__all__'
  	template_name='editar_evento.html'
  	success_url=reverse_lazy('reporte_eventos')

class Reporte_Eventos(ListView):
	template_name='reporte_eventos.html'
	model=Eventos

class Detalle_eventos(DetailView):
	template_name='detalle_evento.html'
	model=Eventos


class Registro_Personal(CreateView):
	template_name='registro_personal.html'
	model=Personal
	fields='__all__'
	success_url=reverse_lazy('reporte_personal')

class Eliminar_Personal(DeleteView):
    model = Personal
    success_url = reverse_lazy('reporte_personal')

class Editar_Personal(UpdateView):
  	model=Personal
  	fields='__all__'
  	template_name='editar_personal.html'
  	success_url=reverse_lazy('reporte_personal')

class Reporte_Personal(ListView):
	template_name='reporte_personal.html'
	model=Personal

CALENDAR_FLOW = OAuth2WebServerFlow(
    settings.GOOGLE_OAUTH2_CLIENT_ID,
    settings.GOOGLE_OAUTH2_CLIENT_SECRET,
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://127.0.0.1:8000/calendar/oauth2callback'
)

DRIVE_FLOW = OAuth2WebServerFlow(
    settings.GOOGLE_OAUTH2_CLIENT_ID,
    settings.GOOGLE_OAUTH2_CLIENT_SECRET,
    scope='https://www.googleapis.com/auth/drive.metadata.readonly',
    redirect_uri='http://127.0.0.1:8000/drive/oauth2callback'
)

def calendar(request):
    context = {
        'events': Event.objects.all(),
    }
    if CredentialsModel.objects.filter(user=request.user).count() > 0:
        context['have_cred'] = True
    else:
        context['have_cred'] = False
    return render(request, 'calendar.html', context)

def calendar_eventadded(request):
    context = {
        'events': Event.objects.all(),
        'event_added': True,
    }

    if CredentialsModel.objects.filter(user=request.user).count() > 0:
        context['have_cred'] = True
    else:
        context['have_cred'] = False
    return render(request, 'calendar.html', context)

def calendar_add_event(request, event_id):
    storage = DjangoORMStorage(
        CredentialsModel,
        'user',
        request.user,
        'credential'
    )
    credential = storage.get()
    if credential is None or credential.invalid == True:
        CALENDAR_FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                       request.user)
        authorize_url = CALENDAR_FLOW.step1_get_authorize_url()
        return redirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)

        event = Event.objects.get(pk=event_id)
        calendar_service = build('calendar', 'v3', http=http)
        body = {
            'start': { "date": str(event.date) },
            'end': { "date": str(event.date) },
            'summary': event.summary
        }
        calendar_request = calendar_service.events().insert(
            calendarId='primary',
            body=body,
        )
        response = calendar_request.execute()
        return redirect('calendar_eventadded')

def calendar_auth_return(request):
    if not xsrfutil.validate_token(
            settings.SECRET_KEY,
            bytes(request.GET['state'], 'utf-8'),
            request.user):
        return  HttpResponseBadRequest()
    credential = CALENDAR_FLOW.step2_exchange(request.GET)
    storage = DjangoORMStorage(CredentialsModel, 'user', request.user, 'credential')
    storage.put(credential)
    return redirect('calendar')

