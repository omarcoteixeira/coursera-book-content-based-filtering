from datetime import datetime, timedelta

from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from airflow.models.baseoperator import chain

from domain.goodreads.usecases.book_recommendation_ingestion import BookRecommendationsIngestionUseCase
from domain.goodreads.database import (
    create_database_session,
    save_dataframe_to_database,
)

default_args = {
    "owner": "omarcoteixeira",
    "retry": 1,
    "retry_delay": timedelta(minutes=5),
}


def process_kaggle_book_recommendation_dataset(**kwargs):
    database_session = kwargs["database_session"]
    data = BookRecommendationsIngestionUseCase().execute()
    # save_dataframe_to_database(
    #     database_session=database_session, dataframe=data, model=Company
    # )


@dag(
    dag_id="goodreads_etl",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    tags=["goodreads", "kaggle"],
)
def goodreads_etl():
    database_session = create_database_session("book_recommender")
    arguments = {"database_session": database_session}

    process_kaggle_book_recommendation_dataset_task = PythonOperator(
        task_id="process_kaggle_book_recommendation_dataset",
        python_callable=process_kaggle_book_recommendation_dataset,
        provide_context=True,
        op_kwargs=arguments,
    )

    chain(
        process_kaggle_book_recommendation_dataset_task
    )


GOODREADS_ETL = goodreads_etl()
