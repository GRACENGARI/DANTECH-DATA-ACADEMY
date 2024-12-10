from django.shortcuts import render,  redirect
from . models import Contact, Student,Organazations,Pictures,Forms



from django.shortcuts import render
def newsletter_subscribe(request):
    if request.method == 'POST':
        # Process the form data here
        email = request.POST.get('email')
        # Add email  database or send confirmation email
        # ...
        return render(request, 'newsletter_success.html')  # Redirect to a success page
    else:
        return render(request, 'newsletter_form.html')

# Create your views here.
def home (request):
    student =  Student.objects.all()
    organazation =Organazations.objects.all()
    context = {
        'student' : student,
        'organazation':organazation
    }
    return render(request,'index.html', context)

#def contact(request):
 #   return render(request, 'contact.html')


def course(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'course.html')

def courses(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'courses.html')

def events(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'events.html')

def about(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'about.html')

def pricing(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'pricing.html')

def starter(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    
    return render(request, 'starter.html')

def trainer(request):
    pictures = Pictures.objects.all()
    context = {
        'pictures':Pictures
        
        
        
      
      
        
    }
    return render(request, 'trainers.html',context)
def newsletterform(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'newsletterform.html')

def  newslettersucess(request):
    forms = Forms.objects.all()
    context ={
        'forms':forms
        
    }
    return render(request, 'newslettersucess.html')





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
