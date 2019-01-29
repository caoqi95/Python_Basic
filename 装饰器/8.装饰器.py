# 类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建 logit
# 使其能够用于不同的场景来输出日志

from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass

# 这个是实现有一个附加优势，在于比嵌套函数的方式更加整洁，
# 而且包裹一个函数还是使用跟以前一样的语法：
@logit()
def myfunc1():
    pass

# 现在给 logit 创建一个子类，来添加 发 email 的功能（具体怎么实现发 email 就不写了）
class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass