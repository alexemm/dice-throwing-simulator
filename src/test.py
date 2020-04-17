from dice_throwing import throw_n_dices, get_success_rate, guess_n_times
from strategies import get_strategy_ideas
from file_tools import save_json

from os import listdir


def test():
    n: int = int(100000)
    result = throw_n_dices(n)
    odds = dict(
        {strategy: get_success_rate(guess_n_times(n, result, strategy), result) for strategy in get_strategy_ideas()})
    path = "results/"
    file = "%s%i.json" % (path, len(listdir(path)))
    save_json(file, {"n": n, "strategy": odds})


if __name__ == '__main__':
    test()