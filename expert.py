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

warning_text = "Please choose generic descriptors first before granular descriptors"

questionnaire = {
    1: {
        'type': 'choice',
        'question':
        'Clarity',
        'options': {'Clear':[], 'Cloudy':[]},
        'color': 'blue',
        'additional': False,
        'warning' : False
    },
    2: {
        'type': 'choice',
        'question':
        'Brightness',
        'options': {'Dull':[], 'Bright':[], 'Brilliant':[]},
        'color': 'yellow',
        'additional': False,
        'warning' : False
    },
    3: {
        'type': 'choice',
        'question':
        'Intensity',
        'options': {'Pale':[], 'Medium':[], 'Deep':[]},
        'color': 'orange',
        'additional': False,
        'warning' : False
    },
    4: {
        'type': 'multi-choice',
        'question':
        'Evidence of gas or sediment?',
        'options': {'Gas - is it bubbly?':[], 'Sediment':[]},
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    5: {
        'type':
        'choice',
        'question':
        'Colour',
        'options': {
            'White':['straw/lemon', 'yellow', 'gold', 'amber'], 
            'Rose':['pink', 'pink orange', 'orange'], 
            'Red':['purple', 'ruby', 'garnet', 'tawny']
        },
        'color': 'blue',
        'additional': False,
        'warning' : False
    },
    6: {
        'type':
        'choice',
        'question':
        'Hue',
        'options': 
            {'Silver':[], 'green':[], 'orange':[], 'blue':[], 'brown':[]}
        ,
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    7: {
        'type':
        'choice',
        'question':
        'Rim',
        'options': 
            {'Obvious':[], 'not obvious':[]}
        ,
        'color': 'pink',
        'additional': False,
        'warning' : False
    },
    8: {
        'type':
        'choice',
        'question':
        'Stain/Extract',
        'options': 
            {'none':[], 'light':[], 'Medium':[], 'heavy':[]}
        ,
        'color': 'red',
        'additional': False,
        'warning' : False
    },
    9: {
        'type':
        'choice',
        'question':
        'Viscosity/Tears',
        'options':
            {'Low':[], 'Medium':[], 'High':[]}
        ,
        'color': 'orange',
        'additional': False,
        'warning' : False
    },
    10: {
        'type':
        'choice',
        'question':
        'Intensity',
        'options':
            {'Delicate':[], 'Moderate':[], 'Powerful':[]},
        'color': 'green',
        'additional': False,
        'warning' : False
    },
    11: {
        'type':
        'multi-choice',
        'question':
        'Faults',
        'options':
            {'TCA':[], 'H2S':[], 'Volatile':[], 'Acidity':[], 'Brett':[], 'Oxidation':[], 'Other':[]},
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    12: {
        'type':
        'slider',
        'question':
        'Sweetness',
        'options': {
            'dry':["<4g/L: little to no perceptible residual sugar. As sweet as plain bread, raw celery or radish"],
            'off-dry':["4-15ml/L: hint of sweetness. As sweet as ripe white nectarine"],
            'medium':["15-75mg/L: noticeably sweet but not excessively so. As sweet as table grapes or teriyaki sauce"],
            'sweet':["75-120mg/L: Obviously sweet, As sweet as very ripe strawberries or jam"],
            'very sweet':[">120mg/L: intensely sweet. Comparable sweetness to dried dates, honey, baklava"]
        },
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    13: {
        'type':
        'slider',
        'question':
        'Tannin',
        'options': {
            'Ripe':["Low: Soft, smooth, no noticable astringency. Milk chocolate or banana"],
            'Unripe':["Soft mouthfeel, no assertive tannins (moderate), lightly brewed or milk tea, watermelon or fresh red capsicum "],
            'Smooth':["Tanins provide structure and a slight grip on the palate without being overwhelming. Pear or dark chocolate "],
            'Course':["Firm structure and a noticeable astringency. Walnuts or black coffee"],
            'Stalky':["Very dry, very firm and grippy texture. Strongly brewed black tea or a black teabag on the tongue"],
            'Chalky':[],
            'Fine grained':[]
        },
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    14: {
        'type':
        'slider',
        'question':
        'Acidity',
        'options': {
            'Low':[],
            'Soft':["round, less crisp. Cooked, unflavoured white rice "],
            'Moderate':["(lacks freshness) fresh cucumber"],
            'Balanced':["balanced level of tartness, ripe tomato"],
            'Crisp':["fresh and crisp, freshly squeezed lemon juice or fresh tart green apple"],
            'Sharp':["fresh, vibrant, sharp, zesty, grapefruit or white vinegar"]
        },
        'color': 'blue',
        'additional': False,
        'warning' : False
    },
    15: {
        'type':
        'slider',
        'question':
        'Alcohol',
        'options': {
            'Low':[">11%ABV. Fresh easy drinking, light body, delicate crisp character."],
            'Restrained':["11-12.5% ABV: moderate to light alcohol pleasant roundness and structure "],
            'Medium':["12.5-13.5 % ABV: good balance between fruitiness and body. They often exhibit depth and complexity."],
            'Medium+':["13.5-14.5% ABV: fuller-bodied, warming sensation, showcase ripe, rich fruit flavors."],
            'High':[">14.5% ABV: robust and powerful, noticeable warmth, concentrated flavors and complexity."]
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    16: {
        'type':
        'multi-choice',
        'question':
        'Primary',
        'options': {
            'floral': ['blossom', 'elderflower', 'honeysuckle', 'jasmine', 'rose', 'violet'],
            'green fruit': ['apple', 'pear', 'gooseberry', 'grape'],
            'Citrus': ['grapefruit', 'lemon', 'lime', 'orange'],
            'stone fruit': ['peach', 'apricot', 'nectarine'],
            'tropical fruit': ['banana', 'lychee', 'mango', 'melon', 'passion fruit', 'pineapple'],
            'red fruit': ['red currant', 'cranberry', 'raspberry', 'strawberry', 'red cherry', 'red plum'],
            'black fruits': ['blackcurrant', 'blackberry', 'blueberry', 'black cherry', 'black plum'],
            'herbaceous': ['green capsicum', 'grass', 'tomato leaf', 'asparagus'],
            'herbal': ['eucalyptus', 'mint', 'fennel', 'dill', 'dried herbs' ],
            'fruit ripeness': ['unripe', 'ripe']
        },
        'color': 'dark',
        'additional': False,
        'warning' : True
    },
    17: {
        'type':
        'multi-choice',
        'question':
        'Secondary',
        'options': {
            'spice': ['black pepper', 'white pepper', 'liquorice', 'cinnamon'], 
            'yeast': ['biscuit', 'graham cracker', 'bread', 'toasted bread', 'pastry', 'brioche', 'bread dough', 'cheese', 
                      'yoghurt', 'acetaldehyde'], 
            'MLC': ['butter', 'cream', 'cheese' ], 
            'Oak': ['vanilla', 'cloves', 'coconut', 'cedar', 'charred wood', 'smoke', 'chocolate', 'coffee'],
        },
        'color': 'dark',
        'additional': False,
        'warning' : True
    },
    18: {
        'type':
        'multi-choice',
        'question':
        'Tertiary',
        'options': {
            'Tertiary white': ['dried fruit (apricot, raisin)', 'orange marmalade', 'petrol/gasoline', 'cinnamon', 'ginger', 
                               'nutmeg', 'almond', 'hazelnut', 'honeysuckle', 'caramel', 'dried fruit (prune, raisin, fig)', 
                               'cooked fruit (plum, cherry)', 'leather', 'earth', 'mushrooms', 'meat', 'tobacco', 'wet leaves', 
                               'forest floor', 'caramel'], 
            'Oxidised': ['almond', 'hazelnut', 'walnut', 'chocolate', 'coffee', 'caramel']
        },
        'color': 'dark',
        'additional': False,
        'warning' : True
    },
    19: {
        'type':
        'choice',
        'question':
        'Quality Balance',
        'options': {
            'Unbalance (any element dominates)': [],
            'well balanced':[],
            'Exceptionally well balanced':[]
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    20: {
        'type':
        'choice',
        'question':
        'Quality Length',
        'options': {
            'short': [],
            'medium':[],
            'long':[],
            'outstanding':[]
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    21: {
        'type':
        'choice',
        'question':
        'Quality Intensity',
        'options': {
            'low': [],
            'medium':[],
            'high':[]
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    22: {
        'type':
        'choice',
        'question':
        'Quality Complexity',
        'options': {
            'low': [],
            'medium':[],
            'high':[]
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
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
                        color=v['color'],
                        # id = {'parent': x}
                    )
                    for x in v['options']
                ],
                id = {'index': k, 'type': v['type'], 'additional': False},
                multiple=False,
                mb=10
                )
            ] + 
            [
                html.Div(id={'index': k, 'type': v['type'], 'additional': True})
            ]
        +  [SPACE]) for k, v in single_choice_q.items()
    ]
)

layout_multi = html.Div(
    [
        html.Div([html.Div(v['question'])] + [html.Div(warning_text) if v['warning'] == True else html.Div(style={'display':'none'})] + [
            dmc.ChipGroup(
                [
                    dmc.Chip(
                        x,
                        value=x,
                        variant="outline",
                        color=v['color'],
                    )
                    for x in v['options']
                ],
                id = {'index': k, 'type': v['type'], 'additional': False},
                multiple=True,
                mb=10
                )
            ] + 
            [
                html.Div(id={'index': k, 'type': v['type'], 'additional': True})
            ]
        +  [SPACE]) for k, v in multi_choice_q.items()
    ]
)

layout_slider = html.Div(
    [
        html.Div([html.Div(v['question'])] + [
            dcc.Slider(
                id={'index': k, 'type': v['type'], 'additional': False},
                value = 0,
                marks={
                        int(val * 100/(len(v['options']) - 1)): 
                            {'label': list(v['options'].keys())[val], 
                            "style": {"transform": "rotate(-25deg)"}}
                    for val in range(len(v['options']))
                       },
                step=100/(len(v['options']) - 1),
                # mb=20,
        )
            ] + 
            [
                html.Div(id={'index': k, 'type': v['type'], 'additional': True})
            ]
        + [SPACE]) for k, v in slider_q.items()
    ]
)


layout = html.Div([layout_single, layout_multi, layout_slider], style = style.HOME)


def layout_expert():
    get_new_data()
    return layout


@app.callback(
    Output(
        {
            'index': MATCH,
            'type': 'choice',
            'additional': True
        }, 'children'),
    Input(
        {
            'index': MATCH, 
            'type': 'choice', 
            'additional': False
        }, 'value'),
    State(
        {
            'index': MATCH, 
            'type': 'choice', 
            'additional': False
        }, 'id'),
)
def disabled_input(val, id):
    if val is not None:
        values = single_choice_q[id['index']]['options'][val]
        color = single_choice_q[id['index']]['color']
        if len(values) != 0:
            return html.Div([html.Div(val),
                        dmc.ChipGroup(
                                [
                                    dmc.Chip(
                                    y,
                                    value=y,
                                    variant="outline",
                                    color=color,
                                    ) for y in values if len(y) > 0
                                ],
                                multiple=False,
                                mb=10)
                    ], style = {"padding": style.INDENT})
        else:
            return html.Div(style={'display':'none'})
    return html.Div(style={'display':'none'})


@app.callback(
    Output(
        {
            'index': MATCH,
            'type': 'multi-choice',
            'additional': True
        }, 'children'),
    Input(
        {
            'index': MATCH, 
            'type': 'multi-choice', 
            'additional': False
        }, 'value'),
    State(
        {
            'index': MATCH, 
            'type': 'multi-choice', 
            'additional': False
        }, 'id')
)
def disabled_input_multi(choices, id):
    if choices is not None:
        result = []
        for val in choices:
            values = multi_choice_q[id['index']]['options'][val]
            color = multi_choice_q[id['index']]['color']
            if len(values) > 0:
                result += [html.Div(val)] + [html.Div([
                            dmc.ChipGroup(
                                    [
                                        dmc.Chip(
                                        y,
                                        value=y,
                                        variant="outline",
                                        color=color,
                                        ) for y in values
                                    ],
                                    multiple=True,
                                    mb=10)
                        ])]
        if len(result) != 0:
            return html.Div(result, style = {"padding": style.INDENT})
        else:
            return html.Div(style={'display':'none'})
    else:
        return html.Div(style={'display':'none'})
    

@app.callback(
    Output(
        {
            'index': MATCH,
            'type': 'slider',
            'additional': True
        }, 'children'),
    Input(
        {
            'index': MATCH, 
            'type': 'slider', 
            'additional': False
        }, 'value'),
    State(
        {
            'index': MATCH, 
            'type': 'slider', 
            'additional': False
        }, 'marks'),
    State(
        {
            'index': MATCH, 
            'type': 'slider', 
            'additional': False
        }, 'id')
)
def disabled_input_slider(val, marks, id):
    label = marks[str(val)]['label']
    values = slider_q[id['index']]['options'][label]
    color = slider_q[id['index']]['color']
    if len(values) > 0:
        return html.Div([
                    html.Div(text) for text in values
                ], style = {"padding": style.INDENT})
    else:
        return html.Div(style={'display':'none'})













# def generate(k, v):
#     match v['type']:
#         case 'choice':
#             return html.Div([html.P(str(k)+'. '+v['question']), dcc.RadioItems(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False}, options={i: i for i in v['options']})])
#         case 'multi-choice':
#             return html.Div([html.P(str(k)+'. '+v['question']), dcc.Checklist(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False}, options={i: i for i in v['options']})])
#         case 'choice+blank':
            # return html.Div([html.P(str(k)+'. '+v['question']), dcc.RadioItems(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':False}, options={i: i for i in v['options']}), dcc.Input(id={'index': k, 'type': v['type'], 'category':'questionnaire', 'additional':True}, disabled=True)])
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


