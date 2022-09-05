# https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions

def kinetic_energy(m:'in KG', v:'in M/S')->'Joules': 
    return 1/2*m*v**2

print(kinetic_energy.__annotations__)
#{'return': 'Joules', 'v': 'in M/S', 'm': 'in KG'}



print(
    '{:,} {}'.format(kinetic_energy(12,30),
        kinetic_energy.__annotations__['return'])
)


rd={'type':float,'units':'Joules',
    'docstring':'Given mass and velocity returns kinetic energy in Joules'}
def f()->rd:
    pass

print(  f.__annotations__['return']['type']     )
#<class 'float'>
print(  f.__annotations__['return']['units']    )
#'Joules'
print(  f.__annotations__['return']['docstring']    )
#'Given mass and velocity returns kinetic energy in Joules'


def validate(func, locals):
    for var, test in func.__annotations__.items():
        value = locals[var]
        try: 
            pr=test.__name__+': '+test.__docstring__
        except AttributeError:
            pr=test.__name__   
        msg = '{}=={}; Test: {}'.format(var, value, pr)
        assert test(value), msg

def between(lo, hi):
    def _between(x):
            return lo <= x <= hi
    _between.__docstring__='must be between {} and {}'.format(lo,hi)       
    return _between

def f(x: between(3,10), y:lambda _y: isinstance(_y,int)):
    validate(f, locals())
    print(x,y)
    
# f(2,2) 
# AssertionError: x==2; Test: '_between: must be between 3 and 10'
# f(3,2.1)
# AssertionError: y==2.1; Test: '<lambda>'

print('*'*100)

def function(name:str ,age:int) -> "printing the personal details ":
    print(f"name is {name} age is {age}")

function("test",20)
print(function.__annotations__)


# https://peps.python.org/pep-3107/

# Lambda
# lambda’s syntax does not support annotations. The syntax of lambda could be changed to support annotations, by requiring #parentheses around the parameter list. However it was decided [12] not to make this change because:
# It would be an incompatible change.
# Lambdas are neutered anyway.
# The lambda can always be changed to a function.