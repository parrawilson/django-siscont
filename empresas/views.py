from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.urls import reverse
from .forms import EmpresaForm
from .models import Empresa
from django.views.decorators.http import require_POST


def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/lista.html', {'empresas': empresas})



def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            if request.headers.get('HX-Request'):
                response = HttpResponse(status=204)
                response['HX-Redirect'] = reverse('lista_empresas')
                return response
            return redirect('lista_empresas')
    else:
        form = EmpresaForm(instance=empresa)

    template = 'empresas/partials/empresa_form.html' if request.headers.get('HX-Request') else 'empresas/editar.html'
    return render(request, template, {'form': form, 'empresa': empresa})


def eliminar_empresa(request, empresa_id):
    if request.method == 'POST':
        empresa = get_object_or_404(Empresa, id=empresa_id)
        empresa.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        else:
            return redirect('lista_empresas')
    return HttpResponseNotAllowed(['POST'])

def registrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')  # Asegúrate de que esta URL exista
    else:
        form = EmpresaForm()

    return render(request, 'empresas/formulario.html', {
        'form': form,
        'modo': 'registrar',
        'titulo': 'Registrar Empresa',
    })


def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresas')
    else:
        form = EmpresaForm(instance=empresa)

    return render(request, 'empresas/formulario.html', {
        'form': form,
        'modo': 'editar',
        'titulo': 'Editar Empresa',
        'empresa': empresa,
    })

def seleccionar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    request.session['empresa_id'] = empresa.id
    request.session['empresa_nombre'] = empresa.nombre
    return redirect('dashboard2')  # O donde quieras redirigir después de seleccionar

