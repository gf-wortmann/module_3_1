# Домашняя работа по уроку "Пространство имён"


# global calls-
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(g):
    count_calls()
    return len(g), g.upper(), g.lower()


def is_contained(string, list_to_search):
    count_calls()
    the_list = []
    for s in list_to_search:
        the_list.insert(len(the_list), s.upper())
    # print(list_to_search)
    return string.upper() in the_list


print(string_info('flap'))
print(string_info('anaconda'))
# print(is_contained('string', ['string', 'list', 'word']))
print(is_contained('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contained('cycle', ['recycling', 'cyclic']))
print(calls)
