from django.shortcuts import render
from .forms import AlunoForm    
from .models import Aluno




# Create your views here.

def cadastro_aluno(request):
     form = AlunoForm()  # Crie uma instância do formulário
     if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
              # Aqui você pode processar os dados do formulário
            # Por exemplo, salvar no banco de dados
            pass  # Remova isso quando adicionar o processamento real
     else:
        form = AlunoForm()

     context = {
        'form': form
    }
     return render(request, 'matricula/form.html', context)


