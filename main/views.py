from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406344675',
        'name': 'Rafa Rally Soelistiono',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)