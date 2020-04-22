
def func1(arg1, arg2):
    var3 = func4()
    var11 = var6(var3, arg1)
    var20 = var14(arg2, arg1)
    var24 = func11(var20, var3)
    var25 = var24 & (arg1 + arg2) - arg2
    var26 = arg1 - var11
    var27 = var20 + (var26 & var20) & 456
    var28 = 286 & var27 & -114 - var24
    var29 = var24 | 723
    var30 = (var28 + 327) | arg1 + var29
    var31 = arg2 - var28 & arg2 + var25
    if var24 < var26:
        var32 = ((var27 | -965) | var11) + -893584385
    else:
        var32 = var3 - var27 | var31
    var33 = (var29 - -1320714123) + var24
    var34 = var3 & var33 & var25
    var35 = (var30 + (var33 | var20)) | -302
    var36 = (arg1 ^ var31) | var29 + var11
    var37 = 459 & var35
    var38 = var33 + var11 - var20 + var31
    var39 = arg2 & var33
    var40 = var30 ^ var3 - var34
    var41 = (var28 - var26) ^ var27 | 395201194
    var42 = var35 + ((var30 & var33) -
774
 var33)
    var43 = var29 - arg2
    var44 = var11 ^ (var38 & var25)
    var45 = (var24 | (arg1 + var43)) - var35
    result = var39 | arg1
    return result
def func10(arg15, arg16):
    var17 = ((1878717682 | arg16 ^ -912 | (252 & ((((arg15 & (551106471 | arg15)) - 219 + arg15) + ((396 & arg15) + arg15) | (arg15 - -789)) | 827120329 | arg15 ^ -1262212400 | -581576479 + -105)) - -149) | arg15) + arg16
    var18 = -24517031 ^ ((arg16 ^ arg16 & -1189609197 - arg16) - -1325521492 + 1819488117)
    var19 = var18 | (((371649375 | var18) + var18) ^ arg16)
    result = arg15 ^ var18
    return result
def func9():
    closure = [-8]
    def func8(arg12, arg13):
        closure[0] += func10(arg12, arg13)
        return closure[0]
    func = func8
    return func
var14 = func9()
def func7(arg7, arg8):
    var9 = arg7 + 747
    var10 = arg7 - ((46 | var9 ^ -926) & arg8) + var9
    result = 1220562445 | arg8 | (1292351225 | ((-322951170 | var10) - (-181 & (arg7 ^ (1529842954 & arg7) & arg8) | 567)) - 928305735)
    return result
def func6():
    closure = [-10]
    def func5(arg4, arg5):
        closure[0] += func7(arg4, arg5)
        return closure[0]
    func = func5
    return func
var6 = func6()
def func4():
    func2()
    result = len((-9 & 2 - i for i in xrange(5)))
    func3()
    return result
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : 2
def func11(arg21, arg22):
    def func12(acc, rest):
        var23 = (rest + 4) - 4
        if acc == 0:
            return var23
        else:
            result = func12(acc - 1, var23)
            return result
    result = func12(10, 0)
    return result
