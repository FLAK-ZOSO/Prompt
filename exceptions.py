#usr/bin/env Python3


class PromptException(BaseException):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class DirectoryException(PromptException):
    '''
    This is raised when the user asks for an inexistent directory
    '''
    def __init__(self, message: str) -> None:
        super().__init__(message)


class CommandException(PromptException):
    '''
    This is raised when the user asks for an inexistent command
    '''
    def __init__(self, command: str) -> None:
        message = f"The {command} command doesn't exist"
        super().__init__(message)


class ArgumentException(PromptException):
    '''
    This is raised when the user inserts a wrong argument
    '''
    def __init__(self, message: str) -> None:
        super().__init__(message)


class ArgumentTypeException(ArgumentException):
    '''
    This is raised when the user inserts a wrong-type argument
    '''
    def __init__(self, type_: str, expected_: str) -> None:
        message = (
            f"""You inserted a {type_}-type variable. 
            A {expected_} was expected."""
        )
        super().__init__(message)