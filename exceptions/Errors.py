class NotRootError(Exception):
    "Raised when the framework isn't run with root"
    pass


class MissingCoreError(Exception):
    "Raised when the tool isn't installed completely"
    pass


class CommandNotFoundError(Exception):
    "Raised when the given command isn't found"
    pass


class OptionNotFoundError(Exception):
    "Raised when an invalid option is given"
    pass


class PayloadNotFoundError(Exception):
    "Raised when the payload doesn't exist"
    pass

