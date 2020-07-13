def ciccio(a):
    return a*5


def casa(a):
    return a*6


x = 10
if(x>5):
    print("ciao")
else:
    x = ciccio(x) + casa(x)
    print(x)