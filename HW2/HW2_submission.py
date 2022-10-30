import pylab

PI = pylab.pi


def h(t: pylab.ndarray) -> pylab.ndarray:
    return 1.2732 * pylab.sin(2 * t) +\
           0.4244 * pylab.sin(6 * t) +\
           0.25465 * pylab.sin(10 * t) +\
           0.18189 * pylab.sin(14 * t) +\
           0.14147 * pylab.sin(18 * t)


def h_prime(x: pylab.ndarray, d: float):
    return (h(x + d) - h(x)) / d


def main():
    a, b, n = -PI, PI, 50000
    d = (b - a) / (n - 1)
    xs = pylab.linspace(a, b, n, endpoint=True)

    pylab.plot(xs, h(xs), label=r'$h(t)$', color='b')
    pylab.plot(xs, h_prime(xs, d), label=r"$h'(t)$", color='g')

    pylab.grid()
    pylab.legend()
    pylab.xlabel('$t$')
    pylab.ylabel('$s$')
    pylab.axis((-3.5, 3.5, -15, 15))

    pylab.title('Y1110076 - Python HW 2\n'
                'Sawtooth function approximation and derivative')
    pylab.savefig('HW2.png')
    pylab.show()


if __name__ == '__main__':
    main()
