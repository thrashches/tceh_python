
def func_cancel_dec(func):

    def func_cancel():
        print('{} is cancelled!'.format(func.__name__))
    return func_cancel

def func_speed_dec(func):
    def func_speed(*args):
        from timeit import default_timer
        begin_time = default_timer()
        func(*args)
        end_time = default_timer()
        print("Function {} has been executed in {} seconds".format(func.__name__, end_time - begin_time))
    return func_speed

def func_exec_count_dec(func):
    func_exec_count_dec.count = 0
    def exex_count(*args, **kwargs):
        func(*args, **kwargs)
        func_exec_count_dec.count += 1
        print('Function {} has been executed {} times'.format(func.__name__, func_exec_count_dec.count))
    return exex_count

def func_log_dec(func):
    print('Log decorator created!')
    def log(*args, **kwargs):
        print('Function {} starts!'.format(func.__name__))
        func(*args, **kwargs)
        print('Function {} ends!'.format(func.__name__))

    return log


def func_exception_dec(func):
    def func_except(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print('Error {}!'.format(e))
    return func_except


@func_cancel_dec
def long(value):
    import time
    time.sleep(5) # delays for 5 seconds

    return 'long' + str(value)


@func_speed_dec
def short(string_param):
    print('Speed!', string_param)
    return 'short'

@func_exec_count_dec
def medium(value, *modificators):
    result = value
    for m in modificators:
        result *= m

    return result

@func_exception_dec
@func_log_dec
def change_sign(num, check_sign=True):
    if check_sign and num > 0:
        raise ValueError('num > 0!')
    return -num


long()
short('str')
medium(5, [2, 4, 5])
medium(3, [1, 2, 3])
change_sign(-11)
change_sign('1111')
