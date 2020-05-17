"""2. Закодируйте любую строку по алгоритму Хаффмана."""
from collections import Counter, deque

class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(entered_string):
    #Построение дерева для кодирования по алгоритму Хаффмана
    count_string = Counter(entered_string)
    sorted_string = deque(sorted(count_string.items(), key=lambda item: item[1]))
    while len(sorted_string) > 1:
        weight = sorted_string[0][1] + sorted_string[1][1]
        node = MyNode(left=sorted_string.popleft()[0], right=sorted_string.popleft()[0])
        # Вставка пары "узел, вес" на нужное место в список
        for i, item in enumerate(sorted_string):
            if weight > item[1]:
                continue
            else:
                sorted_string.insert(i, (node, weight))
                break
        else:
            sorted_string.append((node, weight))

    return sorted_string[0][0]


encode_dict = dict()


def huffman_code(tree, path=''):
    #Составление таблицы кодирования по дереву

    if not isinstance(tree, MyNode):
        encode_dict[tree] = path

    else:
        huffman_code(tree.left, path=f'{path}0')
        huffman_code(tree.right, path=f'{path}1')


entered_string = input('Введите строку для кодировки: ')
huffman_code(huffman_tree(entered_string))

encoded_list = []

for element in entered_string:
    encoded_list.append(encode_dict[element])


encoded_string = ' '.join(encoded_list)
print(f'Закодированная строка: {encoded_string}')
