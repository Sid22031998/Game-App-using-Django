from django.shortcuts import render

def index(request):
	return render(request, 'Game/index.html')

def snake(request):
	return render(request, 'Game/snake.html')

def ColorGame(request):
	return render(request, 'Game/colorGame.html')