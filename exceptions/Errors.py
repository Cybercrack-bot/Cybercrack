class NotRootError:
    "Raised when the framework isn't run with root"
    pass


class MissingCoreError:
    "Raised when the tool isn't installed completely"
    pass


class CommandNotFoundError:
    "Raised when the given command isn't found"
    pass


class OptionNotFoundError:
    "Raised when an invalid option is given"
    pass


class PayloadNotFoundError:
    "Raised when the payload doesn't exist"
    pass


