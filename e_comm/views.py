from django.shortcuts import render

from details.models import book

def home(request):

	d = book.objects.all()
	return render("../templates/home.html",{"details":d})
def details(request,name):

    b = book.objects.filter(title = name)
    return render(request,"../templates/detail.html",{ "book":b})
