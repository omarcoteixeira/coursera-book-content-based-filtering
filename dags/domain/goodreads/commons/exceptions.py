import logging
from pydantic import BaseModel


LOGGER = logging.getLogger(__name__)


class DataValidationException(Exception):

    def __init__(self, message: str, data_model: BaseModel) -> None:
        super().__init__(message)
        LOGGER.error(message)

        self.data_model = data_model


class InvalidRequestException(Exception):

    def __init__(self, url: str, error: str) -> None:
        message = f"Invalid Request from {url=}. Error: {error}"
        super().__init__(message)
        LOGGER.error(message)
