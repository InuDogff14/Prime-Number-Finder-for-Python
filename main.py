def is_prime(num):
    """
    与えられた数が素数かどうかを判断する関数

    引数:
        num (int): 素数かどうかを判定する対象の数

    戻り値:
        bool: 与えられた数が素数ならTrue、そうでなければFalse
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def find_primes(limit):
    """
    与えられた数までのすべての素数を見つける関数

    引数:
        limit (int): 素数を探す最大の数

    戻り値:
        list: 素数のリスト
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    limit = int(input("素数を探す上限の数を入力してください: "))
    primes = find_primes(limit)
    print(f"{limit} までの素数は以下の通りです:")
    print(primes)


if __name__ == "__main__":
    main()
