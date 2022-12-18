from multiprocessing import Pool
import argparse

def prime_factorization(x):
    init_number = x
    ans = []
    d = 2
    while d * d <= x:
        if x % d == 0:
            ans.append(d)
            x //= d
        else:
            d += 1
    if x > 1:
        ans.append(x)
    return f'{init_number}: ' + ' '.join(map(str, ans))

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('values', nargs='*', type=int)
    return parser

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()

    pool = Pool()
    print('\n'.join(pool.map(prime_factorization, args.values)))