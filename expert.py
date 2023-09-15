from dash import Dash, dcc, html, Input, Output, ctx, State, MATCH, ALL
import plotly.io as pio
import time
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from flask import send_from_directory

pio.templates.default = "plotly_dark"

from concurrent.futures import ThreadPoolExecutor

import pandas as pd

from config.template_functions import tabs_layout
import config.template_css as style
import config.template_dmc as style_dmc

from dash_init import app

SPACE = html.Br()
SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
SPACE_SMALL = html.Div(style={"padding":"5px"})

def get_new_data():
    global RECOMMEND_GLOBAL
    RECOMMEND_GLOBAL = "Json Object Coming soon"

UPDATE_INTERVAL = 3600

def get_new_data_interval():
    while True:
        time.sleep(UPDATE_INTERVAL)

executor = ThreadPoolExecutor(max_workers = 1)
executor.submit(get_new_data_interval)

def layout_expert_sleep():
    return html.Div("Layout Expert Sleeping")




questionnaire = {
    1: {
        'type': 'choice',
        'question':
        'Clarity',
        'options': ['Clear', 'Cloudy'],
        'color': 'blue'
    },
    2: {
        'type': 'choice+blank',
        'question':
        'Brightness',
        'options': ['Dull', 'Bright', 'Brilliant'],
        'color': 'yellow'
    },
    3: {
        'type': 'choice',
        'question':
        'Concentration',
        'options': ['Pale', 'Medium', 'Deep', 'Translucent	Opaque'],
        'color': 'orange'
    },
    4: {
        'type': 'multi-choice',
        'question':
        'Evidence of gas or sediment?',
        'options': ['Gas - is it bubbly?', 'Sediment'],
        'color': 'dark'
    },
    5: {
        'type':
        'choice',
        'question':
        'Colour',
        'options': [
            'WHITE', 'straw/lemon', 'yellow', 'gold', 'amber', 'ROSE', 'pink', 'pink orange', 'orange', 'RED', 'purple', 'ruby', 'garnet', 'tawny'
        ],
        'color': 'blue'
    },
    6: { # can hue be multi-choice?
        'type':
        'multi-choice',
        'question':
        'Hue',
        'options': [
            'Silver', 'green', 'orange', 'blue', 'brown'
        ],
        'color': 'grape'
    },
    7: {
        'type':
        'choice',
        'question':
        'Rim',
        'options': [
            'Obvious', 'not obvious'
        ],
        'color': 'pink'
    },
    8: {
        'type':
        'choice',
        'question':
        'Stain/Extract',
        'options': [
            'none', 'light', 'medium', 'heavy'
        ],
        'color': 'red'
    },
    9: {
        'type':
        'choice',
        'question':
        'Viscosity/Tears',
        'options': [
            'Low', 'Medium', 'High'
        ],
        'color': 'orange'
    },
    10: {
        'type':
        'choice',
        'question':
        'Intensity',
        'options': [
            'Delicate', 'Moderate', 'Powerful'
        ],
        'color': 'green'
    },
    11: {
        'type':
        'multi-choice',
        'question':
        'Faults',
        'options': [
            'TCA', 'H2S', 'Volatile', 'Acidity', 'Brett', 'Oxidation', 'Other'
        ],
        'color': 'dark'
    },
    12: {
        'type':
        'slider',
        'question':
        'Sweetness',
        'options': [
            'dry',
            'off-dry',
            'medium',
            'sweet',
            'very sweet'
        ],
        'color': 'grape'
    },
    13: {
        'type':
        'slider',
        'question':
        'Tannin',
        'options': [
            'Ripe',
            'Unripe',
            'Smooth',
            'Course',
            'Stalky',
            'Chalky',
            'Fine grained'
        ],
        'color': 'grape'
    },
    14: {
        'type':
        'slider',
        'question':
        'Acidity',
        'options': [
            'Low',
            'Soft',
            'Moderate',
            'Balanced',
            'Crisp',
            'Sharp'
        ],
        'color': 'blue'
    },
    15: {
        'type':
        'slider',
        'question':
        'Alcohol',
        'options': [
            'Low',
            'Restrained',
            'Medium',
            'Medium+',
            'High'
        ],
        'color': 'dark'
    },
}

multi_choice_q = {k: v for k, v in questionnaire.items() if v['type'] == 'multi-choice'}
single_choice_q = {k: v for k, v in questionnaire.items() if v['type'] == 'choice'}
slider_q = {k: v for k, v in questionnaire.items() if v['type'] == 'slider'}

layout_single = html.Div(
    [
        html.Div([html.Div(v['question'])] + [
            dmc.ChipGroup(
                [
                    dmc.Chip(
                        x,
                        value=x,
                        variant="outline",
                        color=v['color']
                    )
                    for x in v['options']
                ],
                id = {'index': k, 'type': v['type']},
                multiple=False,
                mb=10,
                )
            ] + [SPACE]) for k, v in single_choice_q.items()
    ]
)

layout_multi = html.Div(
    [
        html.Div([html.Div(v['question'])] + [
            dmc.ChipGroup(
                [
                    dmc.Chip(
                        x,
                        value=x,
                        variant="outline",
                        # styles=style_dmc.style,
                        color=v['color']
                    )
                    for x in v['options']
                ],
                id = {'index': k, 'type': v['type']},
                multiple=True,
                mb=10,
                )
            ] + [SPACE]) for k, v in multi_choice_q.items()
    ]
)

layout_slider = html.Div(
    [
        html.Div([html.Div(v['question'])] + [
            dcc.Slider(
                id={'index': k, 'type': v['type']},
                value = 0,
                marks={
                        int(val * 100/(len(v['options']) - 1)): 
                            {'label': v['options'][val], 
                            "style": {"transform": "rotate(-25deg)"}}
                    for val in range(len(v['options']))
                       },
                # marks = [
                #     {"value": val * 100/(len(v['options']) - 1), "label": v['options'][val]}
                    # for val in range(len(v['options']))
                # ],
                step=100/(len(v['options']) - 1)
                # mb=20,
        )
            ] + [SPACE]) for k, v in slider_q.items()
    ]
)



layout = html.Div([layout_single, layout_multi, layout_slider], style = style.HOME)


def layout_expert():
    get_new_data()
    return layout



@app.callback(
    Output("chips-values-output", "children"),
    Input("chips-callback", "value"),
)
def chips_values(value):
    return ", ".join(value) if value else None

















# def generate(k, v):
#     match v['type']:
#         case 'choice':
#             return html.Div([html.P(str(k)+'. '+v['question']), dcc.RadioItems(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False}, options={i: i for i in v['options']})])
#         case 'multi-choice':
#             return html.Div([html.P(str(k)+'. '+v['question']), dcc.Checklist(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False}, options={i: i for i in v['options']})])
#         case 'choice+blank':
#             return html.Div([html.P(str(k)+'. '+v['question']), dcc.RadioItems(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False}, options={i: i for i in v['options']}), dcc.Input(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':True}, disabled=True)])
#         case 'blank':
#             return html.Div([html.P(str(k)+'. '+v['question']), dcc.Input(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False})])
#         case 'essay':
#             return html.Div([html.P(str(k)+'. ' + v['question']), dcc.Textarea(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False})])
#         case _:
#             return html.Div('Something wrong...')

# layout = html.Div([generate(k, v) for k, v in questionnaire.items()] +
#                       [html.Br(), btn := html.Button('Submit'), answers := html.Div()])


# def layout_expert():
#     get_new_data()
#     return layout


# @app.callback(
#     Output(
#         {
#             'category': 'questionnaire',
#             'type': 'choice+blank',
#             'additional': True,
#             'index': MATCH
#         }, 'disabled'),
#     Input(
#         {
#             'category': 'questionnaire',
#             'type': 'choice+blank',
#             'additional': False,
#             'index': MATCH
#         }, 'value'))
# def disabled_input(v):
#     return False if v == 'Yes' else True


# @app.callback(
#     Output(
#         btn, 'disabled'),
#     Input(
#         {
#             'category': 'questionnaire',
#             'type': ALL,
#             'additional': False,
#             'index': ALL
#         }, 'value'))
# def disabled_btn(answer):
#     return False if all(answer) else True


# @app.callback(Output(answers, 'children'), Input(btn, 'n_clicks'), [
#     State(
#         {
#             'category': 'questionnaire',
#             'type': ALL,
#             'additional': ALL,
#             'index': ALL
#         }, 'id'),
#     State(
#         {
#             'category': 'questionnaire',
#             'type': ALL,
#             'additional': ALL,
#             'index': ALL
#         }, 'value')
# ], prevent_initial_call=True)
# def collect(n_clicks, index, answer):
#     return str([v | {'answer': answer[i]} for i, v in enumerate(index)])


