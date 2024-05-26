my_dict = {'Aslan':'19 августа', 'Hasbulla' : '15 мая', 'Inna' :'12 октября'}
print(my_dict)
print(my_dict['Aslan'])
print(my_dict)
my_dict['Sasha'] = '3 июня'
print(my_dict)
my_dict.update({'Masha': '10 июля', 'Ben': '4 декабря'})
print(my_dict)
del my_dict['Aslan']
print(my_dict)

my_sets = {1, 2, 1, 4, 3, 2}
print(my_sets)
my_sets.update(['NewOne', 'NewTwo'])
print(my_sets)
my_sets.discard('NewOne')
print(my_sets)
my_sets.remove('NewTwo')
my_sets.add(9)
print(my_sets)

