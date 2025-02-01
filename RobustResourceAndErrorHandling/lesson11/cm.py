import contextlib

@contextlib.contextmanager
def nest_test(name):
    print("Entering", name)
    yield name
    print("exiting", name)
