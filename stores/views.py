from django.shortcuts import render , redirect ,HttpResponseRedirect
from .models import books
from .form import CreatestoreForm,CreatebooksForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from .form import SignUpForm
from django.contrib.auth import authenticate , login ,logout 

def home(request):
	book = books.objects.all()
	form = CreatestoreForm()
	bookform = CreatebooksForm()
	return render(request,'home.html',{'book':book,'form':form,'bookform':bookform})

def create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
		    form = CreatestoreForm(request.POST)
		    if form.is_valid():
		        form.save()
		        return redirect('/createbook')
		else:
		    form = CreatestoreForm()

		return render(request, 'create.html', {'create':form,'datas':request.user})
	else:
		return HttpResponseRedirect('/login')


def signup(request):
	if request.method == 'POST':
	    form = SignUpForm(request.POST)
	    if form.is_valid():
	        form.save()
	        return redirect('/login')

	    else:
	    	return render(request, 'signup.html',{'form':form})

	else:
		form = SignUpForm()	    	
		return render(request, 'signup.html',{'form':form})

def logins(request):
	if request.method=='POST':
		usr = AuthenticationForm(request=request,data=request.POST)
		if usr.is_valid():
			user = usr.cleaned_data['username']
			pasw = usr.cleaned_data['password']
			data=authenticate(username=user,password=pasw)
			if data is not None:
				login(request,data)
				print(data)
				return redirect('/create')
			else:
				return render(request,'login.html',{'form':usr})

		else:
				return render(request,'login.html',{'form':usr})



	else:
		fm = AuthenticationForm()
		return render(request,'login.html',{'form':fm})

def logouts(request):
	logout(request)
	return HttpResponseRedirect('/login')




def createbook(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = CreatebooksForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/home')
		else:
			form = CreatebooksForm()
		return render(request,'user.html',{'create':form})
	else:
		return HttpResponseRedirect('/login')



def update(request,pk):
	data = books.objects.get(id=pk)
	form = CreatebooksForm(instance=data)

	if request.method == 'POST':
		data = CreatebooksForm(request.POST,instance=data)
		if data.is_valid:
			data.save()
			return redirect('/home')

	return render(request,'update.html',{'form':form})


def deletes(request,pk):
	data = books.objects.get(id=pk)
	form = CreatebooksForm(instance=data)

	if request.method == 'POST':
		dataa = CreatebooksForm(request.POST,instance=data)
		data.delete()
		return redirect('/home')

	return render(request,'delete.html',{'form':form})





