my_list = []

def my_func(a,b,c):
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)

my_func(input("Введіть перший елемент списку"),input("Введіть другий елемент списку"),input("Введіть третій елемент списку"))

print(my_list)