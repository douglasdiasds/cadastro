from django.shortcuts import render, get_object_or_404
from .models import Candidato, Criterio
from django import forms
from .forms import CandForm

def canditato_list(request):
	candidatos = Candidato.objects.all()
	return render(request, 'app/candidato_list.html', {'candidatos': candidatos})

def candidato_detalhe(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    return render(request, 'app/candidato_detalhe.html', {'candidato': candidato})

def avaliar(request):
	criterios = Criterio.objects.all()
	return render(request, 'app/avaliacao.html', {'criterios': criterios})

def cadastrar(request):
	if request.method == "POST":
		form = CandForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.name = request.user
			post.save()
			return redirect('candidato_detalhe', pk=post.pk)
	else:
		form = CandForm()
		return render(request, 'app/cadastro.html', {'form': form})