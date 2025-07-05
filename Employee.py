class Employee:

    def __init__(self):
        print('Employee created...')

    def __del__(self):
        print('destructor called...')

def Create_obj():
    print('Making object...')
    obj = Employee()
    print('Function End...')
    return obj

print('Callin Create_obj() function...')
obj = Create_obj()
print('Program End...')