class GreetingService:
    """
    Service responsible for generating greeting messages.
    """

    def get_greeting(self, name: str) -> str:
        return f"Hello, {name}! Welcome to Jenkins CI/CD."
