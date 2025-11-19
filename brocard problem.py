import math

def find_factorial_square_solutions(max_n: int = 20):
    """
    n! + 1 = m^2 를 만족하는 (n, m)을 n=1 ~ max_n 범위에서 모두 찾는다.
    max_n: n의 최댓값
    """
    fact = 1  # n! 값을 누적해서 계산 (매번 factorial 호출하면 느림)

    solutions = []

    for n in range(1, max_n + 1):
        fact *= n        # n! 업데이트
        value = fact + 1 # n! + 1

        # 제곱수인지 확인: m = floor(sqrt(value)) 한 뒤 m^2 == value 이면 perfect square
        m = math.isqrt(value)
        if m * m == value:
            print(f"찾았다! n={n}, m={m}, n!+1={value}")
            solutions.append((n, m, value))

    if not solutions:
        print(f"n=1 ~ {max_n} 범위에서는 해가 없다.")
    else:
        print("\n정리:")
        for n, m, v in solutions:
            print(f"n={n}, m={m}, n!+1={v}")

    return solutions

if __name__ == "__main__":
    # 원하는 만큼 n의 최댓값을 올려가며 검색하면 된다.
    # 예: 10, 20, 50, 100 ...
    find_factorial_square_solutions(max_n=20)
