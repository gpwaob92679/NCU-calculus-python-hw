import pylab


def main():
    thetas = pylab.linspace(0, 10 * pylab.pi, 1000)
    rs = pylab.sin(2.3 * thetas)**2 + pylab.cos(2.3 * thetas)**4
    pylab.polar(thetas, rs)

    pylab.title(
        r'Y1110076 - Graph of $\sin^2(2.3\theta)+\cos^4(2.3\theta)$ '
        r'for $\theta\in[0, 10\pi]$',
        pad=16)
    pylab.tight_layout()
    # pylab.savefig('HW2.png')
    pylab.show()


if __name__ == '__main__':
    main()
