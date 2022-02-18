def chmin(dp, i, candidate):
    if dp[i] > candidate:
        dp[i] = candidate
        return True
    return False


def chmax(dp, i, candidate):
    if dp[i] < candidate:
        dp[i] = candidate
        return True
    return False

# chmax, chmin 使わない


def fun1():
    # 入力
    n = int(input())
    h = list(map(int, input().split()))

    # DP テーブル初期化
    dp = []
    dp.append(0)
    dp.append(abs(h[0] - h[1]))

    # 計算
    for i in range(len(h)):
        if i == 0 or i == 1:
            continue
        d1 = abs(h[i]-h[i-1])
        d2 = abs(h[i]-h[i-2])

        d_new = None
        if d1 < d2:
            d_new = d1 + dp[i-1]
        else:
            d_new = d2 + dp[i-2]

        dp.append(d_new)

    # 出力
    print(dp[-1])


# chmax, chmin 使わない
def fun2():
    # 入力
    n = int(input())
    h = list(map(int, input().split()))

    # DP テーブル無限大で初期化
    dp = []
    for i in range(len(h)):
        dp.append(float('inf'))

    dp[0] = 0
    dp[1] = abs(h[0] - h[1])

    # 計算
    for i in range(len(h)):
        if i == 0 or i == 1:
            continue
        d1 = abs(h[i]-h[i-1])
        d2 = abs(h[i]-h[i-2])

        chmin(dp, i, d1 + dp[i-1])
        chmin(dp, i, d2 + dp[i-2])

    # 出力
    print(dp[-1])


# 配る DP
def fun3():
    # 入力
    n = int(input())
    h = list(map(int, input().split()))
    h.append(float("inf"))
    h.append(float("inf"))

    # DP テーブル無限大で初期化
    dp = []
    for i in range(n + 2):
        dp.append(float('inf'))

    dp[0] = 0

    # 計算
    for i in range(n):
        d1 = abs(h[i + 1]-h[i])
        chmin(dp, i+1, d1 + dp[i])

        d2 = abs(h[i+2]-h[i])
        chmin(dp, i+2, d2 + dp[i])

    # 出力
    print(dp[n-1])


def main():
    # fun1()
    # fun2()
    fun3()


if __name__ == "__main__":
    main()
