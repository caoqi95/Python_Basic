# 现在看看装饰器的几个使用场景

# 装饰器能有助于检查某个人是否被授权去使用一个 web 应用的端点（endpoint）。
# 它们被大量使用 Flask 和 Django web 框架中。下面是一个例子，来使用基于装饰器的授权：
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    
    return decorated


# 日志是装饰器运用的另一个亮点。这是个例子：
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called