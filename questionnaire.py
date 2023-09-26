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
        'options': {'Pale':[], 'Medium':[], 'Deep':[]},
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
            'White':['straw/lemon', 'yellow', 'gold', 'amber'], 
            'Rose':['pink', 'pink orange', 'orange'], 
            'Red':['purple', 'ruby', 'garnet', 'tawny']
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
            {'Silver':[], 'green':[], 'orange':[], 'blue':[], 'brown':[]}
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
            {'Obvious':[], 'not obvious':[]}
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
            {'none':[], 'light':[], 'Medium':[], 'heavy':[]}
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
            {'TCA':[], 'H2S':[], 'Volatile':[], 'Acidity':[], 'Brett':[], 'Oxidation':[], 'Other':[]},
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
    '13': {
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
    '14': {
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
    '15': {
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
    '16': {
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
    '17': {
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