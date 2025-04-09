# dest.py (更新版)

destinations = [
    {
        'name': 'Tokyo',
        'is_beginner_friendly': True,
        'expectations': ['Shopping', 'Cuisine'],
        'best_seasons': ['Spring', 'Winter'],
        'famous_foods': ['Sushi', 'Tempura'],
        'pace': ['Fast-paced - see as much as possible'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Kyoto',
        'is_beginner_friendly': True,
        'expectations': ['Cultural exploration', 'Nature'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': [],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Museum hopping']
    },
    {
        'name': 'Osaka',
        'is_beginner_friendly': True,
        'expectations': ['Shopping', 'Cuisine'],
        'best_seasons': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'famous_foods': [],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Fukuoka',
        'is_beginner_friendly': True,
        'expectations': ['Cuisine'],
        'best_seasons': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'famous_foods': ['Ramen'],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Hakone',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': [],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Relaxing hot springs']
    },
    {
        'name': 'Nikko',
        'is_beginner_friendly': False,
        'expectations': ['Nature', 'Cultural exploration'],
        'best_seasons': ['Autumn', 'Spring'],
        'famous_foods': [],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Sapporo',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Winter', 'Summer'],
        'famous_foods': [],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Kanazawa',
        'is_beginner_friendly': False,
        'expectations': ['Cultural exploration'],
        'best_seasons': ['Spring', 'Summer', 'Autumn', 'Winter'],
        'famous_foods': [],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Museum hopping']
    },
    {
        'name': 'Fuji',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Summer', 'Autumn'],
        'famous_foods': [],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Saga',
        'is_beginner_friendly': False,
        'expectations': ['Cultural exploration', 'Nature'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': ['Saga beef'],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Relaxing hot springs']
    },
    {
        'name': 'Akita',
        'is_beginner_friendly': False,
        'expectations': ['Nature', 'Cultural exploration'],
        'best_seasons': ['Winter', 'Autumn'],
        'famous_foods': ['Kiritampo'],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Nagoya',
        'is_beginner_friendly': True,
        'expectations': ['Cuisine', 'Cultural exploration'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': ['Miso katsu', 'Hitsumabushi'],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Museum hopping']
    },
    {
        'name': 'Kagoshima',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Spring', 'Winter'],
        'famous_foods': ['Kurobuta pork'],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Relaxing hot springs']
    },
    {
        'name': 'Okinawa',
        'is_beginner_friendly': True,
        'expectations': ['Nature'],
        'best_seasons': ['Spring', 'Summer'],
        'famous_foods': ['Goya champuru'],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Beach activities']
    },
    {
        'name': 'Hiroshima',
        'is_beginner_friendly': True,
        'expectations': ['Cultural exploration', 'Cuisine'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': ['Okonomiyaki'],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Museum hopping']
    },
    {
        'name': 'Kobe',
        'is_beginner_friendly': True,
        'expectations': ['Cuisine', 'Shopping'],
        'best_seasons': ['Spring', 'Winter'],
        'famous_foods': ['Kobe beef'],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Nightlife/entertainment']
    },
    {
        'name': 'Shizuoka',
        'is_beginner_friendly': False,
        'expectations': ['Nature'],
        'best_seasons': ['Spring', 'Summer'],
        'famous_foods': ['Green tea'],
        'pace': ['Slow travel - deep local immersion'],
        'activities': ['Hiking/outdoor adventures']
    },
    {
        'name': 'Nagasaki',
        'is_beginner_friendly': True,
        'expectations': ['Cultural exploration', 'Cuisine'],
        'best_seasons': ['Spring', 'Autumn'],
        'famous_foods': ['Champon'],
        'pace': ['Moderate - mix of activities and relaxation'],
        'activities': ['Museum hopping']
    },
]

questions = [
    {
        'question_en': 'Is this your first time/beginners to go to Japan?',
        'question_cn': '這是你第一次/新手去日本嗎？',
        'options_en': {'a': 'Yes', 'b': 'No'},
        'options_cn': {'a': '是', 'b': '否'}
    },
    {
        'question_en': 'What is your most expectation in your Japan trip?',
        'question_cn': '你最期待日本之旅的什麼？',
        'options_en': {
            'a': 'Shopping',
            'b': 'Cuisine',
            'c': 'Nature',
            'd': 'Cultural exploration'
        },
        'options_cn': {
            'a': '購物',
            'b': '美食',
            'c': '自然',
            'd': '文化探索'
        }
    },
    {
        'question_en': 'What is your favorite season?',
        'question_cn': '你喜歡哪個季節？',
        'options_en': {'a': 'Spring', 'b': 'Summer', 'c': 'Autumn', 'd': 'Winter'},
        'options_cn': {'a': '春天', 'b': '夏天', 'c': '秋天', 'd': '冬天'}
    },
    {
        'question_en': 'What is your favorite Japanese food?',
        'question_cn': '你喜歡哪種日本食物？',
        'options_en': {
            'a': 'Sushi',
            'b': 'Ramen',
            'c': 'Tempura',
            'd': 'Okonomiyaki',
            'e': 'Kobe beef',
            'f': 'None of the above/No preference'
        },
        'options_cn': {
            'a': '壽司',
            'b': '拉麵',
            'c': '天婦羅',
            'd': '大阪燒',
            'e': '神戶牛肉',
            'f': '以上皆非/無偏好'
        }
    },
    {
        'question_en': 'What is your preferred travel pace?',
        'question_cn': '你喜歡什麼旅行節奏？',
        'options_en': {
            'a': 'Fast-paced - see as much as possible',
            'b': 'Moderate - mix of activities and relaxation',
            'c': 'Slow travel - deep local immersion'
        },
        'options_cn': {
            'a': '快節奏 - 盡可能多看',
            'b': '中等 - 活動與放鬆兼顧',
            'c': '慢旅 - 深入體驗當地'
        }
    },
    {
        'question_en': 'What type of activities do you enjoy most?',
        'question_cn': '你最喜歡什麼類型的活動？',
        'options_en': {
            'a': 'Hiking/outdoor adventures',
            'b': 'Museum hopping',
            'c': 'Nightlife/entertainment',
            'd': 'Relaxing hot springs',
            'e': 'Beach activities'
        },
        'options_cn': {
            'a': '徒步/戶外冒險',
            'b': '博物館遊覽',
            'c': '夜生活/娛樂',
            'd': '放鬆溫泉',
            'e': '海灘活動'
        }
    },
    {
        'question_en': 'Do you prefer urban cities or rural areas?',
        'question_cn': '你更喜歡城市還是鄉村？',
        'options_en': {
            'a': 'Urban cities',
            'b': 'Rural areas',
            'c': 'A mix of both'
        },
        'options_cn': {
            'a': '城市',
            'b': '鄉村',
            'c': '兩者兼顧'
        }
    },
    {
        'question_en': 'Are you interested in historical sites?',
        'question_cn': '你對歷史遺址感興趣嗎？',
        'options_en': {
            'a': 'Yes, very interested',
            'b': 'Somewhat interested',
            'c': 'Not really'
        },
        'options_cn': {
            'a': '是的，非常感興趣',
            'b': '有些感興趣',
            'c': '不太感興趣'
        }
    },
    {
        'question_en': 'Do you enjoy trying unique local foods?',
        'question_cn': '你喜歡嘗試當地特色食物嗎？',
        'options_en': {
            'a': 'Yes, I love it',
            'b': 'Sometimes',
            'c': 'No, I prefer familiar flavors'
        },
        'options_cn': {
            'a': '是的，我很喜歡',
            'b': '有時會',
            'c': '不，我更喜歡熟悉的口味'
        }
    },
    {
        'question_en': 'How important is access to hot springs (onsen) for you?',
        'question_cn': '溫泉（onsen）對你來說有多重要？',
        'options_en': {
            'a': 'Very important',
            'b': 'Nice to have but not essential',
            'c': 'Not important'
        },
        'options_cn': {
            'a': '非常重要',
            'b': '有更好但不必要',
            'c': '不重要'
        }
    },
]
def translate_answers_to_english(answers):
    # Mapping of Chinese answers to English equivalents
    translation_map = {
        "是": "Yes",
        "否": "No",
        "購物": "Shopping",
        "美食": "Cuisine",
        "自然": "Nature",
        "文化探索": "Cultural exploration",
        "春天": "Spring",
        "夏天": "Summer",
        "秋天": "Autumn",
        "冬天": "Winter",
        "壽司": "Sushi",
        "拉麵": "Ramen",
        "天婦羅": "Tempura",
        "大阪燒": "Okonomiyaki",
        "神戶牛肉": "Kobe beef",
        "以上皆非/無偏好": "None of the above/No preference",
        "快節奏 - 盡可能多看": "Fast-paced - see as much as possible",
        "中等 - 活動與放鬆兼顧": "Moderate - mix of activities and relaxation",
        "慢旅 - 深入體驗當地": "Slow travel - deep local immersion",
        "徒步/戶外冒險": "Hiking/outdoor adventures",
        "博物館遊覽": "Museum hopping",
        "夜生活/娛樂": "Nightlife/entertainment",
        "放鬆溫泉": "Relaxing hot springs",
        "海灘活動": "Beach activities",
        "城市": "Urban cities",
        "鄉村": "Rural areas",
        "兩者兼顧": "A mix of both",
        "是的，非常感興趣": "Yes, very interested",
        "有些感興趣": "Somewhat interested",
        "不太感興趣": "Not really",
        "是的，我很喜歡": "Yes, I love it",
        "有時會": "Sometimes",
        "不，我更喜歡熟悉的口味": "No, I prefer familiar flavors",
        "非常重要": "Very important",
        "有更好但不必要": "Nice to have but not essential",
        "不重要": "Not important"
    }
    return [translation_map.get(answer, answer) for answer in answers]

content = './photo/'

introduction = [
    {
        'name': 'Tokyo',
        'intro_cn': '東京是日本的首都，融合了現代與傳統的魅力，是購物、美食和夜生活的天堂。',
        'intro_en': 'Tokyo, Japan’s capital, blends modern and traditional charm, making it a paradise for shopping, cuisine, and nightlife.',
        'attractions_cn': ['淺草寺', '東京塔', '澀谷十字路口'],
        'attractions_en': ['Senso-ji Temple', 'Tokyo Tower', 'Shibuya Crossing'],
        'recommended_days': 4,
        'image_url': 'tokyo.jpg',
        'transportation_en': 'From Narita Airport: Take the Narita Express (NEX) to Tokyo Station (about 1 hour, ¥3,020). Within the city: Use the Tokyo Metro (fares start at ¥170).',
        'transportation_cn': '從成田機場：乘坐成田特快（NEX）到東京站（約1小時，¥3,020）。市內交通：使用東京地鐵（票價從¥170起）。',
        'estimated_cost': '¥15,000-¥20,000'
    },
    {
        'name': 'Kyoto',
        'intro_cn': '京都以其悠久的歷史和傳統文化聞名，擁有眾多神社和庭園。',
        'intro_en': 'Kyoto is renowned for its rich history and traditional culture, featuring numerous shrines and gardens.',
        'attractions_cn': ['金閣寺', '清水寺', '伏見稻荷大社'],
        'attractions_en': ['Kinkaku-ji', 'Kiyomizu-dera', 'Fushimi Inari Taisha'],
        'recommended_days': 3,
        'image_url': 'kyoto.jpg',
        'transportation_en': 'From Kansai Airport: Take the Haruka Express to Kyoto Station (about 1 hour 20 minutes, ¥2,850). Within the city: Use city buses (¥230 per ride) or rent a bicycle.',
        'transportation_cn': '從關西機場：乘坐Haruka特快到京都站（約1小時20分鐘，¥2,850）。市內交通：使用市內巴士（每次¥230）或租賃自行車。',
        'estimated_cost': '¥12,000-¥18,000'
    },
    {
        'name': 'Osaka',
        'intro_cn': '大阪是日本的美食之都，同時也是購物和娛樂的熱門城市。',
        'intro_en': 'Osaka is Japan’s food capital and a popular destination for shopping and entertainment.',
        'attractions_cn': ['大阪城', '道頓堀', '環球影城日本'],
        'attractions_en': ['Osaka Castle', 'Dotonbori', 'Universal Studios Japan'],
        'recommended_days': 3,
        'image_url': 'osaka.jpg',
        'transportation_en': 'From Kansai Airport: Take the Nankai Airport Express to Namba Station (about 45 minutes, ¥920). Within the city: Use the Osaka Metro (fares start at ¥180).',
        'transportation_cn': '從關西機場：乘坐南海機場特快到難波站（約45分鐘，¥920）。市內交通：使用大阪地鐵（票價從¥180起）。',
        'estimated_cost': '¥10,000-¥15,000'
    },
    {
        'name': 'Fukuoka',
        'intro_cn': '福岡是九州的中心城市，以其拉麵和開放的港口文化著稱。',
        'intro_en': 'Fukuoka, the hub of Kyushu, is famous for its ramen and vibrant port culture.',
        'attractions_cn': ['大濠公園', '福岡塔', '運河城博多'],
        'attractions_en': ['Ohori Park', 'Fukuoka Tower', 'Canal City Hakata'],
        'recommended_days': 2,
        'image_url': 'fukuoka.jpg',
        'transportation_en': 'From Fukuoka Airport: Take the subway to Hakata Station (about 5 minutes, ¥260). Within the city: Use city buses (fares start at ¥200).',
        'transportation_cn': '從福岡機場：乘坐地鐵到博多站（約5分鐘，¥260）。市內交通：使用市內巴士（票價從¥200起）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
    {
        'name': 'Hakone',
        'intro_cn': '箱根以溫泉和富士山美景聞名，是放鬆身心的理想之地。',
        'intro_en': 'Hakone is famous for its hot springs and stunning views of Mount Fuji, perfect for relaxation.',
        'attractions_cn': ['大湧谷', '箱根神社', '蘆之湖'],
        'attractions_en': ['Owakudani', 'Hakone Shrine', 'Lake Ashi'],
        'recommended_days': 2,
        'image_url': 'hakone.jpg',
        'transportation_en': 'From Tokyo: Take the Shinkansen to Odawara Station (about 35 minutes, ¥3,220), then transfer to the Hakone Tozan Railway to Hakone-Yumoto (about 15 minutes, ¥310).',
        'transportation_cn': '從東京：乘坐新幹線到小田原站（約35分鐘，¥3,220），然後轉乘箱根登山鐵道到箱根湯本（約15分鐘，¥310）。',
        'estimated_cost': '¥10,000-¥15,000'
    },
    {
        'name': 'Nikko',
        'intro_cn': '日光以壯麗的自然風光和歷史悠久的寺廟群吸引遊客。',
        'intro_en': 'Nikko attracts visitors with its stunning natural scenery and historic temple complex.',
        'attractions_cn': ['東照宮', '華嚴瀑布', '中禪寺湖'],
        'attractions_en': ['Toshogu Shrine', 'Kegon Falls', 'Lake Chuzenji'],
        'recommended_days': 2,
        'image_url': 'nikko.jpg',
        'transportation_en': 'From Tokyo: Take the JR Tohoku Shinkansen to Utsunomiya (about 50 minutes, ¥2,820), then transfer to the JR Nikko Line to Nikko Station (about 45 minutes, ¥760).',
        'transportation_cn': '從東京：乘坐JR東北新幹線到宇都宮（約50分鐘，¥2,820），然後轉乘JR日光線到日光站（約45分鐘，¥760）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
    {
        'name': 'Sapporo',
        'intro_cn': '札幌是北海道的首府，以冬季雪節和自然景觀聞名。',
        'intro_en': 'Sapporo, the capital of Hokkaido, is renowned for its winter snow festival and natural landscapes.',
        'attractions_cn': ['大通公園', '札幌時鐘台', '北海道神宮'],
        'attractions_en': ['Odori Park', 'Sapporo Clock Tower', 'Hokkaido Shrine'],
        'recommended_days': 3,
        'image_url': 'sapporo.jpg',
        'transportation_en': 'From New Chitose Airport: Take the JR Rapid Airport train to Sapporo Station (about 40 minutes, ¥1,150). Within the city: Use the Sapporo Subway (fares start at ¥200).',
        'transportation_cn': '從新千歲機場：乘坐JR快速機場列車到札幌站（約40分鐘，¥1,150）。市內交通：使用札幌地鐵（票價從¥200起）。',
        'estimated_cost': '¥12,000-¥18,000'
    },
    {
        'name': 'Kanazawa',
        'intro_cn': '金澤以其保存完好的江戶時代建築和傳統工藝著稱。',
        'intro_en': 'Kanazawa is known for its well-preserved Edo-period architecture and traditional crafts.',
        'attractions_cn': ['兼六園', '金澤城', '東茶屋街'],
        'attractions_en': ['Kenrokuen Garden', 'Kanazawa Castle', 'Higashi Chaya District'],
        'recommended_days': 2,
        'image_url': 'kanazawa.jpg',
        'transportation_en': 'From Tokyo: Take the Hokuriku Shinkansen to Kanazawa Station (about 2 hours 30 minutes, ¥14,000). Within the city: Use the Kanazawa Loop Bus (¥200 per ride).',
        'transportation_cn': '從東京：乘坐北陸新幹線到金澤站（約2小時30分鐘，¥14,000）。市內交通：使用金澤循環巴士（每次¥200）。',
        'estimated_cost': '¥10,000-¥15,000'
    },
    {
        'name': 'Fuji',
        'intro_cn': '富士以富士山為中心，是登山和自然景觀的勝地。',
        'intro_en': 'Fuji centers around Mount Fuji, a prime spot for hiking and natural beauty.',
        'attractions_cn': ['富士山', '富士五合目', '忍野八海'],
        'attractions_en': ['Mount Fuji', 'Fuji Fifth Station', 'Oshino Hakkai'],
        'recommended_days': 2,
        'image_url': 'fuji.jpg',
        'transportation_en': 'From Tokyo: Take the JR Tokaido Shinkansen to Shin-Fuji Station (about 1 hour, ¥3,200), then take a local bus to the Fuji Five Lakes area (about 50 minutes, ¥1,500).',
        'transportation_cn': '從東京：乘坐JR東海道新幹線到新富士站（約1小時，¥3,200），然後乘坐當地巴士到富士五湖地區（約50分鐘，¥1,500）。',
        'estimated_cost': '¥10,000-¥15,000'
    },
    {
        'name': 'Saga',
        'intro_cn': '佐賀是一個安靜的城市，以陶瓷文化和溫泉聞名。',
        'intro_en': 'Saga is a quiet city famous for its ceramic culture and hot springs.',
        'attractions_cn': ['有田瓷器公園', '武雄溫泉', '吉野里遺址'],
        'attractions_en': ['Arita Porcelain Park', 'Takeo Onsen', 'Yoshinogari Historical Park'],
        'recommended_days': 2,
        'image_url': 'saga.jpg',
        'transportation_en': 'From Fukuoka: Take the JR Kamome Limited Express to Saga Station (about 40 minutes, ¥1,110). Within the city: Use local buses (fares start at ¥200).',
        'transportation_cn': '從福岡：乘坐JR鴎號特快到佐賀站（約40分鐘，¥1,110）。市內交通：使用當地巴士（票價從¥200起）。',
        'estimated_cost': '¥7,000-¥10,000'
    },
    {
        'name': 'Akita',
        'intro_cn': '秋田以其傳統的節日和自然美景吸引遊客。',
        'intro_en': 'Akita draws visitors with its traditional festivals and natural beauty.',
        'attractions_cn': ['角館武家屋敷', '田澤湖', '男鹿半島'],
        'attractions_en': ['Kakunodate Samurai District', 'Lake Tazawa', 'Oga Peninsula'],
        'recommended_days': 2,
        'image_url': 'akita.jpg',
        'transportation_en': 'From Tokyo: Take the Akita Shinkansen to Akita Station (about 4 hours, ¥17,000). Within the city: Use local buses (fares start at ¥200).',
        'transportation_cn': '從東京：乘坐秋田新幹線到秋田站（約4小時，¥17,000）。市內交通：使用當地巴士（票價從¥200起）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
    {
        'name': 'Nagoya',
        'intro_cn': '名古屋是日本中部的工業城市，擁有豐富的歷史和美食。',
        'intro_en': 'Nagoya, an industrial city in central Japan, boasts rich history and cuisine.',
        'attractions_cn': ['名古屋城', '熱田神宮', '大須商店街'],
        'attractions_en': ['Nagoya Castle', 'Atsuta Shrine', 'Osu Shopping Street'],
        'recommended_days': 3,
        'image_url': 'nagoya.jpg',
        'transportation_en': 'From Tokyo: Take the Tokaido Shinkansen to Nagoya Station (about 1 hour 40 minutes, ¥10,360). Within the city: Use the Nagoya Subway (fares start at ¥200).',
        'transportation_cn': '從東京：乘坐東海道新幹線到名古屋站（約1小時40分鐘，¥10,360）。市內交通：使用名古屋地鐵（票價從¥200起）。',
        'estimated_cost': '¥10,000-¥15,000'
    },
    {
        'name': 'Kagoshima',
        'intro_cn': '鹿兒島以活火山櫻島和溫泉聞名，是九州南部的寶石。',
        'intro_en': 'Kagoshima, known for the active Sakurajima volcano and hot springs, is a gem in southern Kyushu.',
        'attractions_cn': ['櫻島', '仙巖園', '城山公園'],
        'attractions_en': ['Sakurajima', 'Sengan-en Garden', 'Shiroyama Park'],
        'recommended_days': 2,
        'image_url': 'kagoshima.jpg',
        'transportation_en': 'From Fukuoka: Take the Kyushu Shinkansen to Kagoshima-Chuo Station (about 1 hour 20 minutes, ¥10,000). Within the city: Use the Kagoshima City Tram (fares start at ¥170).',
        'transportation_cn': '從福岡：乘坐九州新幹線到鹿兒島中央站（約1小時20分鐘，¥10,000）。市內交通：使用鹿兒島市電（票價從¥170起）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
    {
        'name': 'Okinawa',
        'intro_cn': '沖繩以其亞熱帶氣候和美麗海灘聞名，是度假的理想選擇。',
        'intro_en': 'Okinawa is famous for its subtropical climate and beautiful beaches, an ideal vacation spot.',
        'attractions_cn': ['首里城', '古宇利島', '沖繩美麗海水族館'],
        'attractions_en': ['Shurijo Castle', 'Kouri Island', 'Okinawa Churaumi Aquarium'],
        'recommended_days': 4,
        'image_url': 'okinawa.jpg',
        'transportation_en': 'From Naha Airport: Use the Yui Rail to central Naha (about 15 minutes, ¥260). For other islands: Rent a car (around ¥5,000 per day) or use local ferries.',
        'transportation_cn': '從那霸機場：使用Yui Rail到那霸市中心（約15分鐘，¥260）。其他島嶼：租車（每天約¥5,000）或使用當地渡輪。',
        'estimated_cost': '¥12,000-¥18,000'
    },
    {
        'name': 'Hiroshima',
        'intro_cn': '廣島以和平紀念和歷史遺址聞名，同時擁有美味的當地美食。',
        'intro_en': 'Hiroshima is known for its peace memorials and historic sites, along with delicious local cuisine.',
        'attractions_cn': ['和平紀念公園', '廣島城', '宮島'],
        'attractions_en': ['Peace Memorial Park', 'Hiroshima Castle', 'Miyajima'],
        'recommended_days': 3,
        'image_url': 'hiroshima.jpg',
        'transportation_en': 'From Hiroshima Airport: Take the airport limousine bus to Hiroshima Station (about 45 minutes, ¥1,340). Within the city: Use the Hiroshima Electric Railway (fares start at ¥190).',
        'transportation_cn': '從廣島機場：乘坐機場豪華巴士到廣島站（約45分鐘，¥1,340）。市內交通：使用廣島電鐵（票價從¥190起）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
    {
        'name': 'Kobe',
        'intro_cn': '神戶是一個港口城市，以神戶牛肉和美麗的夜景著稱。',
        'intro_en': 'Kobe, a port city, is famous for Kobe beef and stunning night views.',
        'attractions_cn': ['神戶港塔', '六甲山', '南京町'],
        'attractions_en': ['Kobe Port Tower', 'Mount Rokko', 'Nankinmachi (Chinatown)'],
        'recommended_days': 2,
        'image_url': 'kobe.jpg',
        'transportation_en': 'From Kansai Airport: Take the Airport Limousine Bus to Sannomiya Station (about 1 hour 10 minutes, ¥2,000). Within the city: Use the Kobe City Loop Bus (¥260 per ride).',
        'transportation_cn': '從關西機場：乘坐機場豪華巴士到三宮站（約1小時10分鐘，¥2,000）。市內交通：使用神戶市循環巴士（每次¥260）。',
        'estimated_cost': '¥10,000-¥15,000'
    },
    {
        'name': 'Shizuoka',
        'intro_cn': '靜岡以富士山和綠茶種植聞名，是自然愛好者的天堂。',
        'intro_en': 'Shizuoka, known for Mount Fuji and green tea plantations, is a paradise for nature lovers.',
        'attractions_cn': ['三保松原', '靜岡城', '日本平'],
        'attractions_en': ['Miho no Matsubara', 'Shizuoka Castle', 'Nihondaira'],
        'recommended_days': 2,
        'image_url': 'shizuoka.jpg',
        'transportation_en': 'From Tokyo: Take the Tokaido Shinkansen to Shizuoka Station (about 1 hour, ¥5,940). Within the city: Use local buses (fares start at ¥200).',
        'transportation_cn': '從東京：乘坐東海道新幹線到靜岡站（約1小時，¥5,940）。市內交通：使用當地巴士（票價從¥200起）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
    {
        'name': 'Nagasaki',
        'intro_cn': '長崎以其多元文化和歷史遺跡聞名，是日本西部的獨特城市。',
        'intro_en': 'Nagasaki is renowned for its multicultural heritage and historical sites, a unique city in western Japan.',
        'attractions_cn': ['和平公園', '哥拉巴園', '大浦天主堂'],
        'attractions_en': ['Peace Park', 'Glover Garden', 'Oura Catholic Church'],
        'recommended_days': 2,
        'image_url': 'nagasaki.jpg',
        'transportation_en': 'From Fukuoka: Take the JR Kamome Limited Express to Nagasaki Station (about 2 hours, ¥4,500). Within the city: Use the Nagasaki Electric Tramway (fares start at ¥130).',
        'transportation_cn': '從福岡：乘坐JR鴎號特快到長崎站（約2小時，¥4,500）。市內交通：使用長崎電車（票價從¥130起）。',
        'estimated_cost': '¥8,000-¥12,000'
    },
]