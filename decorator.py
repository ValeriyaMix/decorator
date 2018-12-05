import time
import inspect


def check_type(thing):
    def wrap():
        if inspect.isfunction(thing):
            start = time.clock()
            elapse = time.clock() - start
            print('foo started /n')
            print('foo finished in', elapse)
        elif inspect.isclass(thing):
            start = time.clock()
            elapse = time.clock() - start
            print('Bar started /n')
            print('Bar finished in', elapse)
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

# foo()
Bar()