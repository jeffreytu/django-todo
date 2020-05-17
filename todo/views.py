from django.http import HttpResponse #return a reponse to the user
from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm

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
def todo_detail(request, id):
    todo = ToDo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_detail.html", context)

def todo_create(request):
    form = ToDoForm(request.POST or None) #form will be populated if there is a POST request and not a get request (None)
    
    if form.is_valid(): #check that every field is passed correct data format, name and due_date
        #create a todo object
        # name = form.cleaned_data['name'] #cleaned_data method to check that it passes model requirements
        # due_date = form.cleaned_data['due_date']
        # new_todo = ToDo.objects.create(name=name, due_date=due_date)

        form.save() #all of what was done above can be called with this
        return redirect('/') #django shortcut to direct back to list view
    context = {"form": form} #context is required. calling form will allow django to build the input forms automatically
    return render(request, "todo_create.html", context)

def todo_update(request, id):
    todo = ToDo.objects.get(id=id)
    form = ToDoForm(request.POST or None, instance=todo) #pass in data of todo object, pass object into form to pre-populate
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form} #context is required. calling form will allow django to build the input forms automatically
    return render(request, "todo_update.html", context)

def todo_delete(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('/')