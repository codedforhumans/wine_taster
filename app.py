from dash import Dash, dcc, html, Input, Output, ctx, State
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import flask
from flask import send_from_directory, render_template

from config.template_functions import tabs_layout
import config.template_css as style
from dash_init import app
import requests

pio.templates.default = "plotly_dark"

from admin import layout_admin
from expert import layout_expert
from taster import layout_taster
from about import layout_about
from expert_tasters import EXPERTS
# from login import layout_landing

from dash.exceptions import PreventUpdate
    
roles = ['Expert', 'Taster']
SPACE = html.Br()
SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
SPACE_SMALL = html.Div(style={"padding":"5px"})
SPACE_SMALLER = html.Div(style={"padding":"2px"})

@app.callback(
    Output("content-div", "children"),
    Input("tabs", "value"),
)
def content(tab):
    if tab == "Expert":
        return layout_expert()
    elif tab == "Taster":
        return layout_taster()
    elif tab == "About":
        return layout_about()

# tabs = html.Div([tabs_layout(["Taster", "About"])])

title = html.P("Vyn Taster", style=style.TITLE)

def init_layout(tabs):
    return html.Div(
        [
        html.Div(       
        [
            html.Div([title], style=style.TOPBAR),
            html.Div([tabs], id="topbar-div", style=style.TOPBAR_MENU),  # Topbar (Tabs, Title, ...)
            html.Div("Loading Content...", id="content-div", style=style.CONTENT),  # Content (Loads in body() function)
            html.Div(id="data-div", style={"display": "none"}),  # Invisible Div to store data in json string format
            # html.Link(href='/assets/style.css', rel='stylesheet'),
        ], id="body", style=style.BODY),
    ], style={"width": "100vw", "height": "100vh", "align":"center", "justify-content":"center"})


layout_login = html.Div(
                        [
                            dmc.Stack(
                                [html.Div("Welcome to Vyn Taster"),
                                    dmc.TextInput(label="Your Name", id = 'login-name', withAsterisk = True, style=style.LOGIN_INPUT),
                                    dmc.TextInput(
                                        label="Your Email:", withAsterisk = True, id = 'login-email', style=style.LOGIN_INPUT),
                                        SPACE_SMALLER,
                                        dmc.Anchor(btn_login := dmc.Button("Get Access"), href="/", id = "output1"),
                                ], id='login-stack', style=style.LOGIN_BODY),
                            ], id = 'login-div', style=style.LOGIN_DIV)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
                     ])

app.layout = layout # layout_login




@app.callback(
    Output('url', 'pathname'),
    Input(btn_login, 'n_clicks'),
    Input('login-name', 'value'),
    Input('login-email', 'value'))
def update_output(n_clicks, name_raw, email_raw):
    if n_clicks > 0:
        name = name_raw.lower()
        email = email_raw.lower()
        if name in EXPERTS.keys():
            if EXPERTS[name]==email:
                return "/expert"
            else:
                return "/taster"
        else:
            return "/taster"
    return "/"
    

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == "/":
        return layout_login
    elif pathname == "/expert":
        return init_layout(tabs = html.Div([tabs_layout(["Expert", "About"])]))
    elif pathname == "/taster":
        return init_layout(tabs = html.Div([tabs_layout(["Taster", "About"])]))
    else:
        return init_layout(tabs = html.Div([tabs_layout(["About"])]))

    

server = app.server


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)