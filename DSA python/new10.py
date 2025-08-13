def test(*args):
 if len(args)>2:
    sum=0
    for num in args:
        sum+=(num**2)
    return sum
