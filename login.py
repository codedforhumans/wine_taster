# from dash import Dash, dcc, html, Input, Output, ctx, State, MATCH, ALL
# import plotly.io as pio
# import time
# import dash_bootstrap_components as dbc
# import dash_mantine_components as dmc
# from flask import send_from_directory
# import json

# pio.templates.default = "plotly_dark"

# from concurrent.futures import ThreadPoolExecutor

# import pandas as pd
# from dash.exceptions import PreventUpdate

# from config.template_functions import tabs_layout
# import config.template_css as style
# import config.template_dmc as style_dmc

# from dash_init import app

# SPACE = html.Br()
# SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
# SPACE_SMALL = html.Div(style={"padding":"5px"})

# def get_new_data():
#     global RECOMMEND_GLOBAL
#     RECOMMEND_GLOBAL = "Json Object Coming soon"

# UPDATE_INTERVAL = 3600

# def get_new_data_interval():
#     while True:
#         time.sleep(UPDATE_INTERVAL)

# executor = ThreadPoolExecutor(max_workers = 1)
# executor.submit(get_new_data_interval)

# def layout_landing_sleep():
#     return html.Div("Layout Login Sleeping")

# def layout_landing():
#     get_new_data()
#     return layout

# index_page = html.Div([
#     html.Div(
#         dcc.Input(id="user", type="text", placeholder="Enter Username",className="inputbox1"),
#     ),
#     html.Div(
#         dcc.Input(id="passw", type="text", placeholder="Enter Password",className="inputbox2"),
#     ),
#     html.Div(
#         html.Button('Verify', id='verify', n_clicks=0)),
#     html.Div(id='output1')
#     ])


# layout = html.Div([
#     index_page,
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
#                      ])


# @app.callback(
#     Output('output1', 'children'),
#     Input('verify', 'n_clicks'),
#     State('user', 'value'),
#     State('passw', 'value'))
# def update_output(n_clicks, uname, passw):
#     li={'saruul':'admin123'}
#     if uname =='' or uname == None or passw =='' or passw == None:
#         # return html.Div(children='')
#         raise PreventUpdate
#     if uname not in li:
#         raise PreventUpdate
#         # return html.Div(children='Incorrect Username')
#     if li[uname]==passw:
#         return html.Div(dcc.Link('Access Granted!', href='/expert'))
#     else:
#         raise PreventUpdate
#         # return html.Div(children='Incorrect Password')
    

# next_page = html.Div([
#     html.Div(dcc.Link('Log out', href='/')),
#     html.H1(
#         children="This is the Next Page, the main Page", 
#         className="ap")
#     ])


