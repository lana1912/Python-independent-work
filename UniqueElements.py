# Напишите функцию Python, которая берет список и возвращает новый список с уникальными элементами первого списка.
def unique_elements(list):
    list2 = []
    for e in list:
        if e not in list2:
            list2.append(e)
    return list2
print(unique_elements([1, 2, 2, 3, 3, 36]))   



