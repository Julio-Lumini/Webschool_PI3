import pandas as pd
from django.shortcuts import render, redirect
from .forms import MaterialForm, MerendaForm
from .models import Merenda
from django.http import HttpResponse
import matplotlib.pyplot as plt
from io import BytesIO
import io
import base64


# Create your views here.
def administrativo_home(request):
    return render(request, 'administrativo_home.html')

def cadastro_materiais(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrativo_home')
    else:
        form = MaterialForm()
    return render(request, 'cadastro_materiais.html', {'form': form})

def controle_merenda(request):
    if request.method == 'POST':
        form = MerendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrativo_home')
    else:
        form = MerendaForm()
    return render(request, 'controle_merenda.html', {'form': form})

def importar_merenda(request):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo = request.FILES['arquivo']
        try:
            df = pd.read_excel(arquivo)  # Carregar planilha Excel
            for _, row in df.iterrows():
                Merenda.objects.create(
                    nome=row['Nome'],
                    quantidade=row['Quantidade'],
                    consumo=row.get('Consumo', 0),  # Consumo é opcional
                )
            return redirect('controle_merenda')
        except Exception as e:
            return render(request, 'importar_merenda.html', {'erro': str(e)})
    return render(request, 'importar_merenda.html')

def exportar_merenda(request):
    # Obtenha os dados do modelo Merenda
    merendas = Merenda.objects.all().values('nome', 'quantidade', 'consumo', 'data_entrada')
    
    # Crie um DataFrame a partir dos dados
    df = pd.DataFrame(list(merendas))
    df.rename(columns={
        'nome': 'Nome',
        'quantidade': 'Quantidade',
        'consumo': 'Consumo',
        'data_entrada': 'Data de Entrada'
    }, inplace=True)
    
    # Crie o arquivo Excel na memória
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="relatorio_merenda.xlsx"'
    df.to_excel(response, index=False, engine='openpyxl')
    
    return response

def analise_dados(request):
    if request.method == "GET":
        # Filtrar itens do banco de dados
        itens = Merenda.objects.all()
        return render(request, "analise_dados.html", {"itens": itens})
    
    elif request.method == "POST":
        # Aplicar filtros
        periodo_inicio = request.POST.get("periodo_inicio")
        periodo_fim = request.POST.get("periodo_fim")
        nome_item = request.POST.get("nome_item")
        
        queryset = Merenda.objects.all()

        if periodo_inicio:
            queryset = queryset.filter(data_entrada__gte=periodo_inicio)
        if periodo_fim:
            queryset = queryset.filter(data_entrada__lte=periodo_fim)
        if nome_item:
            queryset = queryset.filter(nome__icontains=nome_item)
        
        # Convertendo para DataFrame Pandas
        data = pd.DataFrame(list(queryset.values()))
        
        # Exibir resultados filtrados
        return render(request, "analise_dados.html", {"data": data.to_dict(orient="records")})

def exportar_grafico(request):
    queryset = Merenda.objects.all()
    data = pd.DataFrame(list(queryset.values()))

    # Gerar gráfico de barras
    plt.figure(figsize=(10, 6))
    data.groupby("nome")["quantidade"].sum().plot(kind="bar", color="skyblue")
    plt.title("Consumo por Item")
    plt.xlabel("Item")
    plt.ylabel("Quantidade")
    
    # Salvar gráfico como imagem
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    return HttpResponse(buffer, content_type="image/png")



def prever_estoque(request):
    queryset = Merenda.objects.all()
    data = pd.DataFrame(list(queryset.values()))

    # Agrupando por data e somando consumo
    data['data_entrada'] = pd.to_datetime(data['data_entrada'])
    consumo_diario = data.groupby('data_entrada')['quantidade'].sum()
    
    # Calculando média móvel simples
    previsao = consumo_diario.rolling(window=3).mean().iloc[-1]
    
    return render(request, "analise_dados.html", {"previsao": previsao})

def analise_merenda(request):
    # Obtendo dados do banco de dados
    merenda = Merenda.objects.all().values()
    df = pd.DataFrame(merenda)

    # Garantindo que o DataFrame contém dados antes de prosseguir
    if df.empty:
        return render(request, 'analise_merenda.html', {"mensagem": "Nenhum dado disponível para análise."})

    # Convertendo campos de data
    df['data_entrada'] = pd.to_datetime(df['data_entrada'])
    df = df.sort_values(by='data_entrada')

    # Análise - Quantidade por Item
    quantidade_por_item = df.groupby('nome')['quantidade'].sum()

    # Criando um gráfico de barras
    plt.figure(figsize=(10, 6))
    quantidade_por_item.plot(kind='bar', color='skyblue')
    plt.title('Quantidade Total por Item')
    plt.xlabel('Item')
    plt.ylabel('Quantidade')

    # Salvando o gráfico como imagem
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    plt.close()

    # Adicionando dados de consumo e estoque
    df['consumo_estimado'] = df['quantidade'] * 0.2  # Exemplo: consumo é 20% da quantidade
    df['estoque_previsto'] = df['quantidade'] - df['consumo_estimado']

    # Preparando os dados para exibição na página
    dados_tabela = df[['nome', 'quantidade', 'data_entrada', 'consumo_estimado', 'estoque_previsto']].to_dict('records')

    return render(request, 'analise_merenda.html', {
        "grafico": graphic,
        "dados_tabela": dados_tabela
    })
