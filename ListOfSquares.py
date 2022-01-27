# Создать и распечатать список значениями которого будут квадраты чисел от 1 до 30 включительно.
def list_of_squares():
    l = list()
    for i in range(1,31):
        l.append(i*i)
    print (l)
list_of_squares()