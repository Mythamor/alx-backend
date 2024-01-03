#!/usr/bin/env python3

"""
Module: 2-hypermedia_pagination.py
"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    """
    start_index = (page - 1) * page_size
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
        """
        that takes two integer arguments page with default value 1
        and page_size with default value 10.
        """
        # Read csv file
        with open('Popular_Baby_Names.csv', 'r') as file:
            reader = csv.reader(file)
            dataset = list(reader)

        # Validate the arguments
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate the range
        start_index, end_index = index_range(page, page_size)

        return dataset[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:

        data = self.dataset()

        total_pages = math.ceil(len(data) / page_size)

        if page < 1 or page > total_pages:
            return {
                'page_size': 0,
                'page': page,
                'data': [],
                'next_page': None,
                'prev_page': None,
                'total_pages': total_pages

                    }

        data = self.get_page(page, page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        data_dict = {

                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages

                }

        return data_dict
