import contextlib

@contextlib.contextmanager
def nest_test(name):
    print("Entering", name)
    yield name
    print("exiting", name)


@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception')
        if propagate:
            raise
