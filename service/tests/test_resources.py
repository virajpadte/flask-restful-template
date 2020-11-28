from api.resources.foo import Foo
from api.resources.bar import Bar

def test_foo_get():
    test_foo = Foo()
    assert test_foo.get() == None

def test_bar_get():
    test_bar = Bar()
    assert test_bar.get() == None

def test_foo_post():
    test_foo = Foo()
    assert test_foo.post() == None

def test_bar_post():
    test_bar = Bar()
    assert test_bar.post() == None
