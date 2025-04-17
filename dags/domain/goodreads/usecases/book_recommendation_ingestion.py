import logging
from typing import List, Dict

import pandas as pd

# from domain.goodreads.models import Company

from domain.goodreads.commons.validation import validate_data
from domain.goodreads.commons.url import get_data_from_url

LOGGER = logging.getLogger(__name__)


class BookRecommendationsIngestionUseCase:

    def __init__(self) -> None:
        self.books = List[Dict]

    def execute(self) -> pd.DataFrame:
        LOGGER.info("Retrieving book recommendation list from Kaggle.")

        LOGGER.info(f"Books found: {len(self.books)}")
        return self._transform()

    def _transform(self):
        LOGGER.info("Converting book recommendation list accordingly with the requirements.")
        result = pd.DataFrame(self.books)
        return result
