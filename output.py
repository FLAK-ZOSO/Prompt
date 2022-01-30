from colorama import Back, Fore, Style


def abort(message: str) -> None:
    print(f'{Back.RED}{Fore.YELLOW}[ABORT] {message}{Style.RESET_ALL}')


def argument(message: str, end='') -> str:
    message = message.removesuffix(' ')
    return input(f'{Back.MAGENTA}{Fore.WHITE}[ARGUMENT] {message}{Style.RESET_ALL} {end}')


def documentation(message: str, end: str='\n') -> str:
    return print(f'{Back.BLUE}{Fore.YELLOW}{message}{Style.RESET_ALL}{end}')


def error(message: str) -> None:
    print(f'{Back.RED}{Fore.BLACK}[ERROR] {message}{Style.RESET_ALL}')


def question(message: str, end: str='') -> None:
    return input(f'{Back.BLACK}{Fore.WHITE}[QUESTION] {message}{Style.RESET_ALL}{end}')


def system(message: str, end: str=' ') -> None:
    print(f'{Fore.CYAN}[SYSTEM] {message}{Style.RESET_ALL}', end=end)


def warn(message: str) -> None:
    print(f'{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}')


def done(end: str=' ') -> None:
    print(f'{Back.WHITE}{Fore.BLACK}[DONE]{Style.RESET_ALL}', end=end)


def failed() -> None:
    print(f'{Back.RED}{Fore.BLACK}[FAILED]{Style.RESET_ALL}')


def false() -> None:
    print(f'{Back.RED}{Fore.BLACK}[FALSE]{Style.RESET_ALL}')


def true() -> None:
    print(f'{Back.GREEN}{Fore.BLACK}[TRUE]{Style.RESET_ALL}')