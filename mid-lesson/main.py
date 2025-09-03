#example solution for managing a list of favorite foods
def write_foods(foods):
    with open('foods.txt', 'w') as file:
        for food in foods:
            file.write(food + '\n')
def read_foods():
   foods_list =[]
   with open('foods.txt', 'r') as file:
       for line in file:
           foods_list.append(line.strip())
   return foods_list
def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == '2':
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == '3':
            idx = int(input("Which food to remove? "))
            foods.pop(idx - 1)
            write_foods(foods)
        elif action == '4':
            break

main()

