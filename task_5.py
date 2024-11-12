favorite_food = ['manty', 'kazy', 'eggs', 'doner', 'samsa']

def ask_favorite_food(favorite_food):
    food = input('What is your favorite food ? ')
    
    if food in favorite_food:
        print(f'{food} is too mine favorite food !')
    else:
        print(f'{food} is not my favorite food !') 

ask_favorite_food(favorite_food)
