# recommend.py
def get_user_input(questions):
    answers = []
    for q in questions:
        print(q['question_en'])  # CMD 用英文
        for key, value in q['options_en'].items():
            print(f"{key}. {value}")
        while True:
            answer = input("Your choice (e.g., a, b, c): ").lower()
            if answer in q['options_en']:
                answers.append(q['options_en'][answer])
                break
            print("Invalid input, please try again.")
    return answers

def recommend_city(answers, destinations):
    max_score = -1
    best_destinations = []
    reasons_dict = {}
    is_beginner = answers[0] == 'Yes'
    expectation = answers[1]
    season = answers[2]
    food = answers[3] if answers[3] != 'None of the above/No preference' else None
    pace = answers[4]
    activity = answers[5]
    area_preference = answers[6]
    historical_interest = answers[7]
    local_food_interest = answers[8]
    hot_springs_importance = answers[9]
    
    for dest in destinations:
        score = 0
        reasons = []
        # 初學者友好
        if is_beginner == dest['is_beginner_friendly']:
            score += 1
            reasons.append("Suitable for beginners" if is_beginner else "Not beginner-focused")
        # 期待匹配
        if expectation in dest['expectations']:
            score += 1
            reasons.append(f"Matches your expectation: {expectation}")
        # 季節匹配
        if season in dest['best_seasons']:
            score += 1
            reasons.append(f"Great in {season}")
        # 食物偏好
        if food and food in dest['famous_foods']:
            score += 1
            reasons.append(f"Known for {food}")
        # 旅行節奏
        if pace in dest['pace']:
            score += 1
            reasons.append(f"Fits your pace: {pace}")
        # 活動偏好
        if activity in dest['activities']:
            score += 1
            reasons.append(f"Offers {activity}")
        # 城市/鄉村偏好
        if area_preference == 'Urban cities' and dest['is_beginner_friendly']:
            score += 1
            reasons.append("Urban city, great for city lovers")
        elif area_preference == 'Rural areas' and not dest['is_beginner_friendly']:
            score += 1
            reasons.append("Rural area, perfect for nature lovers")
        elif area_preference == 'A mix of both':
            score += 0.5
            reasons.append("Offers a mix of urban and rural experiences")
        # 歷史遺址興趣
        if historical_interest == 'Yes, very interested' and 'Cultural exploration' in dest['expectations']:
            score += 1
            reasons.append("Rich in historical sites")
        elif historical_interest == 'Somewhat interested' and 'Cultural exploration' in dest['expectations']:
            score += 0.5
            reasons.append("Has some historical sites")
        # 當地特色食物興趣
        if local_food_interest == 'Yes, I love it' and dest['famous_foods']:
            score += 1
            reasons.append("Offers unique local foods")
        elif local_food_interest == 'Sometimes' and dest['famous_foods']:
            score += 0.5
            reasons.append("Has some unique local foods")
        # 溫泉重要性
        if hot_springs_importance == 'Very important' and 'Relaxing hot springs' in dest['activities']:
            score += 1
            reasons.append("Has access to hot springs")
        elif hot_springs_importance == 'Nice to have but not essential' and 'Relaxing hot springs' in dest['activities']:
            score += 0.5
            reasons.append("Offers hot springs as an option")
        
        if score > max_score:
            max_score = score
            best_destinations = [dest['name']]
            reasons_dict = {dest['name']: reasons}
        elif score == max_score:
            best_destinations.append(dest['name'])
            reasons_dict[dest['name']] = reasons
    
    return [(name, reasons_dict[name]) for name in best_destinations] if best_destinations else []

if __name__ == "__main__":
    from dest import questions, destinations
    answers = get_user_input(questions)
    recommendation = recommend_city(answers, destinations)
    if recommendation:
        print("Based on your preferences, we recommend:")
        for city, reasons in recommendation:
            print(f"{city}:")
            for reason in reasons:
                print(f"  - {reason}")
    else:
        print("No specific recommendation based on your preferences.")