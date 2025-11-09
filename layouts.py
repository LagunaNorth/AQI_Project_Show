import dash_bootstrap_components as dbc
from dash import dcc, html
import assets.graph_style as gs


def create_layout ():
    return dbc.Container([
        dbc.NavbarSimple(        #Навигационная панель
            brand='Дашборд о качестве воздуха в выбранном городе',
            brand_href='#', 
            className='nav_panel',
        ),

        dbc.Row([
            dbc.Col([           #Текущее состояние
                dbc.Card(id='state-output', body=True, className='card'),
            ], width=6, md=6, xs=12),
            dbc.Col([           #Выбор города
                dbc.Input(id='city-input', 
                          value='Санкт-Петербург', 
                          placeholder='Введите название города', 
                          type='text', debounce=True, 
                          className='city-box'),
            ], width=6, md=6, xs=12)
        ]),

        dbc.Row([               #Настройки почасового прогноза
            dbc.Col([           #Выбор временного диапазона (сегодня, завтра, прслезавтра)
                html.Label("Почасовой прогноз по загрязнителям на:", className='settings-label'),
                dcc.Dropdown(
                    id='forecast-day',
                    options=[
                        {'label': 'сегодня', 'value': 0},
                        {'label': 'завтра', 'value': 1},
                        {'label': 'послезавтра', 'value': 2},
                    ],
                    value=0,
                    clearable=False,
                    className='forecast-dropdown',
                    style=gs.DROPDOWN_STYLE)], md=4),
            dbc.Col([           #Выбор вида графика
                html.Label("Вид графика", className='settings-label'),
                dcc.Dropdown(
                    id='chart-type',
                    options=[
                        {'label': 'Линейный', 'value': 'line'},
                        {'label': 'Столбчатый', 'value': 'bar'},
                    ],
                    value='line', 
                    clearable=False,
                    className='forecast-dropdown',
                    style=gs.DROPDOWN_STYLE
                )
            ]),
            dbc.Col([           #Добавление ПДК
                dbc.Checklist(
                    id='pdk',
                    options=[
                        {"label": "Показать предельно допустимые концентрации", "value": "on"}
                    ],
                    value=["off"],
                    switch=True,
                    className='pdk_choice'
                )
            ])
        ], className='settings-row'),
                                #Графики
        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph', className='air-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='no2-graph', className='air-graph'), width=4, md=4, xs=12),
            dbc.Col(dcc.Graph(id='o3-graph', className='air-graph'), width=4, md=4, xs=12),
        ], className='graph-row'),
        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph', className='air-graph'), width=4, md=4, xs=12), 
            dbc.Col(dcc.Graph(id='pm2_5-graph', className='air-graph'), width=4, md=4, xs=12), 
            dbc.Col(dcc.Graph(id='pm10-graph', className='air-graph'), width=4, md=4, xs=12),
        ], className='graph-row')
        ], fluid=True)