from django.shortcuts import render
from core.models import Evento
from django.contrib.auth.decorators import login_required


# Create your views here.

# def index(request):
#     return redirect('/agenda')

def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
