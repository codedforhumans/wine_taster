from dash import Dash, dcc, html, Input, Output, ctx, State
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import flask
import json
import os
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
from expert_tasters import EXPERTS, TASTERS
from database import Database
from leaderboard import layout_leader
# from login import layout_landing

from dash.exceptions import PreventUpdate
    
roles = ['Expert', 'Taster']
SPACE = html.Br()
SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
SPACE_SMALL = html.Div(style={"padding":"5px"})
SPACE_SMALLER = html.Div(style={"padding":"2px"})

db = Database()

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
    elif tab == "Leaderboard":
        return layout_leader()

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
                                        label="Your Phone Number:", withAsterisk = True, id = 'login-phone', style=style.LOGIN_INPUT),
                                        SPACE_SMALLER,
                                        dmc.Anchor(btn_login := dmc.Button("Get Access"), href="/", id = "output1"),
                                ], id='login-stack', style=style.LOGIN_BODY),
                            ], id = 'login-div', style=style.LOGIN_DIV)

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
                     ])



def write_user_json(name, phone) -> None:
    info_dict = {"name": name, "phone": phone}
    with open('user_info.json', 'w') as fp:
        json.dump(info_dict, fp)
        print("User Info Saved to File")

def clear_user_info_json():
    open('user_info.json', 'w').close()


def user_info_empty():
    if os.path.exists('user_info.json'):
        data = None
        try:
            # Open the JSON file for reading
            with open('user_info.json', 'r') as json_file:
                # Load the JSON data
                data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            return True

        # Check if the JSON data is empty
        if not data:
            print("user_info.json is empty")
            return True
        else:
            print("user_info.json is not empty")
            return False
    else:
        print("user_info.json does not exist")
        return True


@app.callback(
    Output('url', 'pathname'),
    Input(btn_login, 'n_clicks'),
    Input('login-name', 'value'),
    Input('login-phone', 'value'))
def update_output(n_clicks, name_raw, phone_raw):
    if n_clicks > 0:
        name = name_raw.lower()
        phone = int(phone_raw)
        write_user_json(name, phone)
        if name in EXPERTS.keys():
            print("name in expert")
            print(phone)
            if EXPERTS[name]==phone:
                return "/expert"
            else:
                return "/"
        elif name in TASTERS.keys():
            if TASTERS[name]==phone:
                return "/taster"
            else:
                return "/"
        else:
            return "/"
    return "/"
    

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == "/":
        clear_user_info_json()
        return layout_login
    elif pathname == "/expert":
        if not user_info_empty():
            return init_layout(tabs = html.Div([tabs_layout(["Expert", "About", "Leaderboard"])]))
        else:
            return layout_login
    elif pathname == "/taster":
        if not user_info_empty():
            return init_layout(tabs = html.Div([tabs_layout(["Taster", "About"])]))
        else:
            return layout_login
    else:
        return init_layout(tabs = html.Div([tabs_layout(["About"])]))

server = app.server
app.layout = layout # layout_login


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=False)