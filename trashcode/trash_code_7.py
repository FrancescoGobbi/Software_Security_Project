
def func1(arg1, arg2):
    var15 = func5()
    var34 = func6(arg2, arg1)
    var38 = func7(var15, arg2)
    var43 = func9(var15, var34)
    var44 = (arg1 ^ var34) & arg1 & arg1
    var45 = var34 ^ var38
    var46 = var34 + (var38 ^ var43) ^ var38
    if var45 < var45:
        var47 = -2027561704 ^ arg2 - var15 | 400
    else:
        var47 = -1146409496 & (arg1 - var46) | var45
    var48 = (var46 | var43) | (var43 & 288)
    var49 = ((var46 - 199609886) & 986) + -351
    var50 = ((var44 ^ var38) ^ -2088430066) - arg1
    var51 = var38 ^ (-1875209980 + (var45 | var34))
    var52 = var50 | var45
    var53 = var51 & var34 | var48
    var54 = (var45 | arg1) - var43 - var48
    var55 = var44 | (var51 - arg2)
    result = (var51 & var55 - var3
8a4
4 | arg2 + (var38 - var53) - ((var38 | arg2 + (arg1 ^ var38)) + var53)) | var48
    return result
def func9(arg39, arg40):
    var41 = 0
    for var42 in xrange(23):
        var41 += var42 + (var42 & 5)
    return var41
def func6(arg16, arg17):
    var18 = (-804 + 734 - arg17) & arg17
    var19 = 1137281602 ^ arg16 - arg16
    var20 = var19 ^ arg17 + -168155151
    var21 = var18 - var20
    var22 = var19 - (509 - -847) ^ var19
    var23 = var19 | -972
    var24 = (var20 - var18 ^ var22) + var21
    var25 = arg17 + var21
    var26 = var24 ^ var21 ^ arg17 - var20
    var27 = 405 - var23 ^ var19
    var28 = -872902590 ^ ((var22 & var24) - var18)
    var29 = arg17 + -8622176
    var30 = (var23 | var24) + -945640173
    var31 = arg16 ^ (-247087844 & var29) - arg17
    var32 = var30 - (var25 & var22 ^ var23)
    var33 = var27 & arg17 | var22 ^ var25
    result = var28 + (var19 & var30) | var30 ^ var33 + (var23 + var29)
    return result
def func5():
    func2()
    result = len(func4(4, 8))
    func3()
    return result
def func4(arg3, arg4):
    var5 = arg4 + arg3 & arg4
    yield var5
    var6 = var5 ^ (977 | (837 + -1614251448))
    yield var6
    var7 = -1856285269 - 782496411 ^ var6 | arg4
    yield var7
    var8 = (580 + arg4 + var6) ^ var6
    yield var8
    var9 = var7 ^ var7 | (var8 + arg3)
    yield var9
    var10 = arg4 & (var5 ^ -1806741609 & var5)
    yield var10
    var11 = (arg3 & (var8 | var6)) ^ var5
    yield var11
    var12 = var8 & 939015646 + var8
    yield var12
    var13 = (var7 & var6) + arg4 ^ var12
    yield var13
    var14 = var13 & var7
    yield var14
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : -2
def func7(arg35, arg36):
    def func8(acc, rest):
        var37 = (4 & 6) | acc
        if acc == 0:
            return var37
        else:
            result = func8(acc - 1, var37)
            return result
    result = func8(10, 0)
    return result
