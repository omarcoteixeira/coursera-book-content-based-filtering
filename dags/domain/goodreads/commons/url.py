import logging
from typing import List, Dict

import requests

from domain.goodreads.commons.exceptions import InvalidRequestException


LOGGER = logging.getLogger(__name__)


def get_data_from_url(url: str, params=None, timeout=300) -> List[Dict]:
    LOGGER.info(f"Retrieving data from {url=}")
    result = requests.get(url, params=params, timeout=timeout)
    if result.status_code == 200:
        return result.json()
    raise InvalidRequestException(
        url, f"Retrieving data error from {url=}. Status code {result.status_code}"
    )
