import requests
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import AllowAny
from .forms import travelgramForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.

#create
class Create(generics.ListCreateAPIView):
    queryset=Travelgram.objects.all()
    serializer_class=travelgramSerializers
    permission_classes=[AllowAny]

class Details(generics.RetrieveAPIView):
    queryset=Travelgram.objects.all()
    serializer_class=travelgramSerializers

class Update(generics.RetrieveUpdateAPIView):
    queryset=Travelgram.objects.all()
    serializer_class=travelgramSerializers

class Delete(generics.DestroyAPIView):
    queryset=Travelgram.objects.all()
    serializer_class=travelgramSerializers

class Search(generics.ListAPIView):
    queryset=Travelgram.objects.all()
    serializer_class=travelgramSerializers

    def get_queryset(self):
        name=self.kwargs.get('place_name')
        return Travelgram.objects.filter(Name__icontains=name)

def create_travel_details(request):
    if request.method=='POST':
        form=travelgramForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                api_url='http://127.0.0.1:8000/create/'
                data=form.cleaned_data
                print(data)

                response=requests.post(api_url, data=data, files={'place_img':request.FILES['place_img']})

                if response.status_code==400:
                    messages.success(request, 'Details inserted successfully')
                else:
                    messages.error(request, f'Error{response.status_code}')

            except requests.RequestException as e:
                messages.error(request, f'Error during API request {str(e)}')

        else:
            messages.error(request, 'Form is not valid')

    else:
        form=travelgramForm()

    return render(request, 'create_travel_details.html', {'form':form})

def delete_travel_details(request, id):
    api_url=f'http://127.0.0.1:8000/delete/{id}'
    response=requests.delete(api_url)

    if response.status_code==200:
        print(f'Item with id{id} has been deleted')
    else:
        print(f'Failed to delete item. status_code {response.status_code}')

    return redirect('/')

def main(request):
    if request.method=='POST':
        search=request.POST['search']

        api_url=f'http://127.0.0.1:8000/search/{search}/'

        try:
            response=request.get(api_url)
            print(response.status_code)

            if response.status_code==200:
                data=request.json()
            else:
                data=None

        except requests.RequestException as e:
            data=None

        return render(request, 'main.html', {'data':data})

    else:
        api_url=f'http://127.0.0.1:8000/create/'

        try:
            response=requests.get(api_url)

            if response.status_code==200:
                data=response.json()
                original_data=data

                paginator=Paginator(original_data, 100)

                try:
                    page=int(request.GET.get('page', 1))

                except:
                    page=1

                try:
                    travel_details=paginator.page(page)

                except(EmptyPage.InvalidPage):
                    travel_details=Paginator.page(paginator.num_pages)

                return render(request, 'main.html', {'original_data':original_data, 'travel_details':travel_details})
            else:
                return render(request, 'main.html', {'error_message':f'Error:{response.status_code}' })

        except requests.RequestException as e:
            return render(request, 'main.html', {'error_message':f'Error:{str(e)}' })

    return render(request, 'main.html')

def travel_details_for_update(request, id):
    api_url = f'http://127.0.0.1:8000/detail/{id}'
    response=requests.get(api_url)

    if response.status_code==200:
        data=response.json()
        description=data['description'].split('.')

    return render(request, 'travel_details_for_update.html', {'travel_details':data, 'description':description})

def update_travel_details(request, id):
    if request.method=='POST':
        place_name=request.POST['Place_name']
        weather=request.POST['Weather']
        location=request.POST['Location']
        map=request.POST.get('Map')
        print('Image Url', request.FILES.get('Place_img'))
        description=request.POST['Description']

        api_url = f'http://127.0.0.1:8000/update/{id}'

        data={
            'place_name':place_name,
            'weather':weather,
            'location':location,
            'map':map,
            'description':description
        }

        files={'Place_img':request.FILES.get('Place_img')}

        response=request.put(api_url, data=data, files=files)

        if response.status_code==200:
            messages.success((request, 'Travel details updated succesfully'))
            return redirect('/')
        else:
            messages.error(request, f'Error submitting data to the REST API:{response.status_code}')

    return render(request, 'update_travel_details.html')

def fetch_travel_details(request, id):
    api_url=f'http://127.0.0.1:8000/detail/{id}'
    response=requests.get(api_url)

    if response.status_code == 200:
        data=response.json()
        description=data['Description'].split(',')
        return render(request, 'fetch_travel_details.html', {'travel_details': data, 'description':description})
    return render(request, 'fetch_travel_details.html')

def users(request):
    if request.method=='POST':
        search=request.POST['search']

        api_url=f'http://127.0.0.1:8000/search/{search}/'

        try:
            response=request.get(api_url)
            print(response.status_code)

            if response.status_code==200:
                data=request.json()
            else:
                data=None

        except requests.RequestException as e:
            data=None

        return render(request, 'users.html', {'data':data})

    else:
        api_url=f'http://127.0.0.1:8000/create/'

        try:
            response=requests.get(api_url)

            if response.status_code==200:
                data=response.json()
                original_data=data

                paginator=Paginator(original_data, 100)

                try:
                    page=int(request.GET.get('page', 1))

                except:
                    page=1

                try:
                    travel_details=paginator.page(page)

                except(EmptyPage.InvalidPage):
                    travel_details=Paginator.page(paginator.num_pages)

                return render(request, 'users.html', {'original_data':original_data, 'travel_details':travel_details})
            else:
                return render(request, 'users.html', {'error_message':f'Error:{response.status_code}' })

        except requests.RequestException as e:
            return render(request, 'users.html', {'error_message':f'Error:{str(e)}' })

    return render(request, 'users.html')

def image_view(request, id):
    api_url=f'http://127.0.0.1:8000/detail/{id}'
    response=requests.get(api_url)

    if response.status_code == 200:
        data=response.json()
        return render(request, 'image_view.html', {'travel_details': data})
    return render(request, 'image_view.html')

def help(request):

    return render(request, 'help_page.html')


