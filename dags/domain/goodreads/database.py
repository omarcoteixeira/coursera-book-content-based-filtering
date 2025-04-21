import logging
import pandas as pd

from airflow.hooks.postgres_hook import PostgresHook

from sqlalchemy.orm import sessionmaker, Session

from domain.goodreads.models import DataTypes, Base


LOGGER = logging.getLogger(__name__)


def create_database_session(connection_id: str) -> Session:
    LOGGER.info("Creating database session.")
    hook = PostgresHook(postgres_conn_id=connection_id)
    engine = hook.get_sqlalchemy_engine()

    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()


def save_dataframe_to_database(
    database_session: Session, dataframe: pd.DataFrame, model: DataTypes
):
    LOGGER.info("Saving results to database.")
    dataframe.to_sql(
        con=database_session.get_bind(),
        name=model.__tablename__,
        index=False,
        if_exists="replace",
    )

