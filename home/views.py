import datetime
import io
import PyPDF4
import pyttsx3
from datetime import date
from django.shortcuts import render,redirect
import urllib.request
import cv2
import numpy as np
from django.http import HttpResponse
import django.core.files
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render(request,'home/index.html')
def listen(request):
    if request.method=='POST' and request.FILES['file']:
        file=request.FILES['file'].read()
        if ".pdf" not in request.FILES['file'].name:
            messages.warning(request,"upload only pdfs")
        else:
            if file:
                filereader=PyPDF4.PdfFileReader(io.BytesIO(file))
                content=''
                total=filereader.getNumPages()
                for i in range(total):
                    content+=filereader.getPage(i).extractText()+"\n"
                if content.strip():
                    engine=pyttsx3.init()
                    p=content.split('.')
                    for i in p:
                        engine.say(i)
                        if "stop" in request.POST:
                            engine.stop()
                            break
                    try:
                        engine.runAndWait()
                    except:
                        pass
                else:
                    messages.warning(request,'enter valid pdf')
    form=uploadForm()
    return render(request,'home/listen.html',{'form':form})

def explore(request):
    form = Application.objects.all()
    return render(request,'home/explore.html',{'form':form})
def add(request):
    if request.method=='POST':
        for i,j in request.POST.items():
            if i=='enddate':
                crctdate=datetime.datetime.strptime(j,'%Y-%m-%d').date()
                print("application date is ",j)
                print("todays date is ",date.today()>crctdate)
        reform = ApplicationForm(request.POST)
        user=reform.save()
        return redirect('/')
    form=ApplicationForm()
    return render(request,'home/add.html',{'form':form})
def delete(request,pk):
    item=Application.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    content={'item':item}
    return render(request,'home/delete.html',content)
def edit(request,pk):
    item=Application.objects.get(id=pk)
    form=ApplicationForm(instance=item)
    if request.method=='POST':
        form=ApplicationForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/explore')
    content={'form':form}
    return render(request,'home/edit.html',content)
def project(request):
    if request.method=="POST":
        val=request.POST.get("keyword","")
        url = "https://unsplash.com/s/photos/" + val
        text = urllib.request.urlopen(url)
        file = text.read()
        decoded = file.decode()
        corpus = set()
        filter = ''
        index = 0
        end = 0
        l = decoded.count("img")
        def url_to_img(url):
            resp = urllib.request.urlopen(url)
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            return image
        leng = len(decoded)
        for i in range(l):
            index = decoded.find(r"img", end, leng)
            src = decoded.find(r"src=", index, leng)
            end = decoded.find('\"', src + 5, leng)
            filter += decoded[src + 5:end:]
            corpus.add(filter)
            filter = ''
        count = 0
        for i in list(corpus):
            try:
                image = url_to_img(i)
            except:
                continue
            if image is not None:
                text =val + str(count) + ".jpg"
                cv2.imwrite(text, image)
                count += 1
        return redirect('/')
    return render(request,'home/project.html')
