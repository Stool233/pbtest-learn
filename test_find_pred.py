
import hypothesis.strategies as s
from hypothesis import given, event, note, settings, Verbosity

@given(s.lists(s.integers()), s.integers())
def test_find(l, x):
    out = find(l, x)
    if out == -1:
        assert x not in l
    else:
        assert l[out] == x
        assert x not in l[0:out]
    


def find(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1