import logging
from sqlalchemy.exc import IntegrityError

import pandas as pd
import kagglehub


from domain.goodreads.models import Book, Author

LOGGER = logging.getLogger(__name__)


class BookRecommendationsIngestionUseCase:

    def __init__(self, database_session) -> None:
        self.database_session = database_session
        self.books = []
        self.authors = []

    def execute(self) -> pd.DataFrame:
        LOGGER.info("Retrieving book recommendation list from Kaggle.")
        ds_path = kagglehub.dataset_download("jealousleopard/goodreadsbooks")
        print(f"Path to dataset files: {ds_path}")

        df = pd.read_csv(f"{ds_path}/books.csv", on_bad_lines='skip')
        self._process_authors(df)
        self._process_books(df)

    def _process_authors(self, df: pd.DataFrame):
        existing_authors = self.database_session.query(Author).all()
        existing_author_names = {author.name: author for author in existing_authors}

        LOGGER.info("Saving authors records at the database.")
        all_authors = set()
        for record in df.to_dict("records"):
            individual_authors = [author.strip() for author in record['authors'].split('/')]
            all_authors.update(individual_authors)

        for author_name in all_authors:
            if author_name not in existing_author_names:
                author = Author(name=author_name)
                self.database_session.add(author)
                self.authors.append(author)
            else:
                self.authors.append(existing_author_names[author_name])

        self.database_session.commit()
        LOGGER.info("Authors records saved at the database.")

    def _process_books(self, df: pd.DataFrame):
        LOGGER.info("Saving book records at the database.")
        author_name_to_object = {author.name: author for author in self.authors}

        for record in df.to_dict("records"):
            try:
                    individual_authors = [author.strip() for author in record['authors'].split('/')]
                    book = Book(
                        isbn=record['isbn'],
                        isbn13=record['isbn13'],
                        title=record['title'],
                        average_rating=record['average_rating'],
                        language_code=record['language_code'],
                        num_pages=(0 if 'num_pages' not in record else record['num_pages']),
                        ratings_count=record['ratings_count'],
                        text_reviews_count=record['text_reviews_count'],
                        publication_date=record['publication_date'],
                        publisher=record['publisher']
                    )

                    for author_name in individual_authors:
                        if author_name in author_name_to_object:
                            book.authors.append(author_name_to_object[author_name])

                    self.database_session.add(book)
                    self.database_session.commit()
            except IntegrityError as e:
                self.database_session.rollback()  # Rollback the transaction to allow further processing
                print(f"Skipping duplicate entry: {record['title']} - {record.get('authors', '')}. Error: {e}")
            except Exception as e:
                self.database_session.rollback()
                print(f"An unexpected error occurred while processing: {record['title']}. Error: {e}")

        
        LOGGER.info("Book records saved at the database.")
