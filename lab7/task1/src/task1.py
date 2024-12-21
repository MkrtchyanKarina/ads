from utils import File


def exchange(money: int, coins: list[int]) -> int:
    dp = [0] + [float('inf')] * money
    for coin in coins:
        for j in range(coin, money+1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[money]


def exchange_with_amount(money: int, coins: dict[int: list[int]]) -> int:
    dp = [0] + [float('inf')] * money
    for c in coins.keys():
        denomination = c
        amount = coins[c]
        if amount > 0:
            for j in range(denomination, money+1):
                dp[j] = min(dp[j], dp[j - denomination] + 1)
    return dp[money]


def limits(money: int, amount: int, coins: list[int]) -> bool:
    if (1 <= money <= 10**3) and (1 <= amount == len(coins) <= 100) and all(1 <= c <= 10**3 for c in coins):
        return True
    else:
        return False


def exchange_txt() -> None:
    f = File(__file__)
    arguments = f.read()
    money, amount = list(map(int, arguments[0].split(" ")))
    coins = list(map(int, arguments[1].split(" ")))
    if limits(money, amount, coins):
        answer = exchange(money, coins)
        f.write(str(answer))


if __name__ == "__main__":
    exchange_txt()
