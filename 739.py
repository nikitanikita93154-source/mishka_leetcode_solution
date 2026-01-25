temp=[73,74,76,75,71,69,72,76,73]


def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []  # будет хранить индексы

    for i in range(n):
        # Пока стек не пуст и текущая температура выше, чем у дня на вершине стека
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index  # сколько дней ждали
        stack.append(i)

    return ans
print(daily_temperatures([73,74,76,75,71,69,72,76,73]))

