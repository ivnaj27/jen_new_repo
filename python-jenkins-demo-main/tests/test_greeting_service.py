from app.greeting_service import GreetingService

def test_greeting_message():
    service = GreetingService()

    result = service.get_greeting("Jenkins")

    assert result == "Hello, Jenkins! Welcome to Jenkins CI/CD."
