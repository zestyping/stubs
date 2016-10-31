# stubs

Tools for setting up stubs and mocks in Python.  Example:

    def f(x):
        return x * 2

    with stub[f](_ >= 3) >> 5:
        print(f(2))  # prints 4
        print(f(3))  # prints 5
    print(f(3))  # prints 6

For more details, see the docstrings in `stubs.py` and `matchers.py`.
