from django.shortcuts import render,  redirect
from . models import Contact
# Create your views here.
def home (request):
    return render(request,'index.html')

#def contact(request):
 #   return render(request, 'contact.html')


def course(request):
    return render(request, 'course.html')

def courses(request):
    return render(request, 'courses.html')

def events(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def starter(request):
    return render(request, 'starter.html')

def trainers(request):
    return render(request, 'trainers.html')




def contact(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')

       contact = Contact(name=name, email=email, subject=subject, message=message)
       contact.save()

       return redirect('index')  # Redirect to the index page after saving the contact

    return render(request, 'index.html')
    

    return redirect('index')  # Redirect to the index page after saving the contact

    return render(request, 'index.html')
# Create your views here.


# Create your views here.
