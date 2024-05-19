from web.forms import LoginForm
from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
    context = {}
    if request.method == "GET":
        context['login'] = LoginForm()
    else:
        form = LoginForm(request.POST)
        context['login'] = form
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            print("-----------")
            print(usuario)
            return redirect('bienvenido', usuario=usuario)
    return render(request, 'web/index.html', context)