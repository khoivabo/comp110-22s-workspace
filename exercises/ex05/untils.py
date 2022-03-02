
__author__ = "730277137"


def only_evens (x: list[int]) -> list[int]:
    """Give even numbers from a list"""
    for number in x: 
        i: int = 0
        empty_list: list[int] = list()
        while i < len(x):
            if x[i] % 2 == 0:
                empty_list.append(x[i])
                i += 1 
            else: 
                i += 1
    return


def sub (y: list[int], start_index: int, end_index: int) -> list[int]:
    """Create a subet of a list"""
    for number in y:
        empty_list: list[int] = list()
        i = start_index
        if start_index < 0: 
            i = 0
            if end_index > len(y):
                while i < len(y):
                    empty_list.append(y[i])
                    i += 1
            else:
                while i < end_index:
                    empty_list.append(y[i])
                    i += 1
        else: 
            if end_index > len(y):
                while i < len(y):
                    empty_list.append(y[i])
                    i += 1
            else:
                while i < end_index:
                    empty_list.append(y[i])
                    i += 1
    print(empty_list)
    return


def concat (x:list[int], y: list[int]) -> list[int]:
    """Combining two different list into one"""
    empty_list: list[int] = list()
    i = 0
    while i < len(x):
        empty_list.append(x[i])
        i += 1
    i = 0 
    while i < len(y):
        empty_list.append(y[i])
        i += 1
    print(empty_list)
    return