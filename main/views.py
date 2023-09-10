from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nameApp': 'Inventori App',
        'name': 'Fauzan',
        'class': 'PBP E',
    }

    return render(request, "main.html", context)
