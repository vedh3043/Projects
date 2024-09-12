


CALORIE_GOAL_LIMIT = 3000
PROTEIN_GOAL = 180
CARBS_GOAL = 200
FATS_GOAL = 60


from dataclasses import dataclass

@dataclass
class Food: 
    name: str
    calories: int
    protein: int
    carbs: int
    fats: int


done = False
today = []


while not done:
    print("""
    (1) Add a new food
    (2) Visualize Progress
    (3) Quit
    """)
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Add name: ")
        calories = int(input("Add calories(kcal): ")) 
        protein = int(input("Add protein(g): ")) 
        carbs = int(input("Add carbs(g): ")) 
        fats = int(input("Add fats(g): ")) 
        food = Food(name, calories, protein, carbs, fats)
        today.append(food)
        print("Successfully added!")

    elif choice == "2":
       
        calories_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        carbs_sum = sum(food.carbs for food in today)
        fats_sum = sum(food.fats for food in today)
        
        
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        axs[0, 0].pie([protein_sum, carbs_sum, fats_sum], labels=["Protein", "Carbs", "Fats"], autopct='%1.1f%%')
        axs[0, 0].set_title("Macronutrients Distribution")

        
        axs[0, 1].bar([0 ,1, 2], [protein_sum, carbs_sum, fats_sum], width=0.4, label='Consumed')
        axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, CARBS_GOAL, FATS_GOAL], width=0.4, label='Goal')
        axs[0, 1].set_title("Macronutrients Progress")  
        axs[0, 1].set_xticks([0.25, 1.25, 2.25])
        axs[0, 1].set_xticklabels(["Protein", "Carbs", "Fats"])
        axs[0, 1].legend()

        
        axs[1, 0].plot([0, 1], [0, calories_sum], label="Calories Consumed", marker="o")
        axs[1, 0].axhline(y=CALORIE_GOAL_LIMIT, color="r", linestyle="--", label="Calorie Goal")
        axs[1, 0].set_title("Calorie Progress")
        axs[1, 0].legend()

        
        protein_calories = protein_sum * 4
        carbs_calories = carbs_sum * 4
        fats_calories = fats_sum * 9
        axs[1, 1].bar([0], [protein_calories], label='Protein (4 kcal/g)', color='blue')
        axs[1, 1].bar([0], [carbs_calories], bottom=[protein_calories], label='Carbs (4 kcal/g)', color='green')
        axs[1, 1].bar([0], [fats_calories], bottom=[protein_calories + carbs_calories], label='Fats (9 kcal/g)', color='orange')
        axs[1, 1].set_title("Caloric Breakdown by Macronutrients")
        axs[1, 1].legend()

        fig.tight_layout()
        plt.show()
