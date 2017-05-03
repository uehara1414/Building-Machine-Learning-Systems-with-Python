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

    for i in [1, 2, 3, 10, 100]:
        fp = sp.polyfit(x, y, i)
        f = sp.poly1d(fp)
        print(f'{i} error', error(f, x, y))

        fx = sp.linspace(0, x[-1], 1000)
        plt.plot(fx, f(fx), linewidth=2)
        plt.legend([f"d={f.order}"], loc='upper left')

    inflection = int(3.5 * 7 * 24)
    xa = x[:inflection]
    ya = y[:inflection]
    xb = x[inflection:]
    yb = y[inflection:]
    fa = sp.poly1d(sp.polyfit(xa, ya, 1))
    fb = sp.poly1d(sp.polyfit(xb, yb, 1))

    fa_error = error(fa, xa, ya)
    fb_error = error(fb, xb, yb)
    print(f'Error inflection={fa_error+fb_error}')
    plt.plot(xa, fa(xa), linewidth=2)
    plt.plot(xb, fb(xb), linewidth=2)

    plt.scatter(x, y)
    plt.title('Web traffic over the world')
    plt.xlabel('Time')
    plt.ylabel('Hits/hour')
    plt.xticks([w*7*24 for w in range(10)],
               [f'week {w}' for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
