import pylab

PI = pylab.pi


def g(t: pylab.ndarray) -> pylab.ndarray:

    def g_func(x: float):
        return 1 if x // PI <= x / PI <= x // PI + 0.5 else -1

    return pylab.array([g_func(x) for x in t])


def g_prime(t: pylab.ndarray, d: float):

    def check_inf(x: float):
        return pylab.inf if abs(x) > 1e4 else x

    derivative = (g(t + d) - g(t)) / d
    return pylab.array([check_inf(x) for x in derivative])


def h(t: pylab.ndarray) -> pylab.ndarray:
    return 1.2732 * pylab.sin(2 * t) + \
           0.4244 * pylab.sin(6 * t) + \
           0.25465 * pylab.sin(10 * t) + \
           0.18189 * pylab.sin(14 * t) + \
           0.14147 * pylab.sin(18 * t)


def h_prime(x: pylab.ndarray, d: float):
    return (h(x + d) - h(x)) / d


def main():
    a, b, n = -PI, PI, 50000
    d = (b - a) / (n - 1)

    xs = pylab.linspace(a, b, n, endpoint=True)
    # print(xs)
    # print(g(xs))

    pylab.plot(xs, g(xs), label=r'$g(t)$ sawtooth function', color='r')
    pylab.plot(xs, h(xs), label=r'$h(t)$ approximation', color='b')
    pylab.plot(xs, g_prime(xs, d), label=r"$g'(t)$", color='y')
    pylab.plot(xs, h_prime(xs, d), label=r"$h'(t)$", color='g')

    pylab.grid()
    pylab.legend()
    pylab.xlabel('$t$')
    pylab.ylabel('$s$')
    pylab.axis((-3.5, 3.5, -15, 15))

    pylab.title(
        'Y1110076 - Python HW 2\n'
        'Sawtooth function, trigonometric approximation and derivatives')
    pylab.savefig('HW2.png')
    pylab.show()


if __name__ == '__main__':
    main()
