# encoding:utf8
def div(a,b):
    # assert 断言 后面接1个表达式 如果为真，继续执行。否则就中断，并抛出AssertionError异常
    # assert type(a)==int
    assert isinstance(a,int)
    print('a is int')
    assert type(b)==int
    print('b is int')
    print(a/b)

div(5,'b')