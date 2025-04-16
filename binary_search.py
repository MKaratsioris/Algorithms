from decorators import timeit
from definitions import Iterables, Simple

@timeit
def binary_search(iterable: Iterables, target: Simple) -> tuple[Simple, int] | None:
    """
    Binary search Algorithm.

    Parameters
    ----------
    iterable : Iterables
        Collection of data
    target : Simple
        Data to be found in the iterable

    Returns
    -------
    Simple | None
        The index of the target in the iterable.
    """
    beg_index = 0
    last_index = len(iterable) - 1
    steps: int = 0
    while beg_index <= last_index:
        steps += 1
        median = (beg_index + last_index) // 2
        if iterable[median] == target:
            return median, steps
        elif iterable[median] < target:
            beg_index = median + 1
        else:
            last_index = median - 1
    return None, steps


if __name__ == '__main__':
    # 10^(1) => 0 sec
    test_list: list[int] = [x for x in range(11)]
    print(f"{test_list}")
    test_target: int = 10
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) * 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")

    # 10^(2) => 0 sec
    test_list: list[int] = [x for x in range(101)]
    print(f"{test_list}")
    test_target: int = 100
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    
    # 10^(3) => 0 sec
    test_list: list[int] = [x for x in range(1_001)]
    test_target: int = 1_000
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")

    # 10^(4) => 0 sec
    test_list: list[int] = [x for x in range(10_001)]
    test_target: int = 10_000
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
""" 

    # 10^(5) => 0 sec
    test_list: list[int] = [x for x in range(100_001)]
    test_target: int = 100_003
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")

    # 10^(6) => 0 sec
    test_list: list[int] = [x for x in range(1_000_001)]
    test_target: int = 1_000_000
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = 0
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
    test_target: int = len(test_list) // 2
    index, steps = binary_search(test_list, test_target)
    print(f"Target '{test_target}' {'is in the list.' if index or index == 0 else 'is not in the list.'}\nIterations: {steps}.")
 """