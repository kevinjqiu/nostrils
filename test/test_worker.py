import worker

def test_add():
    assert 1 == worker.add(1, 0)

def test_add___negative():
    assert 0 == worker.add(-1, 1)

def test_subtract():
    assert 0 == worker.subtract(0, 0)

class TestFoo(object):

    def test_add(self):
        assert 5 == worker.add(5, 0)
