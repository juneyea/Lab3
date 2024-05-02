import Lab3 as test

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = test.bubble_sort(input_arr, test.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = test.bubble_sort(input_arr, test.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = test.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_more_ten():
    result = []
    input_arr = [20,10,2,24,5,1,8,3,34,11,14.36]
    result = test.bubble_sort(input_arr,3)
    assert (result == 1)

def test_bubble_zero():
    
    input_arr = []
    result = test.bubble_sort(input_arr,4)
    assert (result == 0 )

def test_bubble_not_integer():
    result = []
    input_arr = [1.0,2,3,4,4,4,2.3]
    result = test.bubble_sort(input_arr,5)
    assert (result == 2 )