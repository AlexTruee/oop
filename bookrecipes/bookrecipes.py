import os

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='UTF-8') as file:
    cook_book = {}
    dish_dict = []
    for string in file:
        dish = string.strip()
        ingredient_count = int(file.readline().strip())
        for item in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    cooking_list = {}
    for dish_ in dishes:
        for ingredient in cook_book[dish_]:

            ingredient_dict = dict([(ingredient['ingredient_name'],
                                     {'measure': ingredient['measure'],
                                      'quantity': int(ingredient['quantity']) * person_count
                                      })])

            if cooking_list.get(ingredient['ingredient_name']) == 'None':
                aded_ = (int(cooking_list[ingredient['ingredient_name']]['quantity']) +
                         int(ingredient_dict[ingredient['ingredient_name']]['quantity']))
                cooking_list[ingredient['ingredient_name']]['quantity'] = aded_
            else:
                cooking_list.update(ingredient_dict)
    sorted_cooking_list = sorted(cooking_list.items())
    return sorted_cooking_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
