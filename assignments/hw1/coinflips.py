import sys
import numpy as np

def coinflips(x):
    counter = x
    heads = 0.0
    tails = 0.0

    while counter > 0:
        flip = np.random.random_sample()
        if flip > 0.5:
            heads += 1
        else:
            tails += 1
        counter -= 1

    print(tails / (heads + tails))


if __name__ == "__main__":
    x = int(sys.argv[1])
    coinflips(x)