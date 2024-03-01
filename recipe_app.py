ingredients = []
new_ingredient = input("")

print(f"Hello! Welcome to your recipe app!")
print(f"Write anything to add ingredients to the list. To exit the app simply write 'quit'.")

while new_ingredient != "quit":
    new_ingredient = input("Add a new ingredient: ")

    if new_ingredient != "" and new_ingredient != "quit":
        ingredients.append(new_ingredient)
        print(ingredients)

print()
print(f"The elements of the recipe: {ingredients}")