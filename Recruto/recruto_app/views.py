from django.shortcuts import render

def home(request):
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    context = {'name': name, 'message': message}
    return render(request, 'home.html', context)
