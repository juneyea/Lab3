import price_info as test

def test_total_cost_shopping():
    test.price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
    test.quantity_list= {'apple': 10, 'orange':10, 'watermelon': 10, 'pineapple': 10, 'pear' : 10, 'papaya': 10, 'pomegranate': 10}
    result = 0
    result = test.total_cost_shopping()
    assert result == 206
    
def test_cost_of_fruits():
    result = 0
    fruit = 'apple'
    quantity = 10
    result = test.cost_of_fruits(fruit, quantity)
    assert result == 12



