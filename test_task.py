import pytest


def get_sum(number_list):
    sum = 0
    wrong_index = []

    def list_add(i):
        nonlocal sum
        if isinstance(i, (int, float)):
            sum += i
        elif isinstance(i, list):
            for k in i:  # k - элемент внутри вложенного листа
                list_add(k)
                if isinstance(k, str):
                    wrong_index.append(i.index(k))
        else:
            wrong_index.append(j)

    for j, i in enumerate(number_list):  # i - элемент в списке, j - индекс элемента в списке
        if isinstance(i, (int, float, list)):
            list_add(i)
        else:
            wrong_index.append(j)

    if wrong_index:
        return wrong_index
    else:
        return sum


@pytest.mark.parametrize("input_list, result", [
    ([1, 2, 3, 4, 5], 15),
    ([1, 2, 3, 4, 5.1], 15.1),
    ([1, 2, 3, 4, 5.0], 15.0),
    ([1, 2, 3, [4, 5.0]], 15.0),
    ([1, 2, "three", 4, 5.0], [2]),
    ([1, 2, ["three", 4, 5.0]], [2, 0]),
    ([True, 2, ("three", [{}, 5.0])], [[0], [2, 0], [2, 1, 0]])
])
def test_sum(input_list, result):
    assert get_sum(input_list) == result, "Неверное равенство"
