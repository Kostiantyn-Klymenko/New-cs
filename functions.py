

database = ['shampoo', 'soap', 'toothpaste', 'toothbrush', 'lotion', 'cream', 'gel', 'vegetable']
price_list = [100, 50, 30, 20, 150, 200, 250, 500]

def show_data_base():
    print('the available items in the store are:')
    for item, price in zip(database, price_list):
        print(f'{item}: {price}')

def show_selected_items(selected_items):
    if len(selected_items) == 0:
        print('you have not selected any items')
    else:
        print('you have selected the following items:')
        for item in selected_items:
            print(f'{item} : {price_list[database.index(item)]}')

def get_total_bull_detailed(selected_items):
    total = 0
    for item in selected_items:
        if item in database:
            price=price_list[database.index(item)]
            print(f'{item}: {price}')
            total += price
        else:
            print(f'{item} is not available in the store')
    return total

def make_line(length=50, char='*'):
    print( char * length )

def make_double_line(length=50, char='*'):
    print( char * length + '\n' + char * length )

def add_item(selected_items, item):

    if item in database:
        selected_items.append(item)
        print(f'{item} has been added to your cart')
    else:
        print(f'{item} is not available in the store')
    return selected_items

def remove_item(selected_items, item):
    if item in selected_items:
        selected_items.remove(item)
        print(f'{item} has been removed from your cart')
    else:
        print(f'{item} is not available in your cart')
    return selected_items