from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm,UserExpensesForm,CategoryForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserExpenses
# Create your views here.



def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'user sucessfully created')

            return redirect('login')
        else:
            messages.success(request,'something went wrong ')
    else:
        form = SignUpForm()
    return render(request,'login_register.html', {'form': form,'data':'register'})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('expenses')
            else:

                messages.error(request, "invalid credentials")
        else:
            messages.error(request, "error validating form")
    return render(request, 'login_register.html', {'form': form})
@login_required(login_url='login')
def UserExpensesList(request):
    form=CategoryForm()
    profile =request.user
    if profile.is_admin:
        if request.method=='POST':
            expobj=UserExpenses.objects.filter(Category=request.POST['Category'])
        else:
            expobj=UserExpenses.objects.all()
    else:
        if request.method=='POST':
            expobj=profile.expenses.filter(Category=request.POST['Category'])
        else:
            expobj=profile.expenses.all()
    return render(request,'expenses.html',{'expenses':expobj,'form':form})

@login_required(login_url='login')
def logoutUser(request):
    
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def CreateExpense(request):
    # if request.is_admin:
    #     return redirect('expenses')
    profile=request.user
    form=UserExpensesForm()
    if request.method=='POST':
        form=UserExpensesForm(request.POST,request.FILES)
        if form.is_valid():
            expense=form.save(commit=False)
            expense.owner=profile
            expense.save()
            return redirect('expenses')
        
    content ={'form':form}
    return render (request,'expense_form.html',content)

@login_required(login_url='login')
def updateExpense(request,pk):
    profile =request.user
    expense=profile.expenses.get(id=pk)
    form=UserExpensesForm(instance=expense)
    if request.method=='POST':
        form=UserExpensesForm(request.POST,request.FILES,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    content ={'form':form}
    return render (request,'expense_form.html',content)
@login_required(login_url='login')
def deleteExpense(request,pk):
    profile =request.user
    expense=profile.expenses.get(id=pk)
    if request.method=="POST":
        expense.delete()
        return redirect('expenses')
    content ={'object':expense}
    return render (request,'delete_form.html',content)
