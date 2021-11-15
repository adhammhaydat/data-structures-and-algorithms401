from data_structure.insertion_sort.insertion_sort import insertion_sort


def test_insertion_sort():
    
    expected=[5, 5, 5, 7, 7, 12]
    actual=insertion_sort([5,12,7,5,5,7])

    assert actual == expected

def test_insertion_sort_str():
    
    expected=['c', 'd', 'e', 'e', 'f', 'g']
    actual=insertion_sort(["g","e","c","d","e","f"])

    assert actual == expected