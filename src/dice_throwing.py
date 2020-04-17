from typing import List
from random import randrange

from strategies import get_strategy, get_strategy_ideas
from file_tools import save_json


def throw_n_dices(n: int) -> List[int]:
    return [randrange(1, 7) for _ in range(0, n)]


def guess_n_times(n: int, result: List[int], strategy: str) -> List[int]:
    return [get_strategy(strategy)(result[0: i]) for i in range(n)]


def get_success_rate(guesses: List[int], result: List[int]) -> float:
    return sum(filter(lambda x: x, [a == result[idx] for idx, a in enumerate(guesses)])) / float(len(guesses))


def test():
    n: int = int(10e6)
    result = throw_n_dices(n)
    odds = dict(
        {strategy: get_success_rate(guess_n_times(n, result, strategy), result) for strategy in get_strategy_ideas()})
    file = "results/2.json"
    save_json(file, {"n": n, "strategy": odds})


if __name__ == '__main__':
    test()
