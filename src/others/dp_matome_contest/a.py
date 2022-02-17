def main():
    # s1 = input().split()
    h = [2, 9, 4, 5, 1, 6, 10]

    dp = []
    dp.append(0)
    dp.append(abs(h[0] - h[1]))

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

    print(dp)


if __name__ == "__main__":
    main()
