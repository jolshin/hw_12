def main():
    """Main function opens file .txt and calls function to parse lines and generate an entry for the cook_book"""
    main.cook_book = {}             #as I got it's not a GLOBAL variable, which is prohibited by the task
    main.dish_name = None           #this one not too
    main.ingredients_quantity = 0   #and this
    main.list = []                  #...not
    
    with open("recipes.txt") as document:
        for line in document:
            parser_and_dict_maker(line.strip('\n'))
            #print(line.strip('\n'))

    parser_and_dict_maker('') #because of the fact that RECIPES.TXT ends with not empty line, after context manager it sends an empty string to trigger last ELIF which adds last dish entry in the cook_book
    
    print('COOK_BOOK:')
    for dish in main.cook_book:
        print(dish, main.cook_book[dish])
        print('')

    terminal()

def parser_and_dict_maker(line):
    """Function for parsing and generating entry for the COOK_BOOK"""

    if line.isdigit():
        main.ingredients_quantity = int(line)

    elif line.find('|') != -1:
        main.list.append({'ingredient_name' : line.split(' | ')[0], 'quantity' : line.split(' | ')[1], 'measure' : line.split(' | ')[2] })

    elif line != '':
        main.dish_name = line
        
    elif main.ingredients_quantity == len(main.list):
        main.cook_book.update({main.dish_name : main.list})
        main.dish_name = None
        main.ingredients_quantity = 0
        main.list = []

def get_shop_list_by_dishes(dishes, person_count):
    """Function generates SHOP_LIST according to input data"""
    shop_list = {}
    for dish in dishes:
        if dish in main.cook_book.keys():
            for ingredient in main.cook_book[dish]:
                if ingredient['ingredient_name'] in shop_list.keys():
                    shop_list.update({ingredient['ingredient_name'] : {ingredient['measure'] : shop_list[ingredient['ingredient_name']][ingredient['measure']] + int(ingredient['quantity']) * person_count}}) 
                else:
                    shop_list.update({ingredient['ingredient_name'] : {ingredient['measure'] : int(ingredient['quantity']) * person_count}}) 
        else:
            print(f'Блюдо \"{dish}\" отсутвует в кулинарной книге, попробуйте ввести повторно')
            terminal()
            

    for dish in shop_list:
        print(dish, shop_list[dish])

def terminal():
    """Function gets input data"""
    while True:
        get_shop_list_by_dishes(input('Введите список блюд через запятую (соблюдайте регистр, после запятой ставьте пробел): ').split(', '), int(input('Введите количество персон: ')))
    
    
main()