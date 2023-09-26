# from database import Database
# db = Database()

questionnaire = {
    '1': {
        'type': 'choice',
        'question':
        'Clarity',
        'options': {'Clear':[], 'Cloudy':[]},
        'color': 'blue',
        'additional': False,
        'warning' : False
    },
    '2': {
        'type': 'choice',
        'question':
        'Brightness',
        'options': {'Dull':[], 'Bright':[], 'Brilliant':[]},
        'color': 'yellow',
        'additional': False,
        'warning' : False
    },
    '3': {
        'type': 'choice',
        'question':
        'Intensity',
        'options': {'Pale':[], 'Medium':[], 'Deep':[], 'Translucent':[], 'Opaque': []},
        'color': 'orange',
        'additional': False,
        'warning' : False
    },
    '4': {
        'type': 'multi-choice',
        'question':
        'Evidence of gas or sediment?',
        'options': {'Gas - is it bubbly?':[], 'Sediment':[]},
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    '5': {
        'type':
        'choice',
        'question':
        'Colour',
        'options': {
            'White':['Straw/lemon', 'Yellow', 'Gold', 'Amber'], 
            'Rose':['Pink', 'Pink orange', 'Orange'], 
            'Red':['Purple', 'Ruby', 'Garnet', 'Tawny', 'Brown']
        },
        'color': 'blue',
        'additional': False,
        'warning' : False
    },
    '6': {
        'type':
        'choice',
        'question':
        'Hue',
        'options': 
            {'Silver':[], 'Green':[], 'Orange':[], 'Blue':[], 'Brown':[]}
        ,
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    '7': {
        'type':
        'choice',
        'question':
        'Rim',
        'options': 
            {'Obvious':[], 'Not obvious':[]}
        ,
        'color': 'pink',
        'additional': False,
        'warning' : False
    },
    '8': {
        'type':
        'choice',
        'question':
        'Stain/Extract',
        'options': 
            {'None':[], 'light':[], 'Medium':[], 'Heavy':[]}
        ,
        'color': 'red',
        'additional': False,
        'warning' : False
    },
    '9': {
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
    '10': {
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
    '11': {
        'type':
        'multi-choice',
        'question':
        'Faults',
        'options':
            {'TCA':[], 'H2S':[], 'Volatile Acidity':[], 'Brett':[], 'Oxidation':[], 'Other':[]},
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    '12': {
        'type':
        'slider',
        'question':
        'Sweetness',
        'options': {
            'dry':["dry <4g/L: little to no perceptible residual sugar. As sweet as plain bread, raw celery or radish"],
            'off-dry':["off dry 18-50 g/L: off dry sweetness"],
            'medium':["medium sweet 15-75mg/L: noticeably sweet but not excessively so. As sweet as table grapes or teriyaki sauce"],
            'sweet':["sweet 75-120mg/L: Obviously sweet, As sweet as very ripe strawberries or jam"],
            'very sweet':["very sweet >120mg/L: intensely sweet. Comparable sweetness to dried dates, honey, baklava"]
        },
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    '13': {
        'type':
        'slider',
        'question':
        'Tannin',
        'options': {
            'Low':["Low: Soft, smooth, no noticable astringency. Milk chocolate or banana"],
            'Soft':["Soft mouthfeel, no assertive tannins (moderate), lightly brewed or milk tea, watermelon or fresh red capsicum "],
            'Structure':["Tanins provide structure and a slight grip on the palate without being overwhelming. Pear or dark chocolate"],
            'Firm':["Firm structure and a noticeable astringency. Walnuts or black coffee"],
            'Very dry':["Very dry, very firm and grippy texture. Strongly brewed black tea or a black teabag on the tongue"],
        },
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    '13.5': {
        'type':
        'multi-choice',
        'question':
        'Tannin',
        'options': {
            'Ripe':[],
            'Smooth':[],
            'Unripe':[],
            'Green':[],
            'Course':[],
            'Stalky':[],
            'Chalky':[],
            'Fine grained':[]
        },
        'color': 'grape',
        'additional': False,
        'warning' : False
    },
    '14': {
        'type':
        'slider',
        'question':
        'Acidity',
        'options': {
            'Low':["LOW: soft, round, less crisp. Cooked, unflavoured white rice"],
            'Medium Low':["MED LOW: moderate (lacks freshness) fresh cucumber"],
            'Medium':["MED: balanced level of tartness, ripe tomato"],
            'Medium+':["MED +: fresh and crisp, freshly squeezed lemon juice or fresh tart green apple"],
            'High':["HIGH: refreshing, vibrant, sharp, zesty, grapefruit or white vinegar"]
        },
        'color': 'blue',
        'additional': False,
        'warning' : False
    },
    '15': {
        'type':
        'slider',
        'question':
        'Alcohol',
        'options': {
            'Low':["Low <11%ABV. Fresh easy drinking, light body, delicate crisp character"],
            'Restrained':["Restrained: 11-12.5% ABV: moderate to light alcohol pleasant roundness and structure"],
            'Medium':["Medium: 12.5-13.5 % ABV: good balance between fruitiness and body. They often exhibit depth and complexity"],
            'Medium+':["Medium + 13.5-14.5% ABV: fuller-bodied, warming sensation, showcase ripe, rich fruit flavors"],
            'High':["High >14.5% ABV: robust and powerful, noticeable warmth, concentrated flavors and complexity"]
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    '16': {
        'type':
        'multi-choice',
        'question':
        'Primary',
        'options': {
            'Floral': ['white flowers','Purple flowers','linden','lime blossom','roses','orange blossom','jasmine','fruit tree','honeysuckle'],
            'Green/tree fruit': ['apple', 'pear', 'quince'],
            'Earth': ['mineral (slate)', 'mineral (chalk)', 'mineral (Flint/stone)', 'wet stones', 'white mushroom'],
            'Grape': ['muscat', 'grape'],
            'Botrytis': ['ginger', 'honey','saffron'],
            'Citrus': ['grapefruit', 'lemon', 'lime', 'orange', 'lime candy' ,'citronella','grapefruit', 'orange', 'peel', 'lime zest'],
            'Stone fruit': ['peach', 'apricot', 'nectarine', 'white plum','white peach','white nectarine'],
            'Tropical fruit': ['banana', 'banana peel', 'guava', 'passion fruit', 'pineapple'],
            'Berry': ['blackcurrant'],
            'Other': ['sulphides', 'dry Lentils', 'smoke', 'candlewax', 'slight spice', 'margarita salt', 'fresh tennis ball', 'panna cotta', 'meringue', 'Celery', 'White Pepper']
        },
        'color': 'dark',
        'additional': False,
        'warning' : True
    },
    '17': {
        'type':
        'multi-choice',
        'question':
        'Secondary',
        'options': {
            'Spice': ['Cardamon', 'anise', 'Pepper', 'Fennel'], 
            'Bottle age aromas': ['Honey', 'petrol / kerosene', 'paraffin', 'marzipan', 'browned toast', 'nutty', 'oak'], 
        },
        'color': 'dark',
        'additional': False,
        'warning' : True
    },
    '18': {
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
    '19': {
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
    '20': {
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
    '21': {
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
    '22': {
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
    '23': {
        'type':
        'slider',
        'question':
        'Flavour Intensity',
        'options': {
            'Light': [],
            'Medium -':[],
            'Medium':[],
            'Medium +': [],
            'Pronounced ':[],
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    '24': {
        'type':
        'slider',
        'question':
        'Body',
        'options': {
            'Light': [],
            'Medium -':[],
            'Medium':[],
            'Medium +': [],
            'Full':[],
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
    '25': {
        'type':
        'slider',
        'question':
        'From a scale of 1 to 10 (with 10 being the best), how much do you enjoy the wine?',
        'options': {
            '1': [],
            '2':[],
            '3':[],
            '4': [],
            '5':[],
            '6':[],
            '7': [],
            '8':[],
            '9':[],
            '10':[],
        },
        'color': 'dark',
        'additional': False,
        'warning' : False
    },
}