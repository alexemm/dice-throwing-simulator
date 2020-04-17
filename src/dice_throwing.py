from typing import List
from random import randrange

from strategies import get_strategy, get_strategy_ideas


def throw_n_dices(n: int) -> List[int]:
    return [randrange(1, 7) for _ in range(0, n)]


def guess_n_times(n: int, result: List[int], strategy: str) -> List[int]:
    print(strategy)
    return [get_strategy(strategy)(result[0: i]) for i in range(n)]


def get_success_rate(guesses: List[int], result: List[int]) -> float:
    return sum(filter(lambda x: x, [a == result[idx] for idx, a in enumerate(guesses)])) / float(len(guesses))
