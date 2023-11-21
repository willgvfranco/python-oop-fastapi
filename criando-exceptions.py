from math import e


class MyError(Exception):
    ...


class AnotherError(Exception):
    pass


try:
    raise MyError("ae", "oi", "tchau")
except (MyError, ZeroDivisionError) as error:
    print("dentro except")
    print(error)
    exception_ = AnotherError("vou lançar de novo")
    # exception_.__notes__ = error.__notes__.copy()
    exception_.add_note("mais uma")
    raise exception_ from error
