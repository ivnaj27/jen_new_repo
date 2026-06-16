from app.greeting_service import GreetingService
from app.logger_config import get_logger

logger = get_logger()

def main():
    logger.info("Application started")

    service = GreetingService()
    message = service.get_greeting("Jenkins")

    print(message)

    logger.info("Application completed successfully")

if __name__ == "__main__":
    main()
