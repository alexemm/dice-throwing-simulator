from typing import List, Callable, KeysView
from random import choice
from collections import Counter
from operator import itemgetter


def get_strategy(key: str) -> Callable:
    return strategies.get(key, random_method)


def get_strategy_ideas() -> KeysView[str]:
    return strategies.keys()


def average_method(previous_results: List[int]) -> int:
    return 3


def average_method_unlucky(previous_results: List[int]) -> int:
    return 4


def average_method_lucky(previous_results: List[int]) -> int:
    return 7


def average_method_3_or_4(previous_results: List[int]) -> int:
    return choice([3, 4])


def random_method(previous_results: List[int]) -> int:
    return choice(range(1, 7))


def average_method_3_or_4_based_on_previous(previous_results: List[int]) -> int:
    return previous_method(list(filter(lambda x: x == 3 or x == 4, previous_results)), list(range(3, 5)))


def previous_method(previous_results: List[int], range_of_choices: List[int] = range(1, 6)) -> int:
    return min(Counter(previous_results).items(), key=itemgetter(1))[0] if len(range_of_choices) == len(
        Counter(previous_results)) else choice(range_of_choices)


def previous_based_on_last_results(previous_results: List[int], last: int = 10) -> int:
    return previous_method(
        previous_results[-1: -(last + 1) if (last + 1) < len(previous_results) else len(previous_results)])


# TODO: maybe objectoriented?
strategies = {
    'avg': average_method,
    'avg4': average_method_unlucky,
    'avg34': average_method_3_or_4,
    'random': random_method,
    'prev34': average_method_3_or_4_based_on_previous,
    'prev': previous_method,
    'prev_last': previous_based_on_last_results
}


def test():
    guesses = [3, 3, 4, 3, 4, 4, 3, 3]
    counter = Counter(guesses)
    print(counter)
    print(len(range(3, 5)))
    print(guesses[-1: 0])
    print(type(get_strategy('random')))


if __name__ == '__main__':
    test()
