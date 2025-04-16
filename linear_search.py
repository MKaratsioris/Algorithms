from decorators import timeit
from definitions import Iterables, Simple


@timeit
def linear_search(iterable: Iterables, target: Simple) -> tuple[Simple, int] | None:
    """
    By using the linear search method, it returns the index position
    of the target if found, else returns None.
    """
    steps: int = 0
    for index in range(len(iterable)):
        steps += 1
        if iterable[index] == target:
            return index, steps
    return None, steps

if __name__ == '__main__':
    #10^(1) => 0.00000 sec
    test_list = [x for x in range(11)]
    test_target = 10
    index, steps = linear_search(test_list, test_target)
    print(f"{len(test_list)=}\t{index=}\t{steps=}")
    
    #10^(2) => 0.00000 sec
    test_list = [x for x in range(101)]
    test_target = 100
    index, steps = linear_search(test_list, test_target)
    print(f"{len(test_list)=}\t{index=}\t{steps=}")
    
    #10^(3) => 0.00000 sec
    test_list = [x for x in range(1_001)]
    test_target = 1_000
    index, steps = linear_search(test_list, test_target)
    print(f"{len(test_list)=}\t{index=}\t{steps=}")
    
    #10^(4) => 0.00000 sec
    test_list = [x for x in range(10_001)]
    test_target = 10_000
    index, steps = linear_search(test_list, test_target)
    print(f"{len(test_list)=}\t{index=}\t{steps=}")
    
    #10^(5) => 0.00300 sec (varies...)
    test_list = [x for x in range(100_001)]
    test_target = 100_000
    index, steps = linear_search(test_list, test_target)
    print(f"{len(test_list)=}\t{index=}\t{steps=}")
    
    #10^(6) => 0.03000 sec (varies...)
    test_list = [x for x in range(1_000_001)]
    test_target = 1_000_000
    index, steps = linear_search(test_list, test_target)
    print(f"{len(test_list)=}\t{index=}\t{steps=}")
    