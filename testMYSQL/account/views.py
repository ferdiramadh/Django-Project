from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all':all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lastname = request.POST['lastname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']

            messages.success(request, 'There was an error on your forms. Please try again...')
            return render(request, 'join.html',
            {
                'fname': fname,
                'lastname': lastname,
                'age': age,
                'email': email,
                'passwd': passwd,

            })
        messages.success(request, ('Your Forms has been submitted successfully!'))
        return redirect('home')
    else:
        return render(request, 'join.html', {})
