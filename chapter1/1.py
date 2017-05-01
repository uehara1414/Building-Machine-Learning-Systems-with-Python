import matplotlib.pyplot as plt
import scipy as sp

def main():

    data = sp.genfromtxt('data/web_traffic.tsv', delimiter='\t')
    x = data[:,0]
    y = data[:,1]

    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

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
