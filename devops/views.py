from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from devops.models import Student, Track
from devops.forms import studentform, trackform

# Create your views here.
def home(request):
    return HttpResponse("<h1> welcome to my website this create by aya rabih  </h1>") 

def getStudent(request, st_id):
    st = Student.objects.get(id = st_id)
    context = {'student': st}
    return render(request, 'devops/student_detiails.html', context)

def getALLStudents(request):
    all_students = Student.objects.all()
    context = {'students': all_students}
    return render(request,"devops/students.html", context)
    
def newStudent(request):
    st_form = studentform()
    if request.method == 'POST':
        st_form = studentform(request.POST)
        if st_form.is_valid():
            st_form.save()
            return HttpResponseRedirect('/devops/all')
        
    context = {'student_form': st_form}
    return render(request,"devops/new_student.html", context)

def editstudent(request, st_id):
    st = Student.objects.get(id= st_id)
    st_form = studentform(instance= st)
    if request.method == 'POST':
        st_form = studentform(request.POST, instance=st)
        if st_form.is_valid():
            st_form.save()
            return HttpResponseRedirect('/devops/all')
    context = {'student_form': st_form}
    return render(request,"devops/new_student.html", context)
def deletestudent(request, st_id):
    student = Student.objects.get(id= st_id)
    student.delete()
    return HttpResponseRedirect('/devops/all')

