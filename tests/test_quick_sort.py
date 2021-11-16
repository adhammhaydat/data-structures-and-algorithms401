from data_structure.quick_sort.quick_sort import  quick_sort

def test_merge_sort():
    expected = [4, 8, 15, 16, 23, 42]
    arr=[8,4,23,42,16,15]
    quick_sort(arr,0,len(arr)-1)
    actual=arr
    assert actual == expected

    