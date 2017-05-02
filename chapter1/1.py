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

    for i in range(1, 6):
        fp = sp.polyfit(x, y, i)
        f = sp.poly1d(fp)
        print(f'{i} error', error(f, x, y))

        fx = sp.linspace(0, x[-1], 1000)
        plt.plot(fx, f(fx), linewidth=2)
        plt.legend([f"d={f.order}"], loc='upper left')

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
