import dest as d
import recommend as r

def main():
 print("Welcome to the Japan Travel Expert System!")
 print("Please answer the following questions to get a personalized recommendation.\n")
 user_answers = r.get_user_input(d.questions)
 recommendation = r.recommend_city(user_answers, d.destinations)
 if not recommendation:
        print("\nNo specific recommendation based on your preferences.")
 elif len(recommendation) == 1:
        print(f"\nBased on your preferences, we recommend: {recommendation[0]}")
 else:
        print("\nBased on your preferences, we recommend these destinations:")
        for idx, city in enumerate(recommendation, 1):
            print(f"  {idx}. {city}")

if __name__ == "__main__":
 main()