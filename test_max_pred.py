import hypothesis.strategies as s
from hypothesis import given, event, note, settings, Verbosity

@given(s.lists(s.integers(), min_size=1))
def test_max_pred(l):
    max_val = f(l)
    assert max_val in l
    assert all(max_val >= x for x in l)
    
def f(l):
    if len(l) > 5:
        return None
    if len(l) == 0:
        return None
    max_val = l[0]
    for x in l:
        if x > max_val:
            max_val = x
    return max_val
