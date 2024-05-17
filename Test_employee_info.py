import employee_info as test

def test_calculate_average_salary():
    result = 0
    result = test.calculate_average_salary()
    assert result == 60166.6667

def test_get_employees_by_dept():
    result = []
    result = test.get_employees_by_dept("Marketing")
    assert result == [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
                        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000 }]

def test_get_employees_by_age_range():
    result = []
    result = test.get_employees_by_age_range(20,31)
    assert result == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]