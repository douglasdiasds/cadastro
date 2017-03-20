from django.shortcuts import render, get_object_or_404
from .models import Candidato, Criterio, Avaliacao
from django import forms
from .forms import CandForm
from .forms import AvalForm
from django.shortcuts import redirect


def canditato_list(request):
	candidatos = Candidato.objects.all()
	return render(request, 'app/candidato_list.html', {'candidatos': candidatos})

def candidato_detalhe(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    return render(request, 'app/candidato_detalhe.html', {'candidato': candidato})

def avaliar(request):
	if request.method == "POST":
		form2 = AvalForm(request.POST)
		
		##################################################################################
		aval = Avaliacao.objects.all()			#
		lista_cand = []							#
		for a in aval:							#nesse bloco eu ponho tds os avaliadores
			lc = str(a.avaliador)				#existentes em uma lista	
			lista_cand += [lc]					#
		##################################################################################	

		if form2.is_valid():
			### ai aqui eu guardo o avaliador atual na variavel
			avaliador = form2.cleaned_data['avaliador']

			### aqui eu faço o teste
			
			post = form2.save(commit=False)
			#avaliador = form2.fields['avaliador']
			post.save()
			#faz redirecionara para uma page que só tenha{'avaliador': avaliador} p/ testar a variavel avaliador
			return redirect('canditato_list') 
	else:
		form2 = AvalForm()
		#avaliador = form2.fields['avaliador']
		#teste
		return render(request, 'app/avaliacao.html', {'criterios': form2,})

	
def cadastrar(request):
	if request.method == "POST":
		form = CandForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('candidato_detalhe', pk=post.pk)
	else:
		form = CandForm()
	return render(request, 'app/cadastro.html', {'form': form})