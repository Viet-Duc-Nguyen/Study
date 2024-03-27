### Teacher Piet
### 28.04.2023
### Py Basics day 9

## Handling Exceptions


# try:
#     x = int(input('Please give a number: '))
#     print(x/0)
# except ZeroDivisionError:
#     print('Divided by zero')



'''
### The try statement works as follow:
- First, the try clause is executed
- If no exception occurs, the except clause is skipped and execution of the try statement is finished
- If an exception occurs duting execution of the try clause, the rest of the try clause is skipped and the except clause is executed
- If an exception occurs which does not match the exception named in the except clause, it is an unhandled exception and execution stops
'''


# try:
#     x = int(input('Please give a number: '))
#     print(1/x)
#     print('hello world!')
# except (ValueError, ZeroDivisionError):
#     print('do not divide zero')



# try:
#     x = int(input('Please give a number: '))
#     print(1/x)
# except:
#     print('Error')



# try:
#     x = int(input('Please give a number: '))
#     print(1/x)
# except Exception as e:
#     print('Error', e)



# try:
#     1 + 'Hello'
# finally:
#     print('Goodbye, world')

# print('This will not be executed')



# def bool_return():
#     try:
#         return True
#     finally:
#         return False

# print(bool_return())


# def dangerous_call(num):
#     print(1+num)

# def after_call():
#     print('everything alright')

# try:
#     dangerous_call('2')
#     after_call()
# except TypeError:
#     print('Type Erroe')


# try:
#     dangerous_call(2)
# except TypeError:
#     print('Type error')
# else:
#     after_call()


# raise NameError('Hi there')

try:
    raise NameError('Hi there')
except NameError:
    print('An exception flew by!')
