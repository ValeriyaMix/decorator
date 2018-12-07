lsimport time
import inspect
from functools import wraps

def check_type(thing):
    @wraps(thing)
    def wrap(*args, **kwargs):
        if inspect.isfunction(thing):
            start = time.time()
            result = thing(*args, **kwargs)
            elapse = time.time() - start
            print(foo.__name__, 'started', '/n')
            print(foo.__name__, 'finished in', float("{0:.9f}".format(elapse)))
            return result
        elif inspect.isclass(thing):
            start = time.clock()
            elapse = time.clock() - start
            print(Bar.__name__, 'started /n')
            print(Bar.__name__, 'finished in', float("{0:.9f}".format(elapse)))
    return wrap


@check_type
# @profile
def foo():
    pass

@check_type
# @profile
class Bar:
  def __init__(self):
    pass

foo()
Bar()