from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel("Dados.xlsx")

# 'stack', 'group', 'overlay', 'relative'
fig = px.bar(df, x="Data", y="Interessados",
color="Nicho", barmode="relative")

ganho = px.bar(df, x="Data", y="Ganhos",
color="Tipo", barmode="stack")

app.layout = html.Div(children=[
    html.H1(children='Graficos de interesados nos nichos'),

    html.Div(children='''
        Grafico de interessados em forma de barra
    '''),

    dcc.Graph(
        id='quantidade_encajamento',
        figure=fig
    ),

    html.Div('''
        Grafico de ganhos
    '''),

    dcc.Graph(
        id="quantidade_ganhos",
        figure=ganho
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)