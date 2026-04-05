def readFoods(fileName):
    foods=dict()
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                line=line.strip()
                if not line:
                    continue
                parts=line.split(";")
                ingredient=parts[0]
                try:
                    costPerKG=float(parts[1])
                    caloriePerKG=float(parts[2])
                except ValueError:
                    continue
                if ingredient not in foods:
                    foods[ingredient]=(costPerKG,caloriePerKG)
                
    except OSError:
        exit("error opening the file!")
    return foods

def readRecipes(fileName):
    recipes=dict()
    try:
        with open(fileName,"r") as inf:
            inf.readline()
            for line in inf:
                line=line.strip()
                if not line or "Method" in line:
                    break
                parts=line.split(";")
                ingredient=parts[0]
                try:
                    grams=float(parts[1].strip())
                except ValueError:
                    continue
                recipes[ingredient]=grams
    except OSError:
        exit("error opening the file!")
    return recipes

def main():
    foods=readFoods("foods.txt")
    recipe_polenta=readRecipes("polenta.txt")
    recipe_fusilli=readRecipes("fusilli.txt")
    
    total_cost=0
    total_calorie=0

    print("Ingredients: ")
    for ingredient, gram in recipe_polenta.items():
        print(ingredient,"-",gram)

        if ingredient in foods:
            costPerKG, calPerKG= foods[ingredient]
            total_cost += (gram/1000)*costPerKG
            total_calorie += (gram/1000)*calPerKG

    print(f"\nNumber of ingredients: {len(recipe_polenta)}")
    print(f"Recipe cost: {total_cost:.2f}")
    print(f"Recipe calories: {total_calorie:.2f}")
        
    

if __name__=="__main__":
    main()