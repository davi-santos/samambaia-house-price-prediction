import pandas as pd
import numpy as np
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import statsmodels
from scipy.special import boxcox1p
import pickle

# fav Flatly

# read the data
df = pd.read_csv('./data/data_app.csv', index_col=[0])

# load the machine learning model
voting_model = pickle.load(open('./model/voting_model.sav', 'rb'))

# create app
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc.icons.BOOTSTRAP])
server = app.server

# read data
df = pd.read_csv('./data/data_app.csv', index_col=[0])

# CREATE COMPONENTS

# Text section: all important and relevant text in the page are in these variables
title_page = 'SAMAMBAIA IMÓVEIS'
subtitle_page = 'Uma análise dos preços dos imóveis da Samambaia. Dados obtidos em Dezembro de 2022\
     na OLX. Para mais detalhes, acesse os links abaixo.'

# Icons
git_icon = html.I(className='bi bi-github')
linkedin_icon = html.I(className='bi bi-linkedin')
twitter_icon = html.I(className='bi bi-twitter')
book_icon = html.I(className='bi bi-book')

# title
header = dbc.Row(
            dbc.Container(
                children=[
                    dbc.Row([
                        dbc.Col(
                            html.H2(title_page), width=6, className='mt-4 text-center')],
                        justify='center'),
                    dbc.Row([
                        dbc.Col(
                            html.P(subtitle_page), width=10, className='text-center')],
                        justify='center'),
                    dbc.Row([
                        dbc.Col([
                            dbc.Button([book_icon], class_name='me-2',
                                        href='https://www.kaggle.com/code/daviribeirodossantos/an-lise-dos-pre-os-dos-im-veis-da-samambaia-df',
                                        target='_blank', style={'background-color': '#0091D5', 'border': 'white'}),
                            dbc.Button(children=[git_icon], className='me-2', style={'background-color': '#0091D5', 'border': 'white'},
                                        href='https://github.com/davi-santos/samambaia-house-price-prediction', target='_blank'),
                            dbc.Button([linkedin_icon], class_name='me-2', style={'background-color': '#0091D5', 'border': 'white'},
                                        href='https://www.linkedin.com/in/davi-datascientist/', target='_blank'),
                            dbc.Button([twitter_icon], class_name='me-2', style={'background-color': '#0091D5', 'border': 'white'},
                                        href='https://twitter.com/davidtscience', target='_blank'),
                        ],
                        align='center', className='text-center mb-4')],
                        justify='evenly')
                        ],
                    
                fluid=True),
                className='text-white',
                style={'background-color': '#1C4E80'}
        ) 
        

# buttons at the top
buttons_head = dbc.Container(
                dbc.Row(
                    children=[
                        dbc.Col(
                            dbc.RadioItems(
                                id="graphs-options",
                                className="btn-group mt-2 mb-2",
                                inputClassName="btn-check",
                                labelClassName="btn btn-outline-primary",
                                labelCheckedClassName="active",
                                options=[
                                    {'label': 'Casas', 'value':'houses'},
                                    {'label': 'Apartamentos', 'value':'apartments'},
                                    {'label': 'Todos', 'value':'all'},
                                ],
                                value='all'
                            ),
                            sm=11, md=11, lg=6, xl=6, xxl=6,
                        )
                    ],
                    className='', justify='center'
                ),                
                className="mt-2 text-center",
                fluid=True)

# first row: map and info
first_row = dbc.Container(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(
                                dcc.Graph(id='graph-samambaia'), 
                                className="text-center",
                                sm=11, md=11, lg=11, xl=10, xxl=10),
                            dbc.Col(
                                children=[
                                    dbc.Container(
                                        dbc.Row(
                                            children=[
                                                html.H4('PREÇO DOS IMÓVEIS', className='text-center mb-4'),
                                                dbc.Col(
                                                    children=[
                                                        html.H5('Média:', className='mt-3 text-dark'),
                                                        html.H2(children='', id='average-value-houses', style={'color':'#EA6A47'}),
                                                        html.P('reais', className='text-dark'),
                                                    ], 
                                                # className='border rounded-1 text-center bg-light mt-3',
                                                className='text-center mt-1 mb-3 border bg-light',
                                                sm=11, md=11, lg=11, xl=12, xxl=12),
                                            ], align='center', justify='center'
                                        )
                                    ),
                                    dbc.Container(
                                        dbc.Row(
                                            children=[
                                                dbc.Col(
                                                    children=[
                                                        html.P('Mínimo:', className='text-dark'),
                                                        html.H5('', id='min-value-houses', style={'color': '#1C4E80'}),
                                                        html.P('reais', className='text-dark mt-1'),
                                                    ], 
                                                    className='mt-2', 
                                                    sm=11, md=11, lg=5, xl=6, xxl=6),
                                                dbc.Col(
                                                    children=[
                                                        html.P('Máximo', className='text-dark'),
                                                        html.H5('', id='max-value-houses', style={'color': '#0091D5'}),
                                                        html.P('reais', className='text-dark mt-1'),
                                                    ], className='mt-2', 
                                                    sm=11, md=11, lg=5, xl=6, xxl=6),
                                                ],
                                            className='text-center mb-3', align='center', justify='evenly'
                                        ), fluid=True),
                                        dbc.Container(
                                            dbc.Row(
                                                children=[
                                                    dbc.Col(
                                                        children=[
                                                            html.P('Dos anúncios obtidos, 50% custam de', 
                                                                    className='mt-2 mb-2'),
                                                            html.H4('', id='range-value-houses',
                                                                    className='mt-2 mb-2', style={'color': '#7E909A'}),
                                                            html.P('Mais detalhes em: link')
                                                        ], 
                                                    className='text-center'),
                                                ],
                                                className='mt-1', align='center', justify='around'
                                            ),
                                        ),
                                ], 
                                    sm=11, md=11, lg=11, xl=2, xxl=2,
                                    )
                                ], 
                        className='mt-2 mb-2', align='center', justify='around'
                    ),
                ],
                className="mt-2 text-center border bg-white",
                fluid=True)

# Second row: two graphs
second_row = dbc.Container(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(
                                dcc.Graph(id='graph-histogram', className='border bg-white'), 
                                className="", 
                                sm=11, md=11, lg=11, xl=7, xxl=7),
                            dbc.Col(
                                dcc.Graph(id='graph-scatter', className='border bg-white mt-1'), 
                                sm=11, md=11, lg=11, xl=5, xxl=5),
                        ],
                        className='mt-2', align='center', justify='around'
                    ),
                ],
                fluid=True,
            )

# third row: two other graphs
third_row = dbc.Container(
                dbc.Row(
                    children=[
                        dbc.Col(
                            dcc.Graph(id='graph-n-garage', className='border bg-white'), 
                            sm=11, md=11, lg=11, xl=6, xxl=6),
                        dbc.Col(
                            dcc.Graph(id='graph-n-bath', className='border bg-white mt-1'), 
                            sm=11, md=11, lg=11, xl=6, xxl=6),
                    ],
                    className='mt-2', align='center', justify='around'
                ),
                className='mb-2',
                fluid=True,
            )

# calculator
calculator = dbc.Row(
                dbc.Container(
                    children=[
                        dbc.Row(
                            dbc.Col(
                                html.H2('Simulador de preços', className='text-light mt-3 mx-3'),
                                width={"size": 6, "offset": 1},
                            ),
                            className='',
                        ),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dcc.Markdown('Categoria'),
                                        dcc.Dropdown(options=['Casas', 'Apartamentos'], id='calc-houses', className='text-dark'),
                                        dcc.Markdown('Número de banheiros', className='mt-4'),
                                        dcc.Dropdown(options=[0, 1, 2, 3, 4, 5], id='calc-bath', className='text-dark'),
                                        dcc.Markdown('Número de Quartos', className='mt-4'),
                                        dcc.Dropdown(options=[0, 1, 2, 3, 4, 5], id='calc-bedrooms', className='text-dark'),
                                        dcc.Markdown('Tamanho do imóvel (m²)', className='mt-4'),
                                        dbc.Input(type="number", id='calc-size',min=0, max=2000, className='mt-2'),
                                    ], 
                                    sm=11, md=5, lg=5, xl=3, xxl=3),
                                dbc.Col(
                                    children=[
                                        dcc.Markdown('Quantidade de vagas na garagem'),
                                        dcc.Dropdown([0, 1, 2, 3, 4, 5], id='calc-n-garage', className='text-dark'),
                                        dcc.Markdown('Valor do condomínio', className='mt-4'),
                                        dbc.Input(type="number", id='calc-cond',min=0, max=1200, className='mt-2'),
                                        dcc.Markdown('Região', className='mt-4'),
                                        dcc.Dropdown(['Samambaia norte', 'Samambaia sul'], id='calc-region', className='text-dark mb-4'),
                                        dcc.Markdown('É perto do metrô? (até 3 km)'),
                                        dcc.Dropdown(['Sim', 'Não'], id='calc-pair', className='text-dark'),
                                    ], 
                                    sm=11, md=5, lg=5, xl=3, xxl=3),
                                dbc.Col(
                                    children=[
                                        dbc.Button('Calcular', id='button-calc', className='mt-5', n_clicks=0),
                                        html.H4('Resposta:', className='mt-3', id='answer-calculator'),
                                        html.H5('Preço médio: X', id='average-price-model'),
                                        html.H5(children='Variação de preços é de: A à B', id='my-result-model'),
                                    ],
                                    sm=11, md=9, lg=9, xl=3, xxl=3),
                            ],
                            className='text-light mb-5',
                            justify='evenly'),
                    ],
                     
                className='mt-3'),
                style={'background-color': '#EA6A47'},
            )

# Sources
sources = dbc.Container(
            children=[
                dbc.Row(
                    dbc.Col(
                        html.H3(''),
                        width=10
                    )
                )
            ],
            className='mt-5 mb-5'
        )

# create own layout
app.layout = dbc.Container([header, buttons_head, first_row, second_row, third_row, calculator, sources], 
                            style={'background-color': '#f7f7f7'},fluid=True)


# DEFINING FUNCTIONS TO PLOT GRAPHS

def plot_scattermap(dff):
        # Remover endereços com locais nulos no sample
    df_sample = dff[~dff['latitude'].isna() & ~dff['longitude'].isna()]

    # Escolher colunas que queremos ver
    cols = ['house_category', 'latitude', 'longitude', 'house_price']

    #pegar local, lat e lon e calcular média dos preço, salvos em house_price
    df_search = df_sample[cols].groupby(['house_category', 'latitude', 'longitude']).mean().reset_index()

    # # take the number of houses by location and catogory
    df_search[0] = df_sample[cols].groupby(['house_category', 'latitude', 'longitude']).count().reset_index()['house_price']

    fig = px.scatter_mapbox(df_search,
                        lon = df_search['longitude'],
                        lat = df_search['latitude'],
                        center={"lat": -15.878191211624543, "lon": -48.10520207922798},
                            zoom=13,
                        color = df_search['house_price'],
                        height=560,
    #                        size = df_search[0],
                        color_continuous_scale=px.colors.diverging.Portland,
                        labels={'house_price': 'Preço médio<br>dos imóveis'},
                        )

    fig.update_layout(mapbox_style='open-street-map', plot_bgcolor = 'white', paper_bgcolor = 'white')
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_traces(marker={'size':13})

    return fig

def plot_histogram(dff):
    title = 'DISTRIBUIÇÃO DO PREÇO'

    fig = px.histogram(data_frame=dff, x='house_price', color='house_category', marginal='box', 
                   labels = {'house_category': ""}, color_discrete_sequence=['#1C4E80', '#0091D5'])

    fig.update_layout(
        title = title,
        titlefont = {'size': 18},
        template = 'simple_white',
        # paper_bgcolor = '#f8f8f8',
        # plot_bgcolor = '#f8f8f8',
        paper_bgcolor = 'white',
        plot_bgcolor = 'white',
        legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1)
    )

    fig.update_yaxes(
        showgrid = True,
        gridwidth = .2,
        gridcolor = '#f8f8f8'
    )

    fig['layout']['xaxis']['title'] = 'Número de banheiros'
    fig['layout']['yaxis']['title'] = 'Preço (R$)'

    return fig

def plot_scatterplot(dff):
    title = 'PREÇO vs TAMANHO DO IMÓVEL'

    fig = px.scatter(dff, x = 'house_size', y = 'house_price', color = 'house_category', trendline = 'ols',
                    labels = {'house_category': ""}, color_discrete_sequence=['#1C4E80', '#0091D5'])

    fig['layout']['xaxis']['title'] = 'Property size (m²)'
    fig['layout']['yaxis']['title'] = 'Price (R$)'

    fig.update_layout(
        title = title,
        titlefont = {'size': 18},
        template = 'simple_white',
        # paper_bgcolor = '#f8f8f8',
        # plot_bgcolor = '#f8f8f8',
        paper_bgcolor = 'white',
        plot_bgcolor = 'white',
        legend=dict(
                orientation="h",
                yanchor="bottom",
                y=0.97,
                xanchor="right",
                x=1.044)
    )

    fig.update_traces(marker_line_width=.3, marker_size = 9, marker_line_color = '#282828')

    fig.update_xaxes(
        showgrid = True,
        gridcolor = '#f8f8f8',
        gridwidth = .1
    )

    fig.update_yaxes(
        showgrid = True,
        gridcolor = '#f8f8f8',
        gridwidth = .1
    )


    fig['layout']['xaxis']['title'] = 'Tamanho do imóvel (m²)'
    fig['layout']['yaxis']['title'] = 'Preço (R$)'
    
    return fig

def plot_n_garage(dff):
    title = 'PREÇO vs N° DE VAGAS'

    fig = px.box(dff, x = 'n_garage', y = 'house_price', title = title, color = 'house_category', 
                labels = {'house_category': ""}, color_discrete_sequence=['#1C4E80', '#0091D5'])

    fig.update_layout(
        title = title,
        titlefont = {'size': 18},
        template = 'simple_white',
        # paper_bgcolor = '#f8f8f8',
        # plot_bgcolor = '#f8f8f8',
        paper_bgcolor = 'white',
        plot_bgcolor = 'white',
        legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1)
    )

    fig.update_yaxes(
        showgrid = True,
        gridcolor = '#c1c1c1',
        gridwidth = .4
    )

    fig['layout']['xaxis']['title'] = 'Vagas de garagem'
    fig['layout']['yaxis']['title'] = 'Preço (R$)'

    return fig

def plot_n_bath(dff):
    title = 'PREÇO vs N° DE BANHEIROS'

    list_order = [0, 1, 2, 3, 4, '5 ou mais']

    fig = px.box(dff, x = 'n_bathrooms', y = 'house_price', title = title, color = 'house_category', 
                category_orders={'n_bathrooms': list_order}, labels = {'house_category': ""}, 
                color_discrete_sequence=['#1C4E80', '#0091D5'])


    fig.update_layout(
        title = title,
        titlefont = {'size': 18},
        template = 'simple_white',
        # paper_bgcolor = '#f8f8f8',
        # plot_bgcolor = '#f8f8f8',
        paper_bgcolor = 'white',
        plot_bgcolor = 'white',
        legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1)
    )

    fig.update_yaxes(
        showgrid = True,
        gridcolor = '#c1c1c1',
        gridwidth = .4
    )

    fig['layout']['xaxis']['title'] = 'Número de banheiros'
    fig['layout']['yaxis']['title'] = 'Preço (R$)'

    return fig


# callbacks
@app.callback(
    [Output(component_id='graph-samambaia', component_property='figure'),
     Output(component_id='average-value-houses', component_property='children'),
     Output('min-value-houses', 'children'),
     Output('max-value-houses', 'children'),
     Output('range-value-houses', 'children'),
     Output('graph-histogram', 'figure'),
     Output('graph-scatter', 'figure'),
     Output('graph-n-garage', 'figure'),
     Output('graph-n-bath', 'figure')
    ],
    [Input(component_id='graphs-options', component_property='value'),
    ]
)
def filter_data(graphs_option):

    # Filter data accordingly to the buttons option
    dff = pd.DataFrame()

    if graphs_option == 'all':
        dff = df.copy()
    elif graphs_option == 'houses':
        dff = df[df['house_category'] == 'Casas']
    else:
        dff = df[df['house_category'] == 'Apartamentos']
    
    # make graphs
    fig_map = plot_scattermap(dff)

    # average house prices
    average_value = dff['house_price'].mean()
    average_value = f'{average_value:,.0f}'
    average_value = average_value.replace(',','.')

    # min house prices
    min_value = dff['house_price'].min()
    min_value = f'{min_value:,.0f}'
    min_value = min_value.replace(',','.')

    # max house prices
    max_value = dff['house_price'].max()
    max_value = f'{max_value:,.0f}'
    max_value = max_value.replace(',','.')

    # Range values text
    Q3 = np.quantile(dff['house_price'], 0.75)
    Q1 = np.quantile(dff['house_price'], 0.25)
    Q1 = f'{Q1:,.0f}'.replace(',','.')
    Q3 = f'{Q3:,.0f}'.replace(',','.')
    range_values = f'{Q1} à {Q3}'

    # Histogram graph
    fig_hist = plot_histogram(dff)

    # Scatterplot graph
    fig_scatter = plot_scatterplot(dff)

    # N garage graph
    fig_n_garage = plot_n_garage(dff)

    # N bath graph
    fig_n_bath = plot_n_bath(dff)

    return fig_map, average_value, min_value, max_value, range_values, fig_hist, fig_scatter, fig_n_garage, fig_n_bath

@app.callback(
    [Output('answer-calculator', 'children'),
     Output('average-price-model', 'children'),
     Output(component_id='my-result-model', component_property='children')],
    [Input('button-calc', 'n_clicks')],
    [State('calc-houses', 'value'), State('calc-bath', 'value'),
    # Daqui pra baixo falta as variáveis
     State('calc-bedrooms', 'value'), State('calc-size', 'value'),
     State('calc-n-garage', 'value'), State('calc-cond', 'value'),
     State('calc-region', 'value'), State('calc-pair', 'value')],
    prevent_inicial_call = False,
)
def model_prediction(n_clicks, house_category, house_n_bath, house_n_bedrooms, house_size,
                     house_n_garage, house_condominium, house_region, house_metro_distance):
    
    if n_clicks == 0:
        return '', 'Preencha os campos e clique no botão calcular para que nosso modelo faça uma estimativa do preço do imóvel.', ''
    
    # make sure all data are not none
    check_data = [house_category, house_n_bath, house_n_bedrooms, house_size, house_n_garage,
              house_condominium, house_region, house_metro_distance]
    
    for item in check_data:
        if item == None:
            return '', 'Você precisa preencher todos os campos!', ''

    # calculate standar deviation
    std = df[df['house_category'] == house_category]['house_price'].std()

    # Convert some of the data to numeric
    house_category = 1 if house_category == 'Apartamentos' else 0
    house_region = 1 if house_region == 'Samambaia norte' else 0
    pair = 1 if house_metro_distance == 'Sim' else 0
    not_pair = 0 if house_metro_distance == 'Sim' else 1

    # Creating missing features
    house_has_condiminium = 1 if house_condominium > 0 else 0
    house_has_garage = 1 if house_n_garage > 0 else 0

    # Structure in the format the model was trained
    X_data = [house_n_bedrooms, house_condominium, house_n_garage, house_size,
              house_n_bath, house_region, house_has_condiminium, house_has_garage,
              house_category, pair, not_pair]
    
    X_data = boxcox1p(X_data, 0.15)
    X_data = [round(val, 3) for val in X_data]
    
    # Prediction
    predicted_value = voting_model.predict(np.array(X_data).reshape(1, -1))[0]
    
    predicted_value = round(predicted_value, 3)
    predicted_value = str(predicted_value).replace('.', '')
    predicted_value = float(predicted_value)
    up_value = f'{predicted_value+std:,.0f}'.replace(',', '.')
    predicted_value = f'{predicted_value:,.0f}'.replace(',','.')
    

    std = round(std, 0)

    string_show = f'Estimativa de R${predicted_value},00 reais, no mínimo, podendo custar até {up_value:},00 \
        dependendo da condição do imóvel, comércio local, localização, entre outras variáveis.'

    return 'Resposta', string_show, ''

if __name__ == '__main__':
    app.run_server(debug=False)

