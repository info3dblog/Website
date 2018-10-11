from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("""<h1>Info3DBlog</h1><p>This is a text to test</p>""")

