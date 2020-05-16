from django.http import HttpResponse #return a reponse to the user
from django.shortcuts import render
from .models import ToDo

# Create your views here.
#function that will handle the request
def todo_list(request): #request object contains lots of user information
    # return HttpResponse("Hello World")
    todos = ToDo.objects.all()
    print(todos)
    #queryset instances of the model
    #context is a dictionary, python dictionary needs to contain key and value
    context = {
        "todo_list": todos
    }
    return render(request, "todo_list.html", context) 
    #context passing in all of our todos, adding it as context to html file, allow html to access the todos

#CRUD - Create, Retrieve, Update, Delete, List
