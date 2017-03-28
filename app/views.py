from django.shortcuts import render, get_object_or_404
from .models import Candidate, Criterion, Evaluation
from django import forms
from .forms import CandForm
from .forms import EvalForm
from django.shortcuts import redirect
from django.db import IntegrityError


def canditate_list(request):
	candidates = Candidate.objects.all()
	
	eva = Evaluation.objects.all()
	eval_cand_list = []										#aqui guarda uma lista com os FK candidates convertidos p/ str

	context = {
		'candidates': candidates,
		'eva': eva
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

    _sum = 0												#variavel que guardara a soma declarada
    for s in scores:
    	_sum += s                                           #faz a soma dos scores

    average = 0	
    if len(scores) > 0:
    	average = _sum/len(scores)								#tira a média

    context = {
    	'candidate': candidate,
    	'average': average
    }
    
    return render(request, 'app/candidate_detail.html', context)


def evaluation(request):
    # form2 initialization
    form2 = EvalForm()

    if request.method == "POST":
        form2 = EvalForm(request.POST)
        if form2.is_valid():    
            post = form2.save(commit=False)
            try:
                post.save()
                return redirect('canditate_list')
            except IntegrityError:
            	return HttpResponse("Você já avaliou este candidato!")
    return render(request, 'app/evaluation.html', {'criterions': form2,})
    

def register(request):
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
	evaluation = Evaluation.objects.all()
	var = []

	cont = 0
	evaluators = []
	for evaluator in evaluation:
		cont = 0
		for e in evaluators:
			if e != evaluator.appraiser:
				cont += 1

		if cont == len(evaluators):
			evaluators += [evaluator.appraiser]


	cont = 0
	candidates = []
	for cand in evaluation:
		cont = 0
		for c in candidates:
			if c != cand.candidate:
				cont += 1

		if cont == len(candidates):
			candidates += [cand.candidate]

	cont = 0		
	context = {
		'evaluators':evaluators,
		'evaluation':evaluation, 
		'var':var,
		'candidates':candidates, 
		'cont':cont,
	}

	return render(request, 'app/grade.html', context)