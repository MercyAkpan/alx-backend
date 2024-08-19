#!/usr/bin/env python3
import csv
import math
from typing import List


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
            # This line skips the Title row.
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (
            isinstance(page, int) and page > 0) and (
            isinstance(page_size, int) and page_size > 0)
        indexes = self.index_range(page, page_size)
        start, end = indexes
        # print(start, end)
        # To populate self.__dataset.
        self.dataset()
        # This gives a total of number of lines in csv -1(Title row)
        length = len(self.__dataset)
        # print(length)
        # if (start < length) and (end > length):
        #     end = length
        if (start >= length) or (end > length) or length == 0:
            # print("inh here")
            return []
        return self.__dataset[start:end]

    # self is needed in this function, as it is part of a class.
    # And it would need to be called by an instance of a class.
    def index_range(self, page, page_size):
        # Gets page 1 = (0,7); page 2 = (7,14)
        # If page_size = 7 ,NT: last index is exclusive
        # and first index, inclusive
        return ((page - 1) * page_size, page * page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        self.total_dataset = len(self.dataset())
        total_pages = math.ceil(self.total_dataset / page_size)
        # Use self, so you can access this instance attribute
        # anywhere else. Otherwise, it becomes a local variable
        self.result_dict = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if (page + 1) < len(
                        self.__dataset) and (page < total_pages) else None,
            "prev_page": page - 1 if (page - 1) > 0 else None,
            "total_pages": total_pages
            }
        return self.result_dict
