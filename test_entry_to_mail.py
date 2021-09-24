import pytest



def test_is_str():
    s = 'abc'
    assert type(s) == str, 'not a string'

@pytest.mark.parametrize('s', ["",pytest.param("a", marks=pytest.mark.xfail),"123456"])
def test_is_str_len_even(s):
    assert len(s) % 2 == 0, "length of string is not even"
  
def test_is_str_deductible():
    try:
        assert 'aaa' - 'a'
    except TypeError:
        pass


   
def test_is_dict():
    d = {'a': 67, 'b': 20}
    assert type(d) == dict, 'not a dictionary'

@pytest.mark.parametrize('d', [{},pytest.param({'a': 67}, marks=pytest.mark.xfail),{'a': 67, 'b': 20}])
def test_is_dict_len_even(d):
    assert len(d) % 2 == 0, "length of dictionary is not even"

def test_is_dict_deductible():
    try:
        assert {'a': 67, 'b': 20} - {'b': 20}
    except TypeError:
        pass
