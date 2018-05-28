from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import User, Article
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    #form = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('testapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'testapp/signup.html', {'form':  form})

def parseIt(info, index = 1):
    for i in info:
        print(str(i) + " -- " + str(info[i]))
        print(str(i) + " -- " + str(info[i]), file=open('temp.txt', 'a'))

def index(request):
    context = {}
    parseIt(request.META)
    #print(dir(request))
    #print(dir(request),file = open('tmpall.txt'))
    print(type(request))
    if request.user.is_authenticated:
        context['user'] = request.user
    context['article_list'] = Article.objects.all()[:4]
    #context = {'article_list': article_list}
    return render(request, 'testapp/index.html', context)

def detail(request, article_id):
    context = {'article': get_object_or_404(Article, pk = article_id)}
    return render(request, 'testapp/detail.html', context)

		

