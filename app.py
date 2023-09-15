from dash import Dash, dcc, html, Input, Output, ctx
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
from flask import send_from_directory

from config.template_functions import tabs_layout
import config.template_css as style
from dash_init import app

pio.templates.default = "plotly_dark"

from admin import layout_admin
from expert import layout_expert
from taster import layout_taster
from about import layout_about

@app.callback(
    Output("content-div", "children"),
    Input("tabs", "value"),
)
def content(tab):
    if tab == "Expert":
        return layout_expert()
    elif tab == "About":
        return layout_about()
    
title = html.P("Vyn Taster", style=style.TITLE)

tabs = html.Div([tabs_layout(["Expert", "About"])])

def layout():
    return html.Div([
        html.Div([
            html.Div([title], style=style.TOPBAR),
            html.Div([tabs], id="topbar-div", style=style.TOPBAR_MENU),  # Topbar (Tabs, Title, ...)
            html.Div("Loading Content...", id="content-div", style=style.CONTENT),  # Content (Loads in body() function)
            html.Div(id="data-div", style={"display": "none"}),  # Invisible Div to store data in json string format
            # html.Link(href='/assets/style.css', rel='stylesheet'),
        ], id="body", style=style.BODY),
    ], style={"width": "100vw", "height": "100vh", "align":"center", "justify-content":"center"})


app.layout = layout()
server = app.server

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)