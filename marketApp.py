from functions import show_selected_items, get_total_bull_detailed,\
    make_line, add_item, remove_item, show_data_base, make_double_line

name = input ('please enter your name: ')


make_double_line('x',100)
print("""Welcome to Store application you can buy, remove, add items and at the end you
can show total bill in this """)
make_double_line('x',100)


selected_items = []
while True:
    
    request = input('''if you want to add items enter "add" 
if you want to remove items enter "remove" 
if you want to show total bill enter "total" 
if you want to exit enter "exit":
Enter here:''').lower()
    if request == 'add':
        make_line('-',100)
        show_data_base()
        show_selected_items(selected_items)
        item = input('please enter the item you want to add: ').lower()
        selected_items = add_item(selected_items, item)
        make_line('-',100)
        
        
    elif request == 'remove':
        make_line('#',100)
        show_selected_items(selected_items)
        item = input('please enter the item you want to remove: ').lower()
        remove_item(selected_items, item)
        make_line('#',100)

    elif request == 'total':
        make_double_line('=',100)
        total = get_total_bull_detailed(selected_items)
        print(f'your total bill is {total}')
        make_line()
        print('thank you for using the store application')
        make_line()
        make_double_line('=',100)   
        selected_items = []
        
    elif request == 'exit':
        print('thank you for using the store application')
        break
    else:
        print('invalid request')
    make_line()
    