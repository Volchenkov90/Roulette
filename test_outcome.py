import pytest
from outcome import Outcome



@pytest.mark.parametrize (
    "name_1, name_2, expect",
    [
        (["Red", 1], ["Red", 1], True),
        (["Red", 1], ["Red", 2], False)
        
    ]

   
)
def test_eq(name_1, name_2, expect):
    o1 = Outcome(name_1[0], name_1[1])
    o2 = Outcome(name_2[0], name_2[1])
    assert (o1 == o2) == expect
    

def test_2():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Red", 1)
    o3 = Outcome("Black", 1)
    set_1 = set()
    set_1.add(o1)
    assert len(set_1) == 1