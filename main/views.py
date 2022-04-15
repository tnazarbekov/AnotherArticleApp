from django.shortcuts import render


def home(request):
    context = {

    }
    return render(request, 'main/home_index.html')


def about(request):
    return render(request, 'main/aboutus_page.html')


def contacts(request):
    return render(request, 'main/contacts_page.html')

def pashalka(request):
    return render(request,'main/pashalka.html')
