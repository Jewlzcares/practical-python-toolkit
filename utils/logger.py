class ConsoleLogger:
    """
    Simple helper class for colored CLI output.
    Pure ANSI (no external dependencies).
    """

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    @staticmethod
    def warn(msg: str):
        print(ConsoleLogger.YELLOW + "[WARNING] " + msg + ConsoleLogger.RESET)

    @staticmethod
    def error(msg: str):
        print(ConsoleLogger.RED + "[ERROR] " + msg + ConsoleLogger.RESET)

    @staticmethod
    def success(msg: str):
        print(ConsoleLogger.GREEN + "[SUCCESS] " + msg + ConsoleLogger.RESET)

    @staticmethod
    def info(msg: str):
        print(ConsoleLogger.BLUE + "[INFO] " + msg + ConsoleLogger.RESET)