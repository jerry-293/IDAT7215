def get_user_input(questions):
    answers = []
    for idx, q in enumerate(questions):
        print(f"\nQuestion {idx+1}: {q['question']}")
        for option, text in q['options'].items():
            print(f"  {option}. {text}")
        while True:
            choice = input("Your choice (a/b/c/d): ").lower()
            if choice in q['options']:
                answers.append(q['options'][choice])
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    return answers

def recommend_city(answers, destinations):
    max_score = -1
    best_destinations = []
    
    is_beginner = answers[0] == 'Yes'
    expectation = answers[1]
    season = answers[2]
    food = answers[3] if answers[3] != 'None of the above/ No preference' else None
    
    for dest in destinations:
        score = 0
        
        # Check beginner compatibility
        if is_beginner == dest['is_beginner_friendly']:
            score += 1
        
        # Check expectation match
        if expectation in dest['expectations']:
            score += 1
        
        # Check season match
        if season in dest['best_seasons']:
            score += 1
        
        # Check food preference
        if food and food in dest['famous_foods']:
            score += 1
        
        # Update best destinations
        if score > max_score:
            max_score = score
            best_destinations = [dest]
        elif score == max_score:
            best_destinations.append(dest)
    
    return [dest['name'] for dest in best_destinations] if best_destinations else []