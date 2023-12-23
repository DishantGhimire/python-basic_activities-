def check(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
check(2, 3, 4, a=1, b=5 )
