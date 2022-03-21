import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

def create_dash_application(flask_app,id):
    dash_app = dash.Dash(server=flask_app,url_base_pathname="/stats/")
    df = pd.read_json (f"json_data{id}.json")
    sum = []
    for i in df['Treść wiadomości']:
        sum.append(len(i))
    
    avg = df['Ocena'].sum() / len(df['Ocena'])
    avg = "{:.1f}".format(avg)
    up = df['Przydatna opinia'].sum()
    down = df['Nieprzydatna opinia'].sum()
    dash_app.layout =html.Div([
        html.H4(f'Avarage rating {avg}  Przydatnych Opini {up}  Nieprzydatnych Opini : {down}'),
        dcc.Graph(
            id = 'Ocena',
            figure = px.pie(df, values=df['Ocena'], names=df['Ocena'], hole=.3, title= 'Rozkład Ocen')
        ),
        dcc.Graph(
            id= 'Bar',
            figure = {
                'data':[
                {'x' : df['Ocena'],'y':df['Przydatna opinia'],'type':'bar','name':'FirstChart'},
                {'x' : df['Ocena'],'y':df['Nieprzydatna opinia'],'type':'bar','name':'Second'}],
                'layout': {
                    'title' : 'Rozkład przydatnych i nieprzydanych opinii na ocenach'
                }
            }
        ),
        dcc.Graph(
            id= 'Scatter',
            figure = {
                'data':[
                {'x' : [0,250,500,750,1000,max(sum)],'y':sum,'type':'scatter','name':'FirstChart'}],
                'layout': {
                    'title' : 'Długość'
                }
            }
        ),
    ])
    
    return dash_app