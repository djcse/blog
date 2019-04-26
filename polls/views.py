from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader, RequestContext

from .models import Question

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
	return HttpResponse("This is the details of ques. no: %s" % question_id)

def results(request, question_id):
	return HttpResponse("These are results of the q no: %s" % question_id)

def vote(request, question_id):
	return HttpResponse("Vote on question: %s" % question_id)