destinations = [
    {
        'name': 'Tokyo',
        'is_beginner_friendly': True,
        'expectations': ['Shopping', 'Cuisine'],
        'best_seasons': ['Spring', 'Winter'],
        'famous_foods': ['Sushi', 'Tempura'],
        'pace': ['Fast-paced'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Kyoto',
        'is_beginner_friendly': True,
        'expectations': ['Cultural exploration', 'Nature'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': [],
        'pace': ['Moderate'],
        'activities': ['Museum hopping']
    },
    {
        'name': 'Osaka',
        'is_beginner_friendly': True,
        'expectations': ['Shopping', 'Cuisine'],
        'best_seasons': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'famous_foods': [],
        'pace': ['Moderate'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Fukuoka',
        'is_beginner_friendly': True,
        'expectations': ['Cuisine'],
        'best_seasons': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'famous_foods': ['Ramen'],
        'pace': ['Moderate'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Hakone',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': [],
        'pace': ['Slow travel'],
        'activities': ['Relaxing hot springs']
    },
    {
        'name': 'Nikko',
        'is_beginner_friendly': False,
        'expectations': ['Nature', 'Cultural exploration'],
        'best_seasons': ['Autumn', 'Spring'],
        'famous_foods': [],
        'pace': ['Moderate'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Hokkaido',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Winter', 'Summer'],
        'famous_foods': [],
        'pace': ['Slow travel'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Kanazawa',
        'is_beginner_friendly': False,
        'expectations': ['Cultural exploration'],
        'best_seasons': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'famous_foods': [],
        'pace': ['Moderate'],
        'activities': ['Museum hopping']
    },
]

questions = [
    {
        'question': 'Is this your first time/ beginners to go to Japan?',
        'options': {
            'a': 'Yes',
            'b': 'No'
        }
    },
    {
        'question': 'What is your most expectation in your Japan trip?',
        'options': {
            'a': 'Shopping',
            'b': 'Cuisine',
            'c': 'Nature',
            'd': 'Cultural exploration'
        }
    },
    {
        'question': 'What is your favorite season?',
        'options': {
            'a': 'Spring',
            'b': 'Summer',
            'c': 'Autumn',
            'd': 'Winter'
        }
    },
    {
        'question': 'What is your favorite Japanese food?',
        'options': {
            'a': 'Sushi',
            'b': 'Ramen',
            'c': 'Tempura',
            'd': 'None of the above/ No preference'
        }
    },
    {
        'question': 'What is your preferred travel pace?',
        'options': {
            'a': 'Fast-paced - see as much as possible',
            'b': 'Moderate - mix of activities and relaxation',
            'c': 'Slow travel - deep local immersion'
        }
    },
    {
        'question': 'What type of activities do you enjoy most?',
        'options': {
            'a': 'Hiking/outdoor adventures',
            'b': 'Museum hopping',
            'c': 'Nightlife/entertainment',
            'd': 'Relaxing hot springs'
        }
    },
]