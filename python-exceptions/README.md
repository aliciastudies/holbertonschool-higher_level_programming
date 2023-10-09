## What’s the difference between errors and exceptions
**Errors** are issues that prevent your code from even starting. **Exceptions** are issues that can occur while your code is running. 



## What are exceptions and how to use them

Exceptions occur during the execution of a program. They represent runtime errors that can happen when a program is trying to perform an operation.

Common errors include:

- `TypeError`
- `ValueError`
- `ZeroDivisionError`
- Custom exceptions can be made when needed

### Try-except

Try-except blocks handle unexpected issues and keep the program from crashing.

```
try:
    # Code that might raise an exception
except SomeExceptionType as e:
    # Code to handle the exception
else:
    # Optional code to run if no exception occurred
finally:
    # Optional cleanup code, runs whether an exception occurred or not
```

1. `try` - where the code that might raise an exception is written.

2. `except` - if an exception of the specified type is raised in `try`, the code inside the `except` block is executed. Specific exceptions can be caught by specifying the exception type after the `except` keyword. `as` can also be used to assign the exception object to a variable for further inspection.

3. `else` (optional) - is executed if no exception occurs in `try`. It's used for code that should run when the `try` block completes successfully.

4. `finally` (optional) - is always executed, regardless of whether an exception occurred or not. It's commonly used for cleanup tasks, like closing files or releasing resources.

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Cleanup code here")

# Output:
# Error: division by zero
# Cleanup code here
```

A `ZeroDivisionError` is raised and caught. The error message is printed, and then the code in the `finally` is executed for cleanup.

Using exceptions prevents the program from crashing and to provide more informative error messages or alternative actions when errors occur.

## When do we need to use exceptions

### File operations
When working with files, exceptions can handle issues like file not found, permission denied, or read/write errors

```
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied to access the file.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
```

### User input validation

```
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(f"Invalid input: {e}")

```
### Custom error handling
```
class CustomError(Exception):
    pass

def some_function():
    if some_condition:
        raise CustomError("This is a custom error.")

try:
    some_function()
except CustomError as e:
    print(f"Custom error occurred: {e}")

```

## How to correctly handle an exception
- Be specific as possible with the types of exceptions
- Use multiple smaller blocks to isolate and handle exceptions
- Write concise and imformative error messages to explain what went wrong and why
- Include test cases that forces exceptions to occur to ensure the handling is working as expected
- Document the expected exceptions and the handling strategies

## What’s the purpose of catching exceptions

### Error Recovery
It allows the program to recover from an error condition and keep running. it allows some level of functionality and provides a better user experience and prevents crashes.

### Debugging and Troubleshooting
Caught exceptions can be logged or display detailed error messages that help diagnose and fix issues in the code. It makes it easier to locate and correct problems. Logging the handling can help with identifying recurring issues.

### Resource Clean-up
It can ensure resources like files, network and database connections are properly closed and released, even if the error occurs.

## How to raise a builtin exception

The raise statement forces a specified exception to occur. The program jumps to the nearest try-except block that can handle the raised exception. If there isn't an appropriate try-except block, Python will look in the calling function (the one that call the current function). This process continues up the call stack until an appropriate try-except block is found or the top of the program is reached. If the latter, the program will terminate and an error message is displayed.

```
raise ExceptionType("Optional error message")

```

ExceptionType is the type of the built-in exception you want to raise. E.g. `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`.

Optional error message can provide more information about why the exception was raised. This message is accessible through the exception object.

## When do we need to implement a clean-up action after an exception

It is the last task before the try statement completes and will run whether or not the try statement produces an exception. This helps maintain program integrity, prevents leaks and ensure that the code behaves as expected even when errors are encountered.