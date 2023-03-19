from django.shortcuts import render,redirect
from .models import pets
# Create your views here.
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')

def upload(request):
    if request.method == 'POST':
        idno = request.POST['idno']
        name = request.POST['name']
        parent = request.POST['parent']
        type = request.POST['type']
        age = request.POST['age']
        gender = request.POST['gender']
        i= pets(idno=idno,name=name,parent = parent, type= type, age=age, gender=gender)
        i.save()
        return redirect('dashboard')
    return render(request,'upload.html')

def dashboard(request):
        pet = pets.objects.all()
        return render(request,'dashboard.html',{'pet':pet})

def delete(request, id):
    if request.method == 'POST':
        pets.objects.get(id=id).delete()
    return redirect('dashboard')

def update(request, id):
    if request.method == 'POST':
        idno = request.POST.get('idno',False)
        name = request.POST.get('name',False)
        parent = request.POST.get('parent',False)
        type = request.POST.get('type',False)
        age = request.POST.get('age',False)
        gender = request.POST.get('gender',False)
        pets.objects.filter(id=id).update(idno = idno,name = name,parent = parent, type = type, age = age, gender = gender)
        return render(request,'update.html')
    return redirect('dashboard')