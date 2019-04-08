from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.core.files.storage import FileSystemStorage

from .forms import livroEntradaForm,livroSaidaForm
from .models import livroEntrada

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        _file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(_file.name, _file)
        context['url'] = fs.url(name)
        print(context)
    return render(request, 'upload.html',context)


def list_doc_entrada(request):
    entradas = livroEntrada.objects.all()
    return render(request, 'list/list_doc_entrada.html', {
        'entradas' : entradas
    })


def anexar_doc_entrada(request):
    if request.method == 'POST':
        form = livroEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listarEntrada')
    else:
        form = livroEntradaForm()
    return render(request, 'anexar_doc_entrada.html', {
        'form':form
    })
