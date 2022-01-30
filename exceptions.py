#!/usr/bin/env Python3
import output as o


class PromptException(BaseException):
    def __init__(self, message: str) -> None:
        o.error(message)


class PromptPermissionError(PromptException):
    '''
    This is raised when the program performs an action which requires admin permissions
    '''
    def __init__(self, message: str) -> None:
        o.error(message)


class DirectoryException(PromptException):
    '''
    This is raised when the user asks for an inexistent directory
    '''
    def __init__(self, directory: str) -> None:
        print(message := f"{directory} doesn't exist")
        super().__init__(message)


class CommandException(PromptException):
    '''
    This is raised when the user asks for an inexistent command
    '''
    def __init__(self, command: str) -> None:
        o.error(f"The {command.split()[0]} command doesn't exist")


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
        o.error(
            f"""You inserted a {type_}-type variable. 
            A {expected_} was expected."""
        )


class FolderPermissionError(PromptPermissionError):
    '''
    This is raised when the program performs an action on an existing directory
    '''
    def __init__(self, folder: str) -> None:
        message = f"Prompt.py doesn't have the permission to create {folder}"
        PromptPermissionError(message)