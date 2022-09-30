from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# ne11mU1MzaY43tX8zsPF2w==C9IJUTIRRqjMHtBl
def index(request):
    context={
        'veriable':"this is a string veriable",
        'x':'4'
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Message has been sent!')
    return render(request, 'contact.html')

def services(request):
    #API NINJAS: https://api-ninjas.com/api/recipe
    import requests 
    if request.method == 'POST':
        que = request.POST.get('query')
        api_url = 'https://api.api-ninjas.com/v1/recipe?query='
        res = requests.get(api_url + que, headers={'X-Api-Key': 'ne11mU1MzaY43tX8zsPF2w==C9IJUTIRRqjMHtBl'}).json()
        print(res)
        return render(request,'services.html',{'response':res,'que':que})
    else:
        return render(request,'services.html')  
   