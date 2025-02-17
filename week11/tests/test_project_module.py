
import pytest

from week11.my_project import project_module



def test_something(my_data):
    assert my_data == 42


'''
The function rolling_average() is expected to compute the moving average with period of 3. 

For input [1,2,3,4,5,6], the expected result is [2.0, 3.0, 4.0, 5.0] ,
'''
@pytest.mark.parametrize("values,expected_results",[
    (
            [1,2,3,4,5,6],
            [2.0, 3.0, 4.0, 5.0],
    ),
    (
            [-1,-2,-3,-4,-5,-6],
            [-2.0, -3.0, -4.0, -5.0], # add -5.0
    ),
])
def test_rolling_average(values,expected_results):

    result = project_module.rolling_average(values, 3)
    assert result == expected_results