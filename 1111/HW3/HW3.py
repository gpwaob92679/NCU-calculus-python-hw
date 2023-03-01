import pylab

PI = pylab.pi


def f(t):
    return 7**pylab.cos(t) * pylab.sin(t)


def F(t):
    return -7**pylab.cos(t) / pylab.log(7)


def main():
    a, b, n = 0, PI / 2, 101
    xs, h = pylab.linspace(a, b, n, endpoint=True, retstep=True)
    ys = f(xs)
    # print(xs, ys, h, sep='\n')

    # 數學積分
    precise_sum = F(b) - F(a)

    # 迴圈求積
    rectangle_sum_loop = 0
    upper_sum = 0
    lower_sum = 0
    trapezoid_sum_loop = 0
    for i in range(0, n - 1):
        rectangle_sum_loop += ys[i]
        upper_sum += max(ys[i], ys[i + 1])
        lower_sum += min(ys[i], ys[i + 1])
        trapezoid_sum_loop += ys[i] + ys[i + 1]
    rectangle_sum_loop *= h
    upper_sum *= h
    lower_sum *= h
    trapezoid_sum_loop *= h / 2

    # 公式求積
    # ys[-1] = x_{n}
    rectangle_sum_formula = sum(ys[:-1]) * h
    trapezoid_sum_formula = (ys[0] + 2 * sum(ys[1:-1]) + ys[-1]) * h / 2
    simpsons_formula = (ys[0] + 4 * sum(ys[1:-1:2]) + 2 * sum(ys[2:-2:2]) +
                        ys[-1]) * h / 3

    def error(x: float) -> str:
        return f'誤差: {round(abs(x - precise_sum), 10)}'

    print(f'數學積分    : {round(precise_sum, 9)}')
    print()

    print('迴圈求積:')
    print(f'矩形積分    : {round(rectangle_sum_loop, 9)}  '
          f'{error(rectangle_sum_formula)}')
    print(f'上矩形積分  : {round(upper_sum, 9)}  {error(upper_sum)}')
    print(f'下矩形積分  : {round(lower_sum, 9)}  {error(lower_sum)}')
    print(f'梯形積分法  : {round(trapezoid_sum_loop, 9)}  '
          f'{error(trapezoid_sum_loop)}')
    print()

    print('公式求積:')
    print(f'矩形積分法  : {round(rectangle_sum_formula, 9)}  '
          f'{error(rectangle_sum_formula)}')
    print(f'梯形積分法  : {round(trapezoid_sum_formula, 9)}  '
          f'{error(trapezoid_sum_formula)}')
    print(f'Simpson積分: {round(simpsons_formula, 9)}  '
          f'{error(simpsons_formula)}')


if __name__ == '__main__':
    main()
