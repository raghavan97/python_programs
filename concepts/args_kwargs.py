

'''
*args is used to send a non-keyworded variable length argument list to the
function.
'''


def my_args_func(arg1, *args):
    print 'arg1={}'.format(arg1)
    count = 2
    for a in args:
        print 'arg{}={}'.format(count, a)
        count += 1

'''
**kwargs allows you to pass keyworded variable length of arguments to a
function.
'''


def my_kwargs_func(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s = %s" % (key, value)

my_args_func(1, 'what', 'is', 'this', 5, 'about')
print '-------------------------'

my_kwargs_func(a=1, b=2, c=3)

print '-------------------------'
my_args = {'a': 1, 'b': 2, 'c': 3}
my_kwargs_func(**my_args)
