import math

import pylab


def taylor_polynomial(n: int, xs: pylab.ndarray) -> pylab.ndarray:
    """Evaluates the nth taylor polynomial of sin(x) + cos(x) at every point x
    in xs."""
    ys = pylab.zeros_like(xs)
    for k in range(n + 1):
        ys += (-1)**math.floor(k / 2) * xs**k / math.factorial(k)
    return ys


def main():
    pylab.figure(figsize=(10, 6))

    xs = pylab.linspace(0, 3 * pylab.pi, 1000, endpoint=True)
    # print(xs)
    # print(taylor_polynomial(1, xs))

    pylab.plot(xs, pylab.sin(xs) + pylab.cos(xs), label=r'$\sin x + \cos x$')
    for i in range(1, 21, 2):
        pylab.plot(xs, taylor_polynomial(i, xs), label=f'$P_{{{i}}}$')

    pylab.grid()
    pylab.legend()
    pylab.xlabel('$x$')
    pylab.ylabel('$y$')
    pylab.ylim(-2, 2)

    pylab.title('Y1110076 - Taylor polynomials with different order for '
                r'$\sin x + \cos x$')
    # pylab.savefig('HW1.png')
    pylab.show()


if __name__ == '__main__':
    main()
