import matplotlib.pyplot as plt
import scipy as sp


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


def main():
    data = sp.genfromtxt('data/web_traffic.tsv', delimiter='\t')
    x = data[:,0]
    y = data[:,1]

    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

    inflection = int(3.5 * 7 * 24)
    xb = x[inflection:]
    yb = y[inflection:]

    frac = 0.3
    split_idx = int(frac * len(xb))

    shuffled = sp.random.permutation(list(range(len(xb))))
    test = sorted(shuffled[:split_idx])
    train = sorted(shuffled[split_idx:])

    fbt1 = sp.poly1d(sp.polyfit(xb[train], yb[train], 1))
    fbt2 = sp.poly1d(sp.polyfit(xb[train], yb[train], 2))
    fbt3 = sp.poly1d(sp.polyfit(xb[train], yb[train], 3))
    fbt10 = sp.poly1d(sp.polyfit(xb[train], yb[train], 10))
    fbt100 = sp.poly1d(sp.polyfit(xb[train], yb[train], 100))

    for f in [fbt1, fbt2, fbt3, fbt10, fbt100]:
        print(f'Error d={f.order}: {error(f, xb[test], yb[test])}')


if __name__ == '__main__':
    main()