from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	dic = {}
	return render(request,'generator/home.html',dic)

def password(request):
	dic = {}
	dic['password'] = "mypassword"
	characters = list('abcdefghijklmnopwx')

	length = int(request.GET.get('length'))

	if(request.GET.get('uppercase')):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTWXYZ'))
	if(request.GET.get('numbers')):
		characters.extend(list('1234567890'))
	if(request.GET.get('special')):
		characters.extend(list('{}[]()_+-=,.?/`~'))

	password = ""


	for x in range(length):
		password += random.choice(characters)
	dic['password'] = password

	return render(request,'generator/password.html',dic)

