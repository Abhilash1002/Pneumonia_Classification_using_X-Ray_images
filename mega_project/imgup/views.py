from django.shortcuts import render
from .forms import ImageForm, LoginForm
from .prepro import preprocessing
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.core.mail import send_mail
# Create your views here.
Username = "Admin"
def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Username = name
            password = form.cleaned_data['password']
        if name == "admin" and password =="12345":
            return redirect('../login/')
        else:
            return render(request,'home.html',{'form':form , 'auth':"No"})


    form = LoginForm()
    return render(request,'home.html',{'form':form , 'auth':"NA"})

def login(request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)


        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            send_mail(
            'Classification results',
            'YO',
            'abhilashgudisena@gmail.com',
            [email],
            fail_silently=True,
            )
            print("MAILENTTTTTTTTTTTT")
        else:
            print("MAIL Failed")

        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        res = preprocessing(uploaded_file.name)
        #upload_file_name = uploaded_file.name
        outcome = ""
        if res['outcome'] == [1]:
            outcome = "Pneumonia +ve"
        else:
            outcome = "Pneumonia -ve"
        results = {     'imgName':uploaded_file.name,
                        'predict': outcome,
                        'proba':res['probability'][0][0] , 
                        'imgSize':uploaded_file.size/1024,
                        }
        
        return render(request,'outcome.html',results)

    form = ImageForm()
    return render(request,'login.html',{'form':form, 'uname':Username})
