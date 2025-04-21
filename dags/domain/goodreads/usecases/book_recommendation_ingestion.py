import logging
from typing import List, Dict

import pandas as pd
import kagglehub

from domain.goodreads.models import Book

from domain.goodreads.database import (
    save_dataframe_to_database
)

LOGGER = logging.getLogger(__name__)


class BookRecommendationsIngestionUseCase:

    def __init__(self, database_session) -> None:
        self.database_session = database_session
        self.books = List[Dict]

    def execute(self) -> pd.DataFrame:
        LOGGER.info("Retrieving book recommendation list from Kaggle.")
        ds_path = kagglehub.dataset_download("jealousleopard/goodreadsbooks")
        self.books = pd.read_csv(f"{ds_path}/books.csv", on_bad_lines='skip')

        LOGGER.info(f"Total records found {len(self.books)}")

        print(f"Path to dataset files: {ds_path}")
        self._transform()
        self._save()

    def _transform(self):
        LOGGER.info("Converting book recommendation list accordingly with the requirements.")
        
        return
    
    def _save(self):
        LOGGER.info("Saving records at the database.")

        save_dataframe_to_database(
            self.database_session, dataframe=self.books, model=Book
        )
