from sympy import *


def main():
    x, y = symbols('x y')
    func = x * y**2 * log(x**2)

    print('Integrate x first and then y')
    for i in range(3):
        integral = Integral(func, x, y)
        pprint(integral)
        pprint('=')
        integral_done = integral.doit()
        pprint(integral_done)
        func = integral_done

    print()
    print('Integrate y first and then x')
    func = x * y**2 * log(x**2)
    for i in range(3):
        integral = Integral(func, y, x)
        pprint(integral)
        pprint('=')
        integral_done = integral.doit()
        pprint(integral_done)
        func = integral_done


if __name__ == '__main__':
    main()
