from django.shortcuts import render
from .models import StudentRegistration
# Create your views here.
def student_register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        date_of_birth=request.POST.get('date_of_birth')
        qualification=request.POST.get('qualification')
        passing_year=request.POST.get('passing_year')
        email=request.POST.get('email')
        password=request.POST.get('password')
        student=StudentRegistration(name=name,contact=contact,date_of_birth=date_of_birth,qualification=qualification,
                            passing_year=passing_year,emil=email,password=password)
        student.save()
        message='successfully registration'
        return render(request,'registration.html',{'mesage':message})
    else:
        return render(request, 'registration.html')


def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        login=StudentRegistration.objects.filter(emil=email,password=password)
        if login:
            type='home'
            return render(request,'home.html',{'type':type})
    else:
        return render(request,'student_login.html')
    message = 'invalid email or password'
    return render(request,'student_login.html',{'mesage':message})


def Hr_list(request):
    type='hr_list'
    student=StudentRegistration.objects.all()
    return render(request,'home.html',{'type':type,'students':student})


def Notification(request):
    type='notification'
    students=StudentRegistration.objects.all()
    for student in students:
        statu=student.qualification
        status= statu =='ACtive'
    return render(request,'home.html',{'type':type,'student':students,'status':status})


def hr_datails(request):
    type='hr_datails'
    id = request.GET.get("hr_id")
    stu=StudentRegistration.objects.filter(id=id)
    for x in stu:
        name=x.name
        address=x.contact
    return render(request,'home.html',{'type':type,'name':name,'address':address})