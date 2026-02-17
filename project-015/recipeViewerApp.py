def load_recipes(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('Ingredients: ','').strip()
                    instructions = lines[2].replace("Instructions: ",'').strip()
                    recipe_dict[name] = {"ingredients":ingredients,'instructions':instructions}
            return recipe_dict
    except FileNotFoundError:
        print("file not found")
        return {}

def showMenu():
    print("\n-Recipe Viewer Menu-")
    print("1. View recipe by name")
    print("2. List all recipe")   
    print("3. Exit") 

def viewRecipes(recipes):
    name = input("enter the name of recipe: ").strip()
    if name in recipes:
        print(f"\n- Recipe {name} Details-")
        print(f"Ingredients: {recipes[name]['ingredients']}")    
        print(f"Ingredients: {recipes[name]['instructions']}")
    else:
        print("Recipe not found")  

recipes_file = 'project-015/recipes.txt'
recipes = load_recipes(recipes_file)

while True:
    showMenu()
    choice = input("enter your choice: ")
    if choice == '1':
        viewRecipes(recipes)
    elif choice == '2':
        for name in recipes:
            print(name)
    elif choice == '3':
        break
    else:
        print("please input the right choice")  
            