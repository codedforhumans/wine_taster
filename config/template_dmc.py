import dash_mantine_components as dmc

style = {
    "label": {
        "&[data-active]": {
            "&, &:hover": { # 
                # "backgroundColor": dmc.theme.DEFAULT_COLORS["red"][5],
                # "color": "white",
                "borderColor": dmc.theme.DEFAULT_COLORS["red"][5]
            },
        },
    },
    # "label": {
    #     "backgroundColor": dmc.theme.DEFAULT_COLORS["red"][5]
    # }
    
}