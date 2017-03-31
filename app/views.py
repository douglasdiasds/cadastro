from django.shortcuts import render, get_object_or_404
from .models import Candidate, Criterion, Evaluation
from django import forms
from .forms import CandForm
from .forms import EvalForm
from .forms import TestForm
from django.shortcuts import redirect
from django.db import IntegrityError


def canditate_list(request):
	candidates = Candidate.objects.all()
	
	eva = Evaluation.objects.all()
	eval_cand_list = []										#aqui guarda uma lista com os FK candidates convertidos p/ str
	var = 0
	var2 = {'v1':2}
	context = {
		'candidates': candidates,
		'eva': eva,
		'var': var,
		'var2':var2
	}
	return render(request, 'app/candidate_list.html',context)

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    c_name = candidate.name             					#pega o nome (string) do candidato
    c1 = Evaluation.objects.all()							#guarda tds Evaluation na variavel	
    scores = []												#declara a array que vai receber as notas
    for c in c1:											
    	cand = str(c.candidate)								#guarda o nome do candidato do Evaluation atual
    	if cand == c_name:									#confere se o Evaluation atual corresponde ao candidate atual(pk)
    		scores += [c.score]

    soma = 0												#variavel que guardara a soma declarada
    for s in scores:
    	soma += s                                           #faz a soma dos scores

    average = 0	
    if len(scores) > 0:
    	average = soma/len(scores)								#tira a média

    context = {
    	'candidate': candidate,
    	'average': average,
    }
    
    return render(request, 'app/candidate_detail.html', context)

"""
def evaluation(request):
    list_evaluation = Evaluation.objects.all()
    form2 = EvalForm()
    cont = 0

    if request.method == "POST":
    	form2 = EvalForm(request.POST)
    	if form2.is_valid():
    		for ev in list_evaluation:
    			cont += 1
"""
def evaluation(request):
    # form2 initialization
    list_evaluation = Evaluation.objects.all()
    form2 = EvalForm()
    marker = False
 
    if request.method == "POST":
        form2 = EvalForm(request.POST)
        if form2.is_valid() == True:
            for e in list_evaluation:
            	if e.appraiser == form2.cleaned_data['appraiser'] and e.candidate == form2.cleaned_data['candidate']:
            		marker = True
            		break
            if marker == False:
            	post = form2.save(commit=False)
            	post.save()
            	return redirect('canditate_list')
            else:
            	form2 = EvalForm()
            	error = 'Você já valiou esse candidato'
            	return render(request, 'app/evaluation.html', {'criterions': form2,'error':error})
    else:
        form2 = EvalForm()
    return render(request, 'app/evaluation.html', {'criterions': form2,})

def register(request):
	list_evaluation = Evaluation.objects.all()

	if request.method == "POST":
		form = CandForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('candidate_detail', pk=post.pk)
	else:
		form = CandForm()
	return render(request, 'app/register.html', {'form': form})


def grid(request):
	evaluation = Evaluation.objects.all()			#querryset com tds os obj avaliação
	cont = 0
	evaluators = []									#lista que guarda os avaliadores sem repeti-los
	for evaluator in evaluation:
		cont = 0
		for e in evaluators:
			if e != evaluator.appraiser:
				cont += 1

		if cont == len(evaluators):
			evaluators += [evaluator.appraiser]


	cont = 0
	candidates = []									#lista que guarda os avaliador sem repeti-los
	for cand in evaluation:
		cont = 0
		for c in candidates:
			if c != cand.candidate:
				cont += 1

		if cont == len(candidates):
			candidates += [cand.candidate]

	
	#							Numero de colunas				Numero de linhas					
	matrice = [[0 for i in range(len(evaluators)+1)] for j in range(len(candidates)+1)]	

	cont_c = 0
	cont_a = 0
	for l in range(len(matrice)):
		for c in range(len(matrice[l])):
			if l == 0 and c > 0:
				matrice[l][c] = str(evaluators[cont_a])
				cont_a += 1
			if l > 0 and c == 0:
				matrice[l][c] = str(candidates[cont_c])
				cont_c += 1

	cont_c = 0
	cont_a = 0
	for e in evaluation:
		for l in range(len(matrice)):
			if str(e.candidate) == matrice[l][0]:
				for c in range(len(matrice[l])):
					if str(e.appraiser) == matrice[0][c]:
						if matrice[l][c] == 0:
							matrice[l][c] = e.score
							break


	cont = 0		
	context = {										#aqui eh o nome que as variaveis terao la no template
			'evaluators':evaluators,
			'evaluation':evaluation,
			'candidates':candidates, 
			'cont':cont,
			'matrice':matrice,
		}

	return render(request, 'app/grade.html', context)