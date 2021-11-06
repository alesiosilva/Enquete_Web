from django.forms import ModelForm
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
#from django.http import HttpResponse
#from django.template import context, loader
from django.urls import reverse

from .models import Choice, Question

# Creating views here.
# ex: /enquete/ 
'''def index(request): 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    
    # Retorno de template e contexto direto no HttpResponse
    template = loader.get_template('enquete/index.html')
    context = {'latest_question_list': latest_question_list}   
    return HttpResponse(template.render(context, request))'''
    
def index(request): 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # Atalho render para retornar o template e contexto
    context = {'latest_question_list': latest_question_list}
    return render(request, 'enquete/index.html', context)

# ex: /enquete/5/
'''def detail(request, question_id):
    # return HttpResponse('You\'re looking at question %s.' % question_id)
    # Resolvendo erro 404 do objeto para o retorno
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist!')
    return render(request, 'enquete/detail.html', {'question': question})'''

def detail(request, question_id):
    # Atalho para retornar diretamente o objeto se não houver erro
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'enquete/detail.html', {'question': question})

# ex: /enquete/5/results
'''def results(request, question_id):
    # Retorno do objeto direto no response
    response = ('You\'re looking at the results of question %s.')
    return HttpResponse(response % question_id)'''

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'enquete/results.html', {'question': question})

def allresults(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'enquete/results.html', context)

# ex: //5/vote
def vote(request, question_id):
    # return HttpResponse('You\'re voting on question %s.' % question_id)'''

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Mostra novamente o formulário de voto
        return render(request, 'enquete/detail.html', {
            'question': question,
            'error_message': "Você não marcou uma escolha válida!",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('enquete:results', args=(question_id,)))

