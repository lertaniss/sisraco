from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Coordenadas, Onibus, Paradas, Rotas, DistanciasR, DistanciaTR
from django_filters import rest_framework as filters
from .serializers import CoordenadasSerializer, ParadasSerializer, RotasSerializer, OnibusSerializer, DistanciasRSerializer, DistanciaTRSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.models import Group
from .forms import OnibusForm, ParadasForm

def principal(request):
    return render(request,'index.html')

@login_required
def motorista(request):
	onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)
	if onibus:
		onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)[0]
		return render(request,'motorista.html', {"id_onibus": onibus.oni_codigo})
	else:
		return redirect('/newOnibus')

@require_POST
def cadastro(request):
	logout(request)
	try:
		email_aux = User.objects.all().filter(email=request.POST['email'])
		user_aux = User.objects.all().filter(username=request.POST['usuario'])
		if email_aux or user_aux:
			return render(request, 'registration/login.html',{"mensagem":"Um motorista com esse email ou usuário já está cadastrado em nosso sistema! Faça um novo cadastro ou tente recuperar sua senha"})
		grupo = Group.objects.get(name='Motoristas') 
		nome = request.POST['nome']
		usuario= request.POST['usuario']
		email = request.POST['email']
		senha = request.POST['senha']
		user = User.objects.create_user(usuario, email, senha)
		user.first_name = nome
		user.save()
		grupo.user_set.add(user)
	except User.DoesNotExist:
		print("Erro")
	return render(request, 'registration/login.html',{"mensagem":"Motorista cadastrado com sucesso! Faça login!"})

def cadastrar(request):
	if request.user.is_authenticated:
		logout(request) 
	return render(request,'cadastrar.html')	

@login_required
def criarOnibus(request):
	bus = Onibus.objects.all().filter(oni_mot_codigo=request.user)
	if bus:
		return render(request,'motorista.html', {"id_onibus": bus})
	if request.method == "POST":
		form = OnibusForm(request.POST)
		if form.is_valid():
			onibus = form.save(commit=False)
			onibus.oni_mot_codigo = request.user
			onibus.save()
			return redirect('/motorista')
	else:
		form = OnibusForm()
		return render(request,'addOnibus.html', {'form': form})
@login_required
def editarOnibus(request):
	onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)[0]
	if request.method == "POST":
		form = OnibusForm(request.POST, instance = onibus)
		if form.is_valid():
			oni = form.save()
			return redirect('/motorista')
		else:
			return render(request,'editarOnibus.html', {'onibus': onibus})
	else:
		return render(request,'editarOnibus.html', {'onibus': onibus})
@login_required
def rota(request):
	id_onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)[0]
	rotaview = Rotas.objects.all().filter(rot_oni_codigo=id_onibus.oni_codigo)
	if rotaview:
		return render(request,'rota.html', {"codigo": id_onibus.oni_codigo, "rota": rotaview})
	return render(request,'rota.html', {"rotaview": 1, "codigo": id_onibus.oni_codigo})

def verRota(request):
	json = '{"type": "LineString",  "coordinates": ['
	id_onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)[0]
	rotaview = Rotas.objects.all().filter(rot_oni_codigo=id_onibus.oni_codigo)
	qtd = 0
	for a in rotaview:
		qtd = qtd+1
		if (len(rotaview)==qtd):
			json = json+"[" + str(a.rot_x) + ", " + str(a.rot_y) + "]"
		else:
			json = json+"[" + str(a.rot_x) + ", " + str(a.rot_y) + "], "

	json = json+']}'

	return HttpResponse(json, content_type="text/json")

@login_required
def deleteRotas(request):
	id_onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)[0]
	rotas = Rotas.objects.all().filter(rot_oni_codigo=id_onibus.oni_codigo)
	paradas = Paradas.objects.all().filter(par_oni_codigo=id_onibus.oni_codigo)
	rotas.delete()
	paradas.delete()	
	return redirect('/rota')
	
@login_required
def paradas(request):
	id_onibus = Onibus.objects.all().filter(oni_mot_codigo=request.user)[0]
	para = Paradas.objects.all().filter(par_oni_codigo=id_onibus.oni_codigo)
	return render(request,'paradas.html', {'paradas': para})
@login_required
def editarParada(request, id):
	parada = get_object_or_404(Paradas, pk=id)
	if request.method == "POST":
		form = ParadasForm(request.POST, instance = parada)
		if form.is_valid():
			par = form.save(commit=False)
			par.par_x = parada.par_x
			par.par_y = parada.par_y
			par.par_oni_codigo = parada.par_oni_codigo
			par.save()
			return redirect('/paradas')
		else:
			return render(request,'editarParadas.html', {'parada': parada})
	else:
		return render(request,'editarParadas.html', {'parada': parada})


def gerar(request):
	json = '{"type": "LineString",  "coordinates": ['
	coordenadas = Coordenadas.objects.all()
	qtd = 0
	vetor = []
	aux = []
	max_codigo = -1
	for a in coordenadas:
		aux.append(a.cor_oni_codigo.oni_codigo)	
	max_codigo = max(aux) + 1

	for a in range (max_codigo):
		vetor.append("")

	for a in coordenadas:
		if (vetor[a.cor_oni_codigo.oni_codigo]==""):
			vetor[a.cor_oni_codigo.oni_codigo]="[" + str(a.cor_x) +","+str(a.cor_y)+"]"
		else:
			vetor[a.cor_oni_codigo.oni_codigo]= str(vetor[a.cor_oni_codigo.oni_codigo]) + ", [" + str(a.cor_x) +","+str(a.cor_y)+"]"		

	for a in range(len(vetor)):
		qtd = qtd+1
		if (qtd==len(vetor)):
			json = json+" [" + str(vetor[a]) + "]"
		else:
			json = json+"[" + str(vetor[a]) + "],"

	json = json+']}'
	return HttpResponse(json, content_type="text/json")

def transmitir(request):
	json = '{"type": "LineString",  "coordinates": ['
	coordenadas = Coordenadas.objects.all()
	qtd = 0
	vetor = []
	aux = []
	max_codigo = -1
	for a in coordenadas:
		aux.append(a.cor_oni_codigo)
	max_codigo = max(aux) + 1

	for a in range (max_codigo):
		vetor.append("")

	for a in coordenadas:
		if (vetor[a.cor_oni_codigo]==""):
			vetor[a.cor_oni_codigo]="[" + str(a.x) +","+str(a.y)+"]"
		else:
			vetor[a.cor_oni_codigo]= str(vetor[a.cor_oni_codigo]) + ", [" + str(a.cor_x) +","+str(a.cor_y)+"]"		

	for a in range(len(vetor)):
		qtd = qtd+1
		if (qtd==len(vetor)):
			json = json+" [" + str(vetor[a]) + "]"
		else:
			json = json+"[" + str(vetor[a]) + "],"

	json = json+']}'
	return HttpResponse(json, content_type="text/json")	
	
class CoordenadasList(generics.ListCreateAPIView):
    queryset = Coordenadas.objects.all()
    serializer_class = CoordenadasSerializer
class ParadasView(generics.ListCreateAPIView):
	queryset = Paradas.objects.all()
	serializer_class = ParadasSerializer
class RotasView(generics.ListCreateAPIView):
	queryset = Rotas.objects.all()
	serializer_class = RotasSerializer
class OnibusView(generics.ListCreateAPIView):
	queryset = Onibus.objects.all()
	serializer_class = OnibusSerializer
class DistanciasRView(generics.ListCreateAPIView):
	queryset = DistanciasR.objects.all()
	serializer_class = DistanciasRSerializer
class DistanciaTRView(generics.ListCreateAPIView):
	queryset = DistanciaTR.objects.all()
	serializer_class = DistanciaTRSerializer