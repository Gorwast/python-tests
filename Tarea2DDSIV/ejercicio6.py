# Lopez Chaidez Luis Enrique DDSIV
def list_ascendant(input_list):
    """Function that orders a list on ascendant order using insertion sort

    Args:
        input_list (list): List with the values that we want to order

    Returns:
        list: The ordered list
    """
    for i in range(1, len(input_list)):
        j = i-1
        next_element = input_list[i]
        # Compare the current element with next one
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j = j-1
        input_list[j+1] = next_element
    return input_list


def list_descendant(input_list):
    """Function that orders a list on descendant order using insertion sort

    Args:
        input_list ([type]): List with the values that we want to order

    Returns:
        list: The ordered list
    """
    for i in range(1, len(input_list)):
        j = i-1
        next_element = input_list[i]
        # Compare the current element with next one
        while (input_list[j] < next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j = j-1
        input_list[j+1] = next_element
    return input_list


def create_list(number_values):
    """Funtion that creates a list, prompting the user to input the values of the list

    Args:
        number_values (int): Number of values that the list will contain

    Returns:
        list: List with the values introduced by the user
    """
    list = []
    for index in range(1, number_values + 1):
        list.append(input('Introduzca el valor no.' + str(index) + ': '))
    return list


loop = True
list = create_list(5)
while loop:
    print('¿Que desea hacer? \n1. Ordenar de forma ascendente\n2. Ordenar de forma descendente\n3.Salir')
    option = input()
    if option == '1':
        print(list_ascendant(list))
    elif option == '2':
        print(list_descendant(list))
    elif option == '3':
        loop = False
