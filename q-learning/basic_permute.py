from typing import NamedTuple, Any


class Permute:

    def __init__(self, **kwargs):
        self.args = tuple(kwargs.keys())
        self.options = kwargs
        self.counter = [0 for _ in range(len(self.args))]

    def __iter__(self):
        return self

    def __next__(self):
        output_value = {
            option_name: self.options[option_name][count]
            for option_name, count in zip(self.args, self.counter)
        }

        self.counter[0] += 1

        for i, count in enumerate(self.counter):
            if count >= len(self.options[self.args[i]]):
                if i == len(self.counter) - 1:
                    raise StopIteration

                self.counter[i] = 0
                self.counter[i + 1] += 1
                continue

            break

        return output_value


per = Permute(caol=[0, 1, 2], ian=[5, 6, 7])
for v in per:
    print(v)
