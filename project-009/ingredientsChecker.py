#learn about tuples and set
recipe = {"flour", 'sugar', 'butter','milk','eggs'}

#alternative ingredients function
def alternativeIngredients():
    edit_ingredients = input("what ingredients you want to changes: ")
    if edit_ingredients in recipe:
        recipe.remove(edit_ingredients)
    else:
        print("please input the right ingredients")
    add_ingredients = input("what ingredients you want to add: ")
    recipe.add(add_ingredients)
    print(f"{add_ingredients} has been added to the recipe")
    
while True:
    print(f"\nThe ingredients: ",recipe)
    #choice for changing an ingredients
    choice = input("\nif you want to changes the ingridients into alternative ingredients type (yes) if not just press(enter): ").lower()
    
    if choice == "yes":
        alternativeIngredients()
    else:
        user_input = input("enter your ingridients you have (separated by commas): ")
        user_ingredients = set(user_input.split(', '))

        missing_ingredients = recipe - user_ingredients
        extra_ingredients = user_ingredients - recipe

        print("\n-Ingredient Checker-")
        if missing_ingredients:
            print(f"you are missing following ingredients:{','.join(missing_ingredients)}")
        else:
            print("you have all the ingredients needed")

        if extra_ingredients:
            print(f"you have extra ingredients:{','.join(extra_ingredients)}")
        else:
            print(f"you don't have extra ingredients")
        break

with open("project-009/ingredientList.txt", "w", encoding="utf-8") as f:
    for item in recipe:
        f.write(item + "\n")
