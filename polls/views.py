from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.template import loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question
from .forms import PollForm,ChoiceFill,ChoiceForm

def index(request):
	# print("latest_questions")
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	# print(latest_questions)
	template = loader.get_template('blog.html')
	context = RequestContext(request, {
		'latest_questions' : latest_questions
	})
	return render(request, 'post.html', context)


def details(request, question_id):
	# API CALL from remote server
	#question = Question.objects.get(pk = question_id)
	return HttpResponse("This is the details of ques. no: %s" % question_id)
	#return render(request,'templates/sidebar.html',{'question':question})

def results(request, question_id):
	return HttpResponse("These are results of the q no: %s" % question_id)

def cast_vote(request, question_id):
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	question = Question.objects.get(pk = question_id)
	try:
		selected_choice = question.q_choice.get(pk=request.POST['choice'])
	except:
		return redirect('post-list')
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return redirect('post-list')
	#return render(request, 'post.html', context)

class QuestionCreateView(CreateView):
	model = Question
	template_name = 'question_create.html'
	form_class = PollForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create'
		return context

	def form_valid(self, form):
		newQuestion = form.save()
		print("This is the new QS ID = ", newQuestion.pk)
		question = Question.objects.get(pk=newQuestion.pk)
		print(question.question_text)
		return redirect('choice-create',question_id = newQuestion.pk)

def question_create(request):
	title = 'Create'
	form = PollForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {
		'title': title,
		'form': form
	}
	return render(request.POST, "question_create.html", context)

def choice_create(request,question_id):
	question = Question.objects.get(pk=question_id)

	form = None

	if len(question.q_choice.all()) == 0:
		for i in range(question.number_of_choices):
			question.q_choice.create(choice_text="default_" + str(i))
	else:
		for i in range(question.number_of_choices):
			print(question.q_choice)

	form = ChoiceFill(request.POST or None,{'nchoice':question.number_of_choices})

	if request.method == "POST":
		if form.is_valid():
			print(form.cleaned_data)
			i = 0
			for ch in question.q_choice.all():
				#ch.update(choice_text=form.cleaned_data['choice'+str(i)])
				ch.choice_text = form.cleaned_data['choice'+str(i)]
				i += 1
				ch.save()
			return redirect("post-list")

	context = {
		'form': form,
		'question': question
	}

	return render(request, "choice_create.html", context)