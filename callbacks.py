from utils.data_loader import load_air_data
import plotly.graph_objects as go
import plotly.io as pio
from dash import Input, Output, html
import assets.graph_style as gs


pio.templates['air'] = pio.templates['plotly'].update(
    layout=dict(colorway=gs.MY_PALETTE)
)

pio.templates.default = 'air'


def register_callbacks (app):
    @app.callback(
            Output('state-output', 'children'),
            Output('co-graph', 'figure'),
            Output('no2-graph', 'figure'),
            Output('o3-graph', 'figure'),
            Output('so2-graph', 'figure'),
            Output('pm2_5-graph', 'figure'),
            Output('pm10-graph', 'figure'),
            Input('city-input', 'value'),
            Input('forecast-day', 'value'),
            Input('chart-type', 'value'),
            Input('pdk', 'value')
    )


    def update_dash(city, day, chart_type, pdk):
        data = load_air_data(city)
        if not city: 
            return {}
        co_fig = go.Figure()
        if chart_type == "bar" and day == 0:
            co_fig.add_trace(
                go.Bar(
                    x=data['hours'],
                    y=data['co'],
                    name="Концентрация угарного газа (CO)"))
        elif chart_type == "bar" and day == 1:
            co_fig.add_trace(
                go.Bar(
                    x=data['hours1'],
                    y=data['co_1'],
                    name="Концентрация угарного газа (CO)"))
        elif chart_type == "bar" and day == 2:
            co_fig.add_trace(
                go.Bar(
                    x=data['hours2'],
                    y=data['co_2'],
                    name="Концентрация угарного газа (CO)"))
        elif chart_type == 'line' and day == 0: 
            co_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=data['co'],
                    name="Концентрация угарного газа (CO)",
                    mode="lines+markers"))
        elif chart_type == 'line' and day == 1: 
            co_fig.add_trace(
                go.Scatter(
                    x=data['hours1'],
                    y=data['co_1'],
                    name="Концентрация угарного газа (CO)",
                    mode="lines+markers"))
        else: 
            co_fig.add_trace(
                go.Scatter(
                    x=data['hours2'],
                    y=data['co_2'],
                    name="Концентрация угарного газа (CO)",
                    mode="lines+markers"))
                          
        co_fig.update_layout(
            title='Концентрация угарного газа (CO)',
            title_font_size=gs.GRAPH_TITLE_FONT_SIZE,
            title_x=gs.GRAPH_TITLE_ALIGN,
            title_font_weight=gs.GRAPH_FONT_WEIGHT,
            title_font_color=gs.GRAPH_TITLE_FONT_COLOR,
            xaxis_title='Время',
            yaxis_title='CO (мкг/м3)',
            font=dict(family=gs.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            plot_bgcolor=gs.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=gs.PAPER_BACKGROUND_COLOR,
        )
        no2_fig = go.Figure() 
        if chart_type == "bar" and day == 0:
            no2_fig.add_trace(
                go.Bar(
                    x=data['hours'],
                    y=data['no2'],
                    name="Концентрация двуокиси азота (NO2)"))
        elif chart_type == "bar" and day == 1:
            no2_fig.add_trace(
                go.Bar(
                    x=data['hours1'],
                    y=data['no2_1'],
                    name="Концентрация двуокиси азота (NO2)"))
        elif chart_type == "bar" and day == 2:
            no2_fig.add_trace(
                go.Bar(
                    x=data['hours2'],
                    y=data['no2_2'],
                    name="Концентрация двуокиси азота (NO2)"))
        elif chart_type == 'line' and day == 0: 
            no2_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=data['no2'],
                    name="Концентрация двуокиси азота (NO2)",
                    mode="lines+markers"))
        elif chart_type == 'line' and day == 1: 
            no2_fig.add_trace(
                go.Scatter(
                    x=data['hours1'],
                    y=data['no2_1'],
                    name="Концентрация двуокиси азота (NO2)",
                    mode="lines+markers"))
        else: 
            no2_fig.add_trace(
                go.Scatter(
                    x=data['hours2'],
                    y=data['no2_2'],
                    name="Концентрация двуокиси азота (NO2)",
                    mode="lines+markers"))

        no2_fig.update_layout(
            title='Концентрация двуокиси азота (NO2)',
            title_font_size=gs.GRAPH_TITLE_FONT_SIZE,
            title_x=gs.GRAPH_TITLE_ALIGN,
            title_font_weight=gs.GRAPH_FONT_WEIGHT,
            title_font_color=gs.GRAPH_TITLE_FONT_COLOR,
            xaxis_title='Время',
            yaxis_title='NO2 (мкг/м3)',
            font=dict(family=gs.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            plot_bgcolor=gs.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=gs.PAPER_BACKGROUND_COLOR,
        )

        o3_fig = go.Figure() 
        if chart_type == "bar" and day == 0:
            o3_fig.add_trace(
                go.Bar(
                    x=data['hours'],
                    y=data['o3'],
                    name="Концентрация приземного озона (O3)"))
        elif chart_type == "bar" and day == 1:
            o3_fig.add_trace(
                go.Bar(
                    x=data['hours1'],
                    y=data['o3_1'],
                    name="Концентрация приземного озона (O3)"))
        elif chart_type == "bar" and day == 2:
            o3_fig.add_trace(
                go.Bar(
                    x=data['hours2'],
                    y=data['o3_2'],
                    name="Концентрация приземного озона (O3)"))
        elif chart_type == 'line' and day == 0: 
            o3_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=data['o3'],
                    name="Концентрация приземного озона (O3)",
                    mode="lines+markers"))
        elif chart_type == 'line' and day == 1: 
            o3_fig.add_trace(
                go.Scatter(
                    x=data['hours1'],
                    y=data['o3_1'],
                    name="Концентрация приземного озона (O3)",
                    mode="lines+markers"))
        else: 
            o3_fig.add_trace(
                go.Scatter(
                    x=data['hours2'],
                    y=data['o3_2'],
                    name="Концентрация приземного озона (O3)",
                    mode="lines+markers"))
            
        o3_fig.update_layout(
            title='Концентрация приземного озона (O3)',
            title_font_size=gs.GRAPH_TITLE_FONT_SIZE,
            title_x=gs.GRAPH_TITLE_ALIGN,
            title_font_weight=gs.GRAPH_FONT_WEIGHT,
            title_font_color=gs.GRAPH_TITLE_FONT_COLOR,
            xaxis_title='Время',
            yaxis_title='O3 (мкг/м3)',
            font=dict(family=gs.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            plot_bgcolor=gs.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=gs.PAPER_BACKGROUND_COLOR,
        )

        so2_fig = go.Figure()
        if chart_type == "bar" and day == 0:
            so2_fig.add_trace(
                go.Bar(
                    x=data['hours'],
                    y=data['so2'],
                    name="Концентрация двуокиси серы (SO2)"))
        elif chart_type == "bar" and day == 1:
            so2_fig.add_trace(
                go.Bar(
                    x=data['hours1'],
                    y=data['so2_1'],
                    name="Концентрация двуокиси серы (SO2)"))
        elif chart_type == "bar" and day == 2:
            so2_fig.add_trace(
                go.Bar(
                    x=data['hours2'],
                    y=data['so2_2'],
                    name="Концентрация двуокиси серы (SO2)"))
        elif chart_type == 'line' and day == 0: 
            so2_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=data['so2'],
                    name="Концентрация двуокиси серы (SO2)",
                    mode="lines+markers"))
        elif chart_type == 'line' and day == 1: 
            so2_fig.add_trace(
                go.Scatter(
                    x=data['hours1'],
                    y=data['so2_1'],
                    name="Концентрация двуокиси серы (SO2)",
                    mode="lines+markers"))
        else: 
            so2_fig.add_trace(
                go.Scatter(
                    x=data['hours2'],
                    y=data['so2_2'],
                    name="Концентрация двуокиси серы (SO2)",
                    mode="lines+markers"))

        so2_fig.update_layout(
            title='Концентрация двуокиси серы (SO2)',
            title_font_size=gs.GRAPH_TITLE_FONT_SIZE,
            title_x=gs.GRAPH_TITLE_ALIGN,
            title_font_weight=gs.GRAPH_FONT_WEIGHT,
            title_font_color=gs.GRAPH_TITLE_FONT_COLOR,
            xaxis_title='Время',
            yaxis_title='SO2 (мкг/м3)',
            font=dict(family=gs.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            plot_bgcolor=gs.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=gs.PAPER_BACKGROUND_COLOR,
        )
        pm2_5_fig = go.Figure()
        if chart_type == "bar" and day == 0:
            pm2_5_fig.add_trace(
                go.Bar(
                    x=data['hours'],
                    y=data['pm2_5'],
                    name="Концентрация мелких твердых частиц (< 2.5 мкм)"))
        elif chart_type == "bar" and day == 1:
            pm2_5_fig.add_trace(
                go.Bar(
                    x=data['hours1'],
                    y=data['pm2_5_1'],
                    name="Концентрация мелких твердых частиц (< 2.5 мкм)"))
        elif chart_type == "bar" and day == 2:
            pm2_5_fig.add_trace(
                go.Bar(
                    x=data['hours2'],
                    y=data['pm2_5_2'],
                    name="Концентрация мелких твердых частиц (< 2.5 мкм)"))
        elif chart_type == 'line' and day == 0: 
            pm2_5_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=data['pm2_5'],
                    name="Концентрация мелких твердых частиц (< 2.5 мкм)",
                    mode="lines+markers"))
        elif chart_type == 'line' and day == 1: 
            pm2_5_fig.add_trace(
                go.Scatter(
                    x=data['hours1'],
                    y=data['pm2_5_1'],
                    name="Концентрация мелких твердых частиц (< 2.5 мкм)",
                    mode="lines+markers"))
        else: 
            pm2_5_fig.add_trace(
                go.Scatter(
                    x=data['hours2'],
                    y=data['pm2_5_2'],
                    name="Концентрация мелких твердых частиц (< 2.5 мкм)",
                    mode="lines+markers"))
            
        pm2_5_fig.update_layout(
            title='Концентрация мелких твердых частиц (< 2.5 мкм)',
            title_font_size=gs.GRAPH_TITLE_FONT_SIZE,
            title_x=gs.GRAPH_TITLE_ALIGN,
            title_font_weight=gs.GRAPH_FONT_WEIGHT,
            title_font_color=gs.GRAPH_TITLE_FONT_COLOR,
            xaxis_title='Время',
            yaxis_title='Концентрация частиц (мкг/м3)',
            font=dict(family=gs.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            plot_bgcolor=gs.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=gs.PAPER_BACKGROUND_COLOR,
        )
        pm10_fig = go.Figure()
        if chart_type == "bar" and day == 0:
            pm10_fig.add_trace(
                go.Bar(
                    x=data['hours'],
                    y=data['pm10'],
                    name="Концентрация крупных твердых частиц (< 10 мкм)"))
        elif chart_type == "bar" and day == 1:
            pm10_fig.add_trace(
                go.Bar(
                    x=data['hours1'],
                    y=data['pm10_1'],
                    name="Концентрация крупных твердых частиц (< 10 мкм)"))
        elif chart_type == "bar" and day == 2:
            pm10_fig.add_trace(
                go.Bar(
                    x=data['hours2'],
                    y=data['pm10_2'],
                    name="Концентрация крупных твердых частиц (< 10 мкм)"))
        elif chart_type == 'line' and day == 0: 
            pm10_fig.add_trace(
                go.Scatter(
                    x=data['hours'],
                    y=data['pm10'],
                    name="Концентрация крупных твердых частиц (< 10 мкм)",
                    mode="lines+markers"))
        elif chart_type == 'line' and day == 1: 
            pm10_fig.add_trace(
                go.Scatter(
                    x=data['hours1'],
                    y=data['pm10_1'],
                    name="Концентрация крупных твердых частиц (< 10 мкм)",
                    mode="lines+markers"))
        else: 
            pm10_fig.add_trace(
                go.Scatter(
                    x=data['hours2'],
                    y=data['pm10_2'],
                    name="Концентрация крупных твердых частиц (< 10 мкм)",
                    mode="lines+markers"))
            
        pm10_fig.update_layout(
            title='Концентрация крупных твердых частиц (< 10 мкм)',
            title_font_size=gs.GRAPH_TITLE_FONT_SIZE,
            title_x=gs.GRAPH_TITLE_ALIGN,
            title_font_weight=gs.GRAPH_FONT_WEIGHT,
            title_font_color=gs.GRAPH_TITLE_FONT_COLOR,
            xaxis_title='Время',
            yaxis_title='Концентрация частиц (мкг/м3)',
            font=dict(family=gs.GRAPH_FONT_FAMILY),
            xaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            yaxis=dict(title_font_size=gs.GRAPH_FONT_SIZE, tickfont=dict(size=gs.GRAPH_FONT_SIZE)),
            plot_bgcolor=gs.PLOT_BACKGROUND_COLOR,
            paper_bgcolor=gs.PAPER_BACKGROUND_COLOR,
        )
        if 'on' in pdk:
            co_fig.add_hline(y=5000, line_dash="dot", line_color="red")
            no2_fig.add_hline(y=200, line_dash="dot", line_color="red")
            o3_fig.add_hline(y=160, line_dash="dot", line_color="red")
            so2_fig.add_hline(y=500, line_dash="dot", line_color="red")
            pm2_5_fig.add_hline(y=160, line_dash="dot", line_color="red")
            pm10_fig.add_hline(y=300, line_dash="dot", line_color="red")

        cur_state = html.Div([
            html.P(f'Состояние воздуха в городе {data['city_name']} сейчас {data['aqi_level']}'),
            html.H5 (f'*Индекс качества воздуха (AQI); уровень, согласно EPA: {data['aqi']}')
        ])
        return cur_state, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig

