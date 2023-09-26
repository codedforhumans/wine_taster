from dash import Dash, dcc, html, Input, Output, ctx, State, MATCH, ALL
import plotly.io as pio
import time
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
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
from database import Database
from calculations import Scorer, get_taster_data, get_expert_data

db = Database()

SPACE = html.Br()
SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
SPACE_SMALL = html.Div(style={"padding":"5px"})

def get_new_data():
    global RECOMMEND_GLOBAL, questions
    questions = db.get_wine_ids()
    RECOMMEND_GLOBAL = "Json Object Coming soon"


UPDATE_INTERVAL = 3600

def get_new_data_interval():
    while True:
        time.sleep(UPDATE_INTERVAL)

executor = ThreadPoolExecutor(max_workers = 1)
executor.submit(get_new_data_interval)

# questionnaire = db.get_questionnaire()

def layout_expert_sleep():
    return html.Div("Layout Expert Sleeping")

def layout_expert():
    get_new_data()
    return layout

warning_text = "Please choose generic descriptors first before granular descriptors"


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
                id = {'index': str(k), 'type': v['type'], 'additional': False},
                multiple=False,
                mb=10
                )
            ] + 
            [
                html.Div(id={'index': str(k), 'type': v['type'], 'additional': True})
            ]
        +  [SPACE]) for k, v in single_choice_q.items()
    ]
)

layout_multi = html.Div(
    [
        html.Div([html.Div(v['question'])] + [dmc.Text(warning_text, size="sm") if v['warning'] == True else html.Div(style={'display':'none'})] + [
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
                id = {'index': str(k), 'type': v['type'], 'additional': False},
                multiple=True,
                mb=10
                )
            ] + 
            [
                html.Div(id={'index': str(k), 'type': v['type'], 'additional': True})
            ]
        +  [SPACE]) for k, v in multi_choice_q.items()
    ]
)

layout_slider = html.Div(
    [
        html.Div([html.Div(v['question'])] + [
            dcc.Slider(
                id={'index': str(k), 'type': v['type'], 'additional': False},
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
                html.Div(id={'index': str(k), 'type': v['type'], 'additional': True})
            ]
        + [SPACE]) for k, v in slider_q.items()
    ]
)

# def get_wine_name():
    
#     result = html.Div([
#                 dmc.Select(
#                     data = questions,
#                     value = questions[0],
#                     label = "Wine",
#                     style = style.DROPDOWN,
#                     icon = DashIconify(icon="radix-icons:magnifying-glass"),
#                     rightSection = DashIconify(icon="radix-icons:chevron-down"),
#                     id="select-wine"),
#                     SPACE
#                 ])
#     return result

# layout_wine_name = get_wine_name()

def layout_wine_name(questions):
    result = html.Div([
                dmc.Select(
                    data = questions,
                    value = questions[0],
                    label = "Wine",
                    style = style.DROPDOWN,
                    icon = DashIconify(icon="radix-icons:magnifying-glass"),
                    rightSection = DashIconify(icon="radix-icons:chevron-down"),
                    id="select-wine"),
                    SPACE
                ])
    return result

layout_answer = html.Div([html.Br(), btn := dmc.Button("Submit", variant="gradient"), answers := html.Div()])
layout_answer_taster = html.Div([html.Br(), btn_taster := dmc.Button("Submit", variant="gradient"), answers_taster := html.Div()])

def layout(questions):
    return html.Div([layout_wine_name(questions),
    layout_single, layout_multi, 
    layout_slider, 
                   layout_answer
                   ], style = style.HOME)

layout_taster_general = html.Div([
    layout_single, layout_multi, 
    layout_slider, 
                   layout_answer_taster
                   ], style = style.HOME)




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
                                id = {'index': id['index'], 'type': id['type'], 'additional': True},
                                
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
            val_index = choices.index(val) + 1 # Python 0-index -> Regular 1-index 
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
                                    id = {'index': str(id['index']) + "_" + str(val_index), 'type': id['type'], 'additional': True},
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
    label = marks[str(int(val))]['label']
    values = slider_q[id['index']]['options'][label]
    color = slider_q[id['index']]['color']
    if len(values) > 0:
        return html.Div([
                    dmc.Text(text, size="xs", color="gray") for text in values
                ], style = {"padding": style.INDENT})
    else:
        return html.Div(style={'display':'none'})




@app.callback(
    Output(
        btn, 'disabled'),
    Input(
        {'index': ALL,
            # 'category': 'questionnaire',
            'type': ALL,
            'additional': False
        }, 'value'))
def disabled_btn(answer):
    return False if any(answer) else True


@app.callback(Output(answers, 'children'), 
                Input(btn, 'n_clicks'), 
                [State(
                    {'index': ALL,
                        # 'category': 'questionnaire',
                        'type': ALL,
                        'additional': ALL,
                        
                    }, 'id'),
                State(
                    {'index': ALL,
                        # 'category': 'questionnaire',
                        'type': ALL,
                        'additional': ALL,
                    }, 'value')
                ], 
                # prevent_initial_call=True
                )
def collect(n_clicks, id, answer):
    if n_clicks:
        result = [v | {'answer': answer[i]} for i, v in enumerate(id)]
        json_object = json.dumps(result)
        json_result = json.dumps({'results': json_object})

        # Writing to sample.json
        with open("expert.json", "w") as outfile:
            outfile.write(json_result)
            outfile.close()
        return html.Div([SPACE, html.Div(done_message), html.Div(id = "send-result")])


done_message = "Expert Tasting Notes Successfully Submitted. Thank you."



@app.callback(
    Output(
        btn_taster, 'disabled'),
    Input(
        {'index': ALL,
            # 'category': 'questionnaire',
            'type': ALL,
            'additional': False
        }, 'value'))
def disabled_btn(answer_taster):
    return False if any(answer_taster) else True


@app.callback(Output(answers_taster, 'children'), 
                Input(btn_taster, 'n_clicks'), 
                [State(
                    {'index': ALL,
                        # 'category': 'questionnaire',
                        'type': ALL,
                        'additional': ALL,
                        
                    }, 'id'),
                State(
                    {'index': ALL,
                        # 'category': 'questionnaire',
                        'type': ALL,
                        'additional': ALL,
                    }, 'value')
                ], 
                # prevent_initial_call=True
                )
def collect(n_clicks, id, answer):
    if n_clicks:
        result = [v | {'answer': answer[i]} for i, v in enumerate(id)]
        json_object = json.dumps(result)
        json_result = json.dumps({'results': json_object})

        # Writing to sample.json
        with open("taster.json", "w") as outfile:
            outfile.write(json_result)
        return html.Div([SPACE, score_div(), html.Div(id = "send-result")])

def score_div():
    scorer = Scorer()
    score_perc = scorer.get_score()
    score_summary = scorer.get_summary_taster_view().fillna("-")
    return html.Div([SPACE,
                     html.Div("Score: " + str(score_perc) + "%"),
                     html.Div("Comparison:"),
                     html.Div(create_table(score_summary))
                     ])

font_size = "6px"
expert_answer = "Expert Answer"
taster_answer = "Taster Answer"
question = "Question"

def create_table(df):
    results = []
    for ind, row in df.iterrows():
        question_text = row[question]
        expert_text = row[expert_answer]
        taster_text = row[taster_answer]
        result = html.Div([
            html.Div([
                dmc.Text("Question: " + str(question_text), weight=700),
                ], style=style.RESULT_DIV),
                SPACE,
            html.Div([
                dmc.Text("Expert: " + str(expert_text)),
                ], style=style.RESULT_DIV),
                SPACE,
            html.Div([
                dmc.Text("Taster: " + str(taster_text)),
                ], style=style.RESULT_DIV),
            SPACE,SPACE,
            ])
        results += [result]
    return html.Div(results)


@app.callback(
        Output("send-result", "children"),
        # Input('login-name', 'value'),
        # Input('login-email', 'value'),
        Input('url', 'pathname'),
        Input("select-wine", "value"),
        Input(btn, 'n_clicks'), 
                [State(
                    {'index': ALL,
                        # 'category': 'questionnaire',
                        'type': ALL,
                        'additional': ALL,
                        
                    }, 'id'),
                State(
                    {'index': ALL,
                        # 'category': 'questionnaire',
                        'type': ALL,
                        'additional': ALL,
                    }, 'value')
                ], 
                # prevent_initial_call=True
)
def send_results(pathname, drink_name, n_clicks, id, answer): # name, email,
    if n_clicks:
        result = [v | {'answer': answer[i]} for i, v in enumerate(id)]

        print("result")
        print(result)
        role_type = pathname[1:] # ignore pathname /
        dict_submit = {}
        name = "tamara"
        email = "tamara@codedforhumans.com"

        for curr_dict in result:
            print(curr_dict)
            index = curr_dict["index"]
            additional = curr_dict["additional"]
            answer = curr_dict["answer"]
            if additional:
                dict_submit[index + "_additional"] = answer
            else:
                dict_submit[index] = answer
        

        print("dict_submit")
        print(dict_submit)

        if role_type == "expert":
            # expert_data = get_expert_data()
            # print(expert_data)
            db.submit_user_input(name, email, role_type, drink_name, dict_submit)
            return html.Div("Submitted Expert Data")
        elif role_type == "taster":
            db.submit_user_input(name, email, role_type, drink_name, dict_submit)
            return html.Div("Submitted Taster Data")
        else:
            return html.Div("")