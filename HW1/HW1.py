import pylab

PI = pylab.pi


def f(x):
    return pylab.maximum(pylab.absolute(x * pylab.sin(x)),
                         pylab.absolute(x * pylab.cos(x)))


def g(x):
    return pylab.minimum(pylab.absolute(x * pylab.sin(x)),
                         pylab.absolute(x * pylab.cos(x)))


def main():
    xs = pylab.linspace(-2 * PI, 2 * PI, 50000, endpoint=True)
    # print(xs)
    # print(f(xs))

    pylab.plot(xs,
               f(xs),
               label=r'$y=f(x)=\max (|x \sin x|, |x \cos x |)$',
               color='purple')
    pylab.plot(xs,
               g(xs),
               label=r'$y=g(x)=\min (|x \sin x|, |x \cos x |)$',
               color='g')

    pylab.grid()
    pylab.legend()
    pylab.xlabel('$x$')
    pylab.ylabel('$y$')
    pylab.axis((-8, 8, 0, 7))

    pylab.title('Y1110076 - Python HW 1')
    pylab.savefig('HW1.png')
    pylab.show()


if __name__ == '__main__':
    main()
