def max_profit_solution(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    income = 0
    left, right = 0, 1
    while right < len(prices):
        if income < prices[right] - prices[left]:
            income = prices[right] - prices[left]
        if prices[right] < prices[left]:
            left = right
        right += 1
    return income


if __name__ == '__main__':
    print(max_profit_solution([1,2]))
