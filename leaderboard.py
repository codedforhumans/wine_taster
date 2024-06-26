from dash import Dash, dcc, html, Input, Output, ctx, State, MATCH, ALL
import plotly.io as pio
import time
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from flask import send_from_directory
import json

pio.templates.default = "plotly_dark"

from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from config.template_functions import tabs_layout
import config.template_css as style
import config.template_dmc as style_dmc

from dash_init import app
from questionnaire import questionnaire
from layout_general import layout

from database import Database

SPACE = html.Br()
SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
SPACE_SMALL = html.Div(style={"padding":"5px"})

def get_new_data():
    global db
    db = Database()

UPDATE_INTERVAL = 3600

def get_new_data_interval():
    while True:
        time.sleep(UPDATE_INTERVAL)

executor = ThreadPoolExecutor(max_workers = 1)
executor.submit(get_new_data_interval)

def layout_leader_sleep():
    return html.Div("Layout Leader Sleeping")

def layout_leader():
    get_new_data()
    return layout()

def layout():
    scoring = db.get_scores_df()
    return html.Div(create_table(scoring))


def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table
