def list_of_stores_with_ingredients(dishes, person_count):
total = {}
for dish in dishes:
if dish in cook_book:
for exist in cook_book[dish]:
total[exist[‘ingredient_name’]] = {‘measure’: cook_book[‘measure’],‘quantity’: (cook_book[‘quantity’] * person_count)}
else:
print(f’Блюда “{dish}” нет в книге рецептов’)
return total
list_of_stores_with_ingredients([“Омлет”], 2)