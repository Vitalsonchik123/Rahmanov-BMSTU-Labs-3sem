data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

def absFunc(x):
    return abs(x)

# без lambda
result = sorted(data, key=absFunc, reverse=True)
print(result)

# lambda функциия
lambdaRes = sorted(data, key=lambda x: abs(x), reverse=True)
print(lambdaRes)
