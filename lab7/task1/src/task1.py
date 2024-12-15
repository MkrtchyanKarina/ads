import typing as tp
from lab7.src.utils import File



def exchange(money: int, coins):
    dp = [0] + [float('inf')] * money
    for coin in coins:
        for j in range(coin, money+1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[money]


def exchange_with_amount(money: int, coins: dict):
    dp = [0] + [float('inf')] * money
    for c in coins.keys():
        denomination = c
        amount = coins[c]
        if amount > 0:
            for j in range(denomination, money+1):
                dp[j] = min(dp[j], dp[j - denomination] + 1)
    return dp[money]

print(exchange(34, (1, 3, 4)))
# def limits(array_len: int, commands: tp.List[str]) -> bool:
#     if 1 <= array_len == len(commands) <= 5*10**5 and all(abs(int(x.split(" ")[1])) <= 10**18 for x in commands):
#         return True
#     else:
#         return False
#
#
# def hash_table_txt():
#     f = File(__file__)
#     arguments = f.read()
#     array_len = int(arguments[0])
#     commands = arguments[1:array_len+1]
#     if limits(array_len, commands):
#         ex = HashTable(commands).actions()
#         answer = "\n".join(ex)
#         f.write(answer)
#
#
# if __name__ == "__main__":
#     hash_table_txt()
