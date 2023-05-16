from my_package.module1 import get_sum as gs
from my_package.module1 import get_minus as gm
from my_package.module1 import get_multiply as getm
from my_package.module2 import get_division as gd
from my_package.module2 import get_raised_degree as grd
from my_package.utils.cli import main as m
num1 = 10
num2 = 5

print(gs(num1,num2))
print(gm(num1,num2))
print(getm(num1,num2))
print(gd(num1,num2))
print(grd(num1,num2))

m()