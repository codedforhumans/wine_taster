from dash import Dash, dcc, html, Input, Output, ctx
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from flask import send_from_directory

pio.templates.default = "plotly_dark"

from dash import Dash, dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.io as pio

import pandas as pd

from config.template_functions import tabs_layout
import config.template_css as style
from database import Database

SPACE = html.Br()
SPACE_INPUTS = html.Div(style={"padding-bottom":"10px"})
SPACE_SMALL = html.Div(style={"padding":"5px"})
SPACE_SMALLER = html.Div(style={"padding":"2px"})

db = Database()

def layout_about():
    return html.Div([
        html.Div("This app is intended to support an amateur tasting game and help participants explore the world of Riesling from around the world."),
        SPACE,
        html.Div("We hope this exercise can inspire fun and learning! We have structured each bracket of the tasting to encourage participants to better understand the difference between key attributes in the wines, from flavour profile to different levels of acidity, quality, residual sugar and alcohol."),
        SPACE,
        html.Div("Each taster can input their assessment of the wine, in a quick, easy to use dashboard with descriptions of each element. Further detail on descriptions can be seen below. This will then be compared with the ‘expert’ answer key and other tasters perceptions. The taster can then use the cheat sheet and their tasting impression to guess where the wine might come from."),
        SPACE,
        html.Div("There will be prizes for"),
        html.Div([
            dmc.List(
            [
                dmc.ListItem("the person who inputs answers closes to the experts (on average)."),
                dmc.ListItem("the person who guesses the highest number of wines correctly."),
                dmc.ListItem("wine that the group rates as most enjoyable."),
            ]
        )
        ]),
        SPACE,
        html.Div("The answer for each classic style of wine is based on:"),
        html.Div([
            dmc.List(
            [
                dmc.ListItem("expert taster input (second year MW candidate), checked by a WSET diploma candidate."),
                dmc.ListItem("alignment with curriculum notes from two leading sommelier tasting associations (we are not affiliated, but align our answers to information in their guides)."),
                dmc.ListItem("a food scientist who has mapped perceptible taste of wine compounds in Riesling (based on relevant scientific literature) to typical regional expressions of the grape."),
                dmc.ListItem("inclusion of references of prominent expert reviewers on a specific wine."),
            ]
        )
        ]),
        SPACE,
        html.Div("Personal data privacy: Phone numbers and names are used only as a means for each party to login to their account and can be deleted or changed on request. Data for an individuals own account can be downloaded on request."),
        SPACE,
        html.Div("Thank you for participating – we hope you have fun!"),
        SPACE,
        html.Div("TASTING CHEAT SHEET"),
        html.Div("Clarity and Brightness: When assessing white Riesling wines, start by checking for clarity – it should be crystal clear, not cloudy. To distinguish between brightness levels, look for the brilliance in the wine's colour. A bright Riesling will have a lively, gleaming appearance, while a brilliant one will practically shimmer in the glass, often indicating a fresher and more vibrant taste."),
        SPACE,
        html.Div("Intensity of Colour: For Riesling, intensity can vary from pale to medium to deep. Choose based on your preference: pale Rieslings are light and delicate, while deeper ones tend to have richer flavours."),
        SPACE,
        html.Div("Hue: Hue refers to the color of the wine. Rieslings can range from pale green to golden yellow. The hue might hint at the wine's age – younger Rieslings tend to be lighter, while older ones may show more golden hues."),
        SPACE,
        html.Div("Viscosity: Viscosity refers to a wine's thickness or 'legs' when swirled in the glass. In the case of Riesling, Alsacian versions often exhibit higher viscosity, creating more pronounced legs, which can help distinguish them from wines produced elsewhere."),
        SPACE,
        html.Div("Flavour/Aroma Profiles: Different flavours reflect regional differences of the wine and often are associated with specific compounds in the wine. When describing flavors make sure they're meaningful and reproducible, and start with the highest level of flavour category first. For example, the taste of green/tree fruits, specifically green apple in Riesling can be linked to its high levels of malic acid, giving it that crisp, fruity character. Remember, finding these familiar flavors helps interpret the wine's profile for others."),
        SPACE,
        html.Div("Flavour profiles can help tasters deduce what region the wine may be from. For example, an Austrian Riesling might showcase flavors of green apple and white pepper, reflecting its cool climate. In contrast, a Clare Valley Riesling from Australia might emphasize lime and citrus notes, signifying a warmer climate. Meanwhile, a Washington State Riesling could display ripe peach and apricot flavors, indicative of its moderate climate conditions. These distinct flavor profiles are influenced by the grape's ripening conditions, which vary with climate."),
        SPACE,
        html.Div("Phenolics: Phenolic compounds, which include tannins and other polyphenols, are influenced by factors like climate and grape ripeness. In cooler climates, grapes may not fully ripen, leading to lower phenolic levels. This results in wines with less texture and mouthfeel. Warmer climates, on the other hand, allow grapes to ripen more fully, leading to higher phenolic content and a richer mouthfeel. Therefore, the level of phenolics in Riesling can reflect the climate and region where the grapes were grown, aiding tasters in identifying the wine's origin."),
        SPACE,
        html.Div("Acidity and Residual Sugar: Acidity and Residual Sugar: High acidity in Riesling can mask the perception of residual sugar. Acidity Perception: In Riesling, acidity is often perceived as a mouthwatering sensation that triggers the production of saliva. This crisp, refreshing quality enhances the wine's overall balance and can make it feel lively and invigorating on the palate. If the wine has obviously high acidity, think carefully about the residual sugar level you perceive"),
        SPACE,
        html.Div("Alcohol and Residual Sugar: In Riesling, wines with higher residual sugar levels often have lower alcohol content, as the fermentation process is stopped before converting all sugars to alcohol. Alcohol-to-Residual Sugar Ratio: Evaluating the ratio of alcohol to residual sugar in Riesling can provide clues about its region or style. For example, a high-alcohol, dry Riesling is more likely to be from a warm climate like Australia, while a low-alcohol, sweet Riesling may point to a cooler region like Germany."),
        SPACE, SPACE

    ], style = style.HOME)