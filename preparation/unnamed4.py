def foo(param1, *param2):
    print(param1)
    print(param2)


foo(1, 2, 3, 4, 5)


def bar(param1, **param2):
    print(param1)
    print(param2)


bar(1, a=2, b=3)

