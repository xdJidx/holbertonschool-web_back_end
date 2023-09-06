#!/usr/bin/env python3
"""
return a tuple of size two containing a start index and an end
index corresponding to the range of indexes to return in a list
for those particular pagination parameters.
"""
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range

    Args:
        page (int): Number of page
        page_size (int): Total number of page

    Returns:
        tuple[int, int]: return in a list for those particular
                         pagination parameters
    """
    # Calculate the start index
    start_index = (page - 1) * page_size
    # Calculate the end index
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: liste of pages
        """
        assert isinstance(page, int) and\
            page > 0, "Page must be an integer greater than 0"
        assert isinstance(page_size, int) \
            and page_size > 0, "Page size must be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset) or start_index < 0:
            return []
        return dataset[start_index:end_index]
