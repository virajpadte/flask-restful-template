from api.resources.foo import Foo
from api.resources.bar import Bar

def test_foo_get():
    test_foo = Foo()
    assert test_foo.get() == None

def test_foo_post():
    test_foo = Foo()
    assert test_foo.post() == None