from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .models import Customer
from .models import ImageUploader
from django.http import HttpResponseRedirect
from .models import Property
# Create your views here.
def index(request):
    properties = Property.objects.all()
    name=request.session.get('name')
    if name is not None:
        return render(request, 'index.html',{'name':name})
    else:
        return render(request,'login.html')

def contact(request):
        return render(request, 'contact.html')

def properties(request):
    name=request.session.get('name')
    if name is not None:
        return render(request, 'properties.html',{'name':name})
    else:
        return render(request,'login.html')

def properties_details(request):
    name=request.session.get('name')
    if name is not None:
        return render(request, 'property-details.html',{'name':name})
    else:
        return render(request,'login.html')

def registration(request):
    if request.method == "POST":
        cname = request.POST.get("cname")
        cadd = request.POST.get("cadd")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        unm = request.POST.get("unm")
        pw = request.POST.get("pw")
        cust=Customer(cname=cname,cadd=cadd,email=email,phone=phone,unm=unm,pw=pw)
        cust.save()
        return render(request, 'login.html')
    else:
        return render(request, "registration.html")

def login(request):
    request.session.flush()
    if request.method == "POST":
        unm = request.POST.get("unm")
        pw = request.POST.get("pw")
        try:
            data=Customer.objects.get(pw=pw)
            request.session['name']=unm
            request.session['data']=data.id
            return redirect('/')
        except Exception:
            return render(request,'login.html')
    else:
        return render(request, "login.html")
    
    
def image_upload(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        image_uploader_obj = ImageUploader()
        image_uploader_obj.photo = request.FILES['image']
        image_uploader_obj.save()

    all_images = ImageUploader.objects.all()

    return render(request = request, template_name="image_upload.html", context = {'img': all_images})

def delete_image(request, image_id):
    if request.method == 'POST':
        obj = ImageUploader.objects.get(pk = image_id)
        obj.delete()
        # In HttpResponseRedirect take the 'route' of the urls
        return HttpResponseRedirect(redirect_to='/images')