from typing import List, Dict, Type
from pydantic import BaseModel

from domain.goodreads.commons.exceptions import DataValidationException

def validate_data(data: List[Dict], model: Type[BaseModel]) -> None:
    for item in data:
        try:
            model.model_validate(item)
        except Exception as e:
            raise DataValidationException(repr(e), model) from e
