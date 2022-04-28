# VERSÃO FINAL - ÚNICA - V1.0
# ALTERADA EM 03/04 -- 18:30


# EXPORTAÇÕES:
import plotly.express as px
from pandas import read_excel
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


# DECLARAÇÃO DO 1º DATAFRAME:
df1 = read_excel("https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Brasil-Exportacao_cafe_por_pais.xlsx?raw=true")

# DECLARAÇÃO DO 2º DATAFRAME:
df2 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/UnidadesReceita.xlsx?raw=true')

# DECLARAÇÃO DO 3º DATAFRAME:
df3 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Preco_Medio.xlsx?raw=true')

# DECLARAÇÃO DO 4º DATAFRAME:
df4 = read_excel('https://github.com/Trabalho-APC-DASH/Painel-APC/blob/main/Banco%20de%20Dados/Paises_exportadores_cafe.xlsx?raw=true')



# INÍCIO A ORGANIZAÇÃO DE DADOS:
# =========================================================================
# DATAFRAME 1)

# ORGANIZAÇÃO DAS OPÇÕES PARA O DROPDOWN:
def funcao_unique(lista):

    resultado = []

    unicidade = set(lista)

    for elemento in unicidade:
        resultado.append(elemento)

    return resultado

opcoes = funcao_unique(df1['CONTINENTE'])

opcoes.insert(0, 'Todos os Continentes')
del opcoes[1]
opcoes2 = ['ARÁBICA (Por sacas de 60kg)', 'CONILLON (Por sacas de 60kg)', 'SOLÚVEL (Por sacas de 60kg)', 'TORRADO (Por sacas de 60kg)', 'TOTAL']

# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig1 = px.bar(df1, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", title='Compra de Café Brasileiro por País')

# ===========================================================================
# DATAFRAME 2)

# TRANSFORMAÇÃO DO DF2 PARA UMA LISTA MODIFICÁVEL:
lista = df2.values

# DECLARAÇÃO DO DATAFRAME OFICIAL DO DF2:
dfOf1 = []

# REORGANIZAÇÃO DO DF2:
for n in lista:
    dfOf1 += [[n[0], n[1], 'Importação Jan/Fev2022']]
    dfOf1 += [[n[0], n[3], 'Exportação Jan/Fev2022']]
    dfOf1 += [[n[0], n[5], 'Importação Jan/Fev2021']]
    dfOf1 += [[n[0], n[7], 'Exportação Jan/Fev2021']]


# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig2 = px.bar(dfOf1, x=0, y=1, color=2, barmode="group", title='Exportação/Importação por Receita Federal', labels={
             '0': 'Unidade Da Receita Federal',
             '1': 'Sacas (60kg)',
             '2': 'Tipo'
            })

fig2.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0.2)',
        font_color='white',
    )

receita_filtragem = []
for n in lista:
    receita_filtragem += [n[0]]

receita_filtragem.insert(0, 'Todos')
# ============================================================================
# DATAFRAME 3)


# MEMORIZAÇÃO DAS COLUNAS DA PRIMEIRA LINHA PRESENTE NO DATAFRAME 3:
opcoes3 = []
for n in df3:
    opcoes3 += [n]

# EXCLUSÃO DE DADOS DESNECESSÁRIOS PARA EXIBIÇÃO NO GRÁFICO:
del opcoes3[0]
del opcoes3[6]

# DECLARAÇÃO PRIMÁRIA DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig3 = go.Figure()

for cafe in opcoes3:
    fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3[cafe],
                        mode='lines', name=cafe))

# ATUALIZAÇÃO DE TÍTULO E NOMEAÇÃO DA PARTE VERTICAL DO GRÁFICO E HORIZONTAL:
fig3.update_layout(title='Preço Médio do Café Brasileiro',
                   xaxis_title='Ano',
                   yaxis_title='Preço (US$)')

# INSERÇÃO DE UMA NOVA OPÇÃO PARA O DROPDOWN:
opcoes3.insert(0, 'Todos os Tipos de Café')

# ==============================================================================
# DATAFRAME 4)

# TRANSFORMAÇÃO DO DF4 PARA UMA LISTA MODIFICÁVEL:
Lista3 = df4.values

# LISTA DE TODOS OS PAÍSES DIVIDIDO POR CONTINENTES PARA SER UTILIZADO NO PASSSO MAIS ABAIXO:
Oceania = ['Estados Federados da Micronésia', 'Fiji', 'Ilhas Marshall', 'Ilhas Salomão', 'Kiribati' ,'Nauru', 'Nova Zelândia', 'Palau', 'Papua-Nova Guiné', 'Samoa', 'Tonga', 'Tuvalu', 'Vanuatu', 'Ilhas Cook']
América_do_Norte = ['Canadá', 'Estados Unidos da América', 'México']
América_Central = ['Antígua e Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Costa Rica', 'Cuba', 'Dominica', 'El Salvador', 'Granada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Nicarágua', 'Panamá', 'República Dominicana', 'Santa Lúcia', 'São Cristóvão e Névis', 'São Vicente e Granadinas', 'Trindade e Tobago']
América_do_Sul = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Guiana Francesa', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela']
Europa = ['Albânia', 'Alemanha', 'Andorra', 'Áustria', 'Bélgica', 'Bielorrússia', 'Bósnia e Herzegovina', 'Bulgária', 'Cazaquistão', 'Chipre', 'Croácia', 'Dinamarca', 'Eslováquia', 'Eslovênia', 'Espanha', 'Estônia', 'Finlândia', 'França', 'Grécia', 'Hungria', 'Irlanda', 'Islândia', 'Itália', 'Letônia', 'Liechtenstein', 'Lituânia', 'Luxemburgo', 'Malta', 'Moldávia', 'Mônaco', 'Montenegro', 'Noruega', 'Países Baixos', 'Polônia', 'Portugal', 'Tchéquia', 'Macedônia do Norte', 'Inglaterra', 'Irlanda do Norte', 'Escócia', 'País de Gales', 'Romênia', 'Rússia', 'San Marino', 'Sérvia', 'Suécia', 'Suíça', 'Turquia', 'Ucrânia', 'Vaticano']
Ásia = ['Timor Leste', 'Birmânia', 'Afeganistão', 'Arábia Saudita', 'Armênia', 'Azerbaijão', 'Bahrein', 'Bangladesh', 'Brunei', 'Butão', 'Camboja', 'Cazaquistão', 'Catar', 'China', 'Chipre', 'Cingapura', 'Coreia do Norte', 'Coreia do Sul', 'Egito', 'Emirados Árabes', 'Filipinas', 'Geórgia', 'Iêmen', 'Índia', 'Indonésia', 'Irã', 'Iraque', 'Israel', 'Japão', 'Jordânia', 'Kuwait', 'Laos', 'Líbano', 'Malásia', 'Maldivas', 'Mianmar', 'Mongólia', 'Nepal', 'Omã', 'Paquistão', 'Quirguistão', 'Rússia', 'Síria', 'Sri Lanka', 'Tajiquistão', 'Tailândia', 'Timor-Leste', 'Turcomenistão', 'Turquia', 'Uzbequistão', 'Vietnã', 'Taiwan', 'República Popular da China']
África = ['África do Sul', 'Angola', 'Argélia', 'Benim', 'Botswana', 'Burquina Faso', 'Burundi', 'Camarões', 'Chade', 'Costa do Marfim', 'Djibouti', 'Egito', 'Eritreia', 'Etiópia', 'Gabão', 'Gâmbia', 'Gana', 'Guiné', 'Guiné-Bissau', 'Guiné Equatorial', 'Madagáscar', 'Cabo Verde', 'Comores', 'São Tomé e Príncipe', 'Seychelles', 'Lesoto', 'Libéria', 'Líbia', 'Malawi', 'Mali', 'Marrocos', 'Mauritânia', 'Moçambique', 'Namíbia', 'Níger', 'Nigéria', 'Quênia', 'República da África Central', 'República Democrática do Congo', 'República do Congo', 'República de Maurício', 'Ruanda', 'Senegal', 'Serra Leoa', 'Somália', 'Eswatini', 'Sudão', 'Sudão do Sul', 'Tanzânia', 'Togo', 'Tunísia', 'Uganda', 'Zâmbia', 'Zimbábue', 'República Popular do Congo']

# DECLARAÇÃO DO DATAFRAME OFICIAL DO DF4:
dfOf3 = []

# INÍCIO DE REPETIÇÃO PARA CADA ELEMENTO DA LISTA "ListaDeFiltro"
for ln in Lista3:
    for cont in Oceania: # INÍCIO DE REPETIÇÃO PARA CADA ELEMENTO DA LISTA "Oceania"

        if ln[1] == cont: # CASO O PAÍS DA LISTA DE FILTRO SE ENCONTRE NA DA OCEANIA, SEU CONTINENTE SERÁ OCEANIA.
            dfOf3 += [[ln[0], ln[1], ln[2],'Oceania']]

    for cont in América_do_Norte: # INÍCIO DE REPETIÇÃO PARA CADA ELEMENTO DA LISTA "América_Do_Norte"

        if ln[1] == cont: # CASO O PAÍS DA LISTA DE FILTRO SE ENCONTRE NA AMÉRICA DO NORTE, SEU CONTINENTE SERÁ AMÉRICA DO NORTE.
            dfOf3 += [[ln[0], ln[1], ln[2], 'América do Norte']]

    for cont in América_Central: # MESMA LÓGICA DOS PASSOS ANTERIORES...
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'América Central']]

    for cont in América_do_Sul:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'América do Sul']]

    for cont in Europa:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'Europa']]

    for cont in Ásia:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'Ásia']]

    for cont in África:
        if ln[1] == cont:
            dfOf3 += [[ln[0], ln[1], ln[2], 'África']]


# DECLARAÇÃO DE COMO O GRÁFICO IRÁ SER ORGANIZADO:
fig4 = px.scatter_geo(dfOf3, # Definição do DataFrame a ser utilizado
                         title= 'Produção de Café Anual (Toneladas)',
                         locations= 0, # As localizações se darão da coluna 0 do DataFrame, que são os ID's
                         projection= 'orthographic', # Projeção do mapa no tipo Ortográfica
                         opacity= 1, # Definição da opacidade das bolinhas no mapa
                         hover_name= 1, # Dado de Nome, que foi definido pela coluna 1 do DataFrame, que é os Países
                         color= 3, # Definição da separação de cores, definida pela coluna 3 do DataFrame, que são os continentes                         
                         hover_data=[2], # Definição de Acrescimo de informação, neste caso a coluna 2 esta sendo acrescentada nos dados do mapa, que são as Produções
                         labels={'3':'Continente', '0':'País ID', "2":'Produção'} # Renomeação dos tópicos no mapa, para que seja melhor interpretado
)

fig4.update_geos(
    landcolor="#06832F",
    oceancolor="#1E8AC9",
    showocean=True,
    lakecolor="#5FC4D0",
)

fig4.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0.2)',
        font_color='white',
    )
# =======================================================================================
# INÍCIO PARA EXECUÇÃO DO LAYOUT E INSERÇÃO DOS GRÁFICOS:


# CONEXÃO DO APP COM O FRAMEWORK BOOTSTRAP:
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# ---------------------------------------------------------------------------------------
# CRIAÇÃO EM PARTES DO SITE:

    # A) BARRA LATERAL:


# DEFINIÇÕES DE ESTILO PARA A BARRA LATERAL
ESTILO_BARRA_LATERAL = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "rgba(221, 162, 99, 0)",
}

# INTENS A SEREM UTILIZADO NA BARRA LATERAL:
items = [
    dbc.DropdownMenuItem("Gráfico 1", n_clicks=0, id='Drop1'),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Gŕafico 2", n_clicks=0, id='Drop2'),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Gráfico 3", n_clicks=0, id='Drop3'),
]

# DEFINIÇÃO DA BARRA LARETAL:
barralateral = html.Div(
    [   # TEXTOS:
        html.H2("Café☕", className="display-4", style={'color': 'white'}),
        html.Hr(),
        html.P(
            'Confira o movimento de mercado do Café Brasileiro', className="lead", style={'color': 'white'}
        ),
        # ÁREA DE NAVEGAÇÃO:
        dbc.Nav(
            [
                # INSERÇÃO DO DROOPDOWN:
                dbc.DropdownMenu(
                label="FIltros", children=items, direction="down"
                ),


                html.Hr(),

                html.P('INFO:', style={'color': 'white', 'margin-top': '2vh'}),

                # DEMAIS OPÇÕES (QUE SERÃO OS INFO DE CADA GRÁFICO):
                dbc.NavLink("Exportações", href="/page-1", id='menu1'),
                dbc.NavLink("Compra", href="/page2", id='menu2'),
                dbc.NavLink("Preços", href="/page-4", id='menu3'),
                dbc.NavLink("Produções", href="/page-5", id='menu4'),

                # ÁREA PARA ACESSO AOS DESENVOLVEDORES:
                html.P('DESENVOLVEDORES:', style={'color': 'white', 'margin-top': '3vh'}),

                html.A('Acesse Aqui', href='Desenvolvedores.html', className='link', target='_Blank'),

                html.Div([
        
                    # IMAGEM LOGO DA UNB:
                    html.Img(src='./assets/logo.png', width=200, className='LogoId')

                ], className='Alinhamento'),

                html.Div('Desenvolvido por alunos da Universidade De Brasília - FGA', style={'color': 'black', 'text-align': 'center', 'font-family': 'Century Gothic', 'font-weight': 'bold'})
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=ESTILO_BARRA_LATERAL,
)

# -----------------------------------------------------------------------------------------
# DECLARAÇÃO EM PARTES DO SITE:

    # B) MODAIS:

modalPrim1 = html.Div(
    [
        dbc.Modal(
            [   # TÍTULO DO MODAL:
                dbc.ModalHeader(dbc.ModalTitle("Filtro: Primeiro Gráfico (Barras)")),

                # CORPO DO MODAL:
                dbc.ModalBody([

                    html.P('Selecione o continente a ser FIltrado:'),

                        dcc.Dropdown(opcoes, value='Todos os Continentes', id='Filtro_Continentes', className='Dropdown1', style={
                            'background-color': 'chocolate',
                            'border-radius': '14px',
                            'border-color': 'transparent',                       
                        }),
    
    
        

                    html.P('Selecione o Tipo de Café a ser FIltrado:', style={'margin-top': '2vh'}),

                        dcc.Dropdown(opcoes2, value='TOTAL', id='Filtro_Tipo', className='Dropdown2', style={
                            'background-color': 'chocolate',
                            'border-radius': '14px',
                            'border-color': 'transparent',
                            'margin-bottom': '1vh',
                            'margin-top': '1vh'                       
                        }),
                ]),

                # RODAPÉ DO MODAL:
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="closePrim1", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modalPrim1",
            is_open=False,
            size='lg'
        ),
    ]
)

modalPrim2 = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Filtro: Segundo Gráfico (Barras em Grupos)")),
                dbc.ModalBody([

                    html.P('Selecione a Localização da Receita Federal a Ser filtrada:'),

                    dcc.Dropdown(receita_filtragem, value='Todos', id='filtro4', className='Dropdown4', style={
                        'background-color': 'chocolate',
                        'border-radius': '14px',
                        'border-color': 'transparent',
                        'margin-bottom': '1vh'}),

                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="closePrim2", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modalPrim2",
            is_open=False,
            size='lg'
        ),
    ]
)

modalPrim3 = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Filtro: Terceiro Gráfico (Linhas)")),
                dbc.ModalBody([

                    html.P('Selecione o Tipo de Café a ser filtrado:'),

                    dcc.Dropdown(opcoes3, value='Todos os Tipos de Café', id='filtro3', className='Dropdown3', style={
                        'background-color': 'chocolate',
                        'border-radius': '14px',
                        'border-color': 'transparent',
                        'margin-bottom': '1vh'}),

                ]),
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="closePrim3", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modalPrim3",
            is_open=False,
            size='lg'
        ),
    ]
)

# DECLARAÇÃO DO 1º MODAL:
modal1 = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Compra de Café Brasileiro")),
                dbc.ModalBody("Gráfico em barras, representa a quantidade exportada de café brasileiro entre os principais países compradores do produto"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="close1", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modal1",
            is_open=False,
            size='lg'
        ),
    ]
)

# DECLARAÇÃO DO 2º MODAL:
modal2 = html.Div(
    [
        dbc.Modal(
            [   # TÍTULO DO MODAL:
                dbc.ModalHeader(dbc.ModalTitle("Importação e Exportação por Receita Federal")),

                # CORPO DO MODAL:
                dbc.ModalBody("Dividido entre as receitas federais, este gráfico de barras, divididos em grupos, relata a Exportação e Importação de café."),

                # RODAPÉ DO MODAL:
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="close2", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modal2",
            is_open=False,
            size='lg'
        ),
    ]
)

# DECLARAÇÃO DO 3º MODAL:
modal3 = html.Div(
    [
        dbc.Modal(
            [   # TÍTULO DO MODAL:
                dbc.ModalHeader(dbc.ModalTitle("Preço Médio do Café Brasileiro")),

                # CORPO DO MODAL:
                dbc.ModalBody("Preço médio calculado mensalmente do café brasileiro, estão representadas neste gráfico de Linhas. (Valores em Dólar US$)."),

                # RODAPÉ DO MODAL:
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="close3", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modal3",
            is_open=False,
            size='lg'
        ),
    ]
)

# DECLARAÇÃO DO 4º MODAL:
modal4 = html.Div(
    [
        dbc.Modal(
            [   # TÍTULO DO MODAL:
                dbc.ModalHeader(dbc.ModalTitle("Produção de Café entre Principais Países")),

                # CORPO DO MODAL:
                dbc.ModalBody("Os dados de produção do mapa esta localizada em cada ponto de seu local, para navegar entre eles, gire o planeta pressionando e arrastando o mouse."),

                # RODAPÉ DO MODAL:
                dbc.ModalFooter(
                    dbc.Button(
                        "Fechar", id="close4", className="ms-auto", n_clicks=0, color='dark', outline=True
                    )
                ),
            ],
            id="modal4",
            is_open=False,
            size='lg'
        ),
    ]
)


#-----------------------------------------------------------------------------------------
# DECLARAÇÃO EM PARTES DO SITE:

    # C) GRÁFICOS:



# DECLARAÇÃO  EM HTML DO 1º GRÁFICO:
grafico1 = [

    dcc.Graph(
        id='Grafico_dados',
        figure=fig1
    )
]

# DECLARAÇÃO  EM HTML DO 2º GRÁFICO:
grafico2 = [

        dcc.Graph(
            id='Grafico_dados2',
            figure=fig2
    )

]

# DECLARAÇÃO  EM HTML DO 3º GRÁFICO:
grafico3 = [

    dcc.Graph(
        id='Grafico_dados3',
        figure=fig3
    ),

]

# DECLARAÇÃO EM HTML DO 4º GRÁFICO:
grafico4 = [

    dcc.Graph(
        id='Grafico_dados4',
        figure=fig4
    )

]
# -----------------------------------------------------------------------------------
# DECLARAÇÃO EM PARTES DO SITE:

    # D) LINHAS DO SITE:


# ORGANIZAÇÃO EM LINHAS DO SITE, NESTE CASO DA LINHA 1:
Conteudo_Linha1 = [

    # A LINHA 1 SERÁ COMPOSTA PELOS GRÁFICOS "grafico1" E "grafico2", QUE SÃO VARIÁVEIS DECLARADAS LOGO ACIMA:
    dbc.Col(html.Div(grafico1), width=5),

    dbc.Col(html.Div(grafico2), width=5),
]

# ORGANIZAÇÃO EM LINHAS DO SITE, NESTE CASO DA LINHA 2:
Conteudo_Linha2 = [

    # A LINHA 1 SERÁ COMPOSTA PELOS GRÁFICOS "grafico3" E "grafico4", QUE SÃO VARIÁVEIS DECLARADAS LOGO ACIMA:
    dbc.Col(html.Div(grafico3), width=5),

    dbc.Col(html.Div(grafico4), width=5),
]

# --------------------------------------------------------------------------------------
# DECLARAÇÃO FINAL DO SITE:

    # E) LAYOUT:


# DECLARAÇÃO DE COMO FICARÁ O LAYOUT:
app.layout = html.Div(className='Tudo', id='Tudo', children=[


    html.Div(className='Base', children= [

    # DIV PARA A PRIMEIRA LINHA:
    html.Div(className='PrimeiraColuna' , children=[
      
        # A PRIMEIRA LINHA TERÁ O CONTEÚDO DA VARIÁVEL 'Conteudo_Linha1':
        dbc.Row(
            Conteudo_Linha1,
            justify="end",
            style={'margin-right': '2vw'}
        )
       
    ]),

    # DIV PARA A SEGUNDA LINHA:
    html.Div(className='SegundaColuna', children=[

        # A SEGUNDA LINHA TERÁ O CONTEÚDO DA VARIÁVEL 'Conteudo_Linha2':
        dbc.Row(
            Conteudo_Linha2,
            justify="end",
            style={'margin-right': '2vw'}
        )

    ])
    ]), barralateral, modal1, modal2, modal3, modal4, modalPrim1, modalPrim2, modalPrim3])


# =====================================================================================================================
# INICIAÇÃO AOS CALLBACKS:

    # CALLBACK PARA O GRÁFICO 1 (EM BARRAS):

# DEFINIÇÃO DE FUNÇÃO PARA FILTRAGEM QUE IRÁ SUBSTITUIR A FUNÇÃO 'LOC' DO PANDAS:
def filtragem(dataframe, pesquisa, coluna):
    Filtro = []
    
    if coluna == None:
        
        for linha in dataframe:
            if linha[0] == pesquisa:
                Filtro += [[linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]]]

    elif coluna == 3:

        for linha in dataframe:
            if linha[0] == pesquisa:
                Filtro += [[linha[0], linha[1], linha[2]]]


    else:
        referencia = 2
        for alternativa in opcoes2:
            if str(coluna) == str(alternativa):
                for linha in dataframe:
                    if linha[0] == pesquisa:
                        Filtro += [[linha[0], linha[1], linha[referencia]]]
            referencia += 1
        

    return Filtro


@app.callback(
    Output('Grafico_dados', 'figure'),
    Input('Filtro_Tipo', 'value'),
    Input('Filtro_Continentes', 'value')
)
def update_de_dash(tipo, continente):
    dfFl1 = df1.values

    if tipo == 'TOTAL':
        if continente == 'Todos os Continentes':

            fig1 = px.bar(df1, x="CONTINENTE", y="TOTAL", color="PAÍS DESTINO", title='Compra de Café Brasileiro por País por Continente')

        else:  

            filtro = filtragem(dfFl1, str(continente), None)
            fig1 = px.bar(filtro, x=0, y=6, color=1, title=f'Compra de Café Brasileiro ({continente})', labels={'0': 'CONTINENTE', '6': 'TOTAL', '1': 'PAÍS DESTINO'})

    else:
        if continente == 'Todos os Continentes':

            fig1 = px.bar(df1, x="CONTINENTE", y=str(tipo), color="PAÍS DESTINO", title=f'Compra de Café {tipo} Brasileiro por Continente')

        else:

            filtro = filtragem(dfFl1, str(continente), str(tipo))
            fig1 = px.bar(filtro, x=0, y=2, color=1, title=f'Compra de Café {tipo} Brasileiro ({continente})', labels={'0': 'CONTINENTE', '1': 'PAÍS DESTINO', '2': tipo})

    fig1.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0.2)',
        font_color='white',
        
    )

    return fig1
# ======================================================================================================================
    # CALLBACL PARA O GRÁFICO 2:

@app.callback(
    Output('Grafico_dados2', 'figure'),
    Input('filtro4', 'value')
)
def UpdateDeDash01(value):
    if value == 'Todos':
        fig2 = px.bar(dfOf1, x=0, y=1, color=2, barmode="group", title='Exportação/Importação por Receita Federal', labels={
             '0': 'Unidade Da Receita Federal',
             '1': 'Sacas (60kg)',
             '2': 'Tipo'
            })

    else:

        fig2filtrada = filtragem(dfOf1, str(value), 3)
        fig2 = px.bar(fig2filtrada, x=0, y=1, color=2, barmode="group", title=f'Exportação/Importação da Receita Federal ({value})', labels={
             '0': value,
             '1': 'Sacas (60kg)',
             '2': 'Tipo'
            })
        
    fig2.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0.2)',
        font_color='white',
    )

    return fig2

# ======================================================================================================================
    # CALLBACK PARA O GRÁFICO 3:


@app.callback(
    Output('Grafico_dados3', 'figure'),
    Input('filtro3', 'value')
)
def UpdateDeDash1(value):
    if value == 'Todos os Tipos de Café':

        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Conillon'],
                            mode='lines',
                            name='Conillon'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Arábica'],
                            mode='lines',
                            name='Arábica'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Total Café Verde'],
                            mode='lines', name='Total (Café Verde)'))

        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Torrado'],
                            mode='lines', name='Torrado'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Solúvel'],
                            mode='lines', name='Solúvel'))
        fig3.add_trace(go.Scatter(x=df3['Mês/Ano'], y=df3['Total Industrializado'],
                            mode='lines', name='Total (Industrializado)'))

        fig3.update_layout(title='Preço Médio do Café Brasileiro',
                        xaxis_title='Ano',
                        yaxis_title='Preço Médio (US$)')

    else:

        fig3 = px.line(df3, x='Mês/Ano', y=str(value), title=f'Preço Médio ({value}) Brasileiro', labels={ str(value) : f'Preço Médio (US$) - {value}'})


    fig3.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0.2)',
        font_color='white',
    )

    return fig3

# ======================================================================================================================
# CALLBACK PARA OS MODAIS:


# PARA O MODAL 1:
@app.callback(
    Output("modal1", "is_open"),
    [Input("menu1", "n_clicks"), Input("close1", "n_clicks")],
    [State("modal1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# PARA O MODAL 2:
@app.callback(
    Output("modal2", "is_open"),
    [Input("menu2", "n_clicks"), Input("close2", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modal1(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# PARA O MODAL 3:
@app.callback(
    Output("modal3", "is_open"),
    [Input("menu3", "n_clicks"), Input("close3", "n_clicks")],
    [State("modal3", "is_open")],
)
def toggle_modal2(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# PARA O MODAL 4:
@app.callback(
    Output("modal4", "is_open"),
    [Input("menu4", "n_clicks"), Input("close4", "n_clicks")],
    [State("modal4", "is_open")],
)
def toggle_modal3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modalPrim1", "is_open"),
    [Input("Drop1", "n_clicks"), Input("closePrim1", "n_clicks")],
    [State("modalPrim1", "is_open")],
)
def toggle_modal3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("modalPrim2", "is_open"),
    [Input("Drop2", "n_clicks"), Input("closePrim2", "n_clicks")],
    [State("modalPrim2", "is_open")],
)
def toggle_modal3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@app.callback(
    Output("modalPrim3", "is_open"),
    [Input("Drop3", "n_clicks"), Input("closePrim3", "n_clicks")],
    [State("modalPrim3", "is_open")],
)
def toggle_modal3(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)