from sample import worker

def test_add():
    assert 1 == worker.add(1, 0)

def test_add___negative():
    assert 0 == worker.add(-1, 1)

def test_subtract():
    assert 0 == worker.subtract(0, 0)

class TestFoo(object):

    def test_add(self):
        assert 5 == worker.add(5, 0)

    def test_multi(self):
        assert 55 == worker.multi(5, 11)

def test_with_yield():

    def assert_arithmetic(op, expected, *args):
        assert expected == apply(op, args)

    yield assert_arithmetic, worker.add, 5, 2, 3
    yield assert_arithmetic, worker.subtract, 1, 3, 2
    yield assert_arithmetic, worker.multi, 99, 11, 9
