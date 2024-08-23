#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]  # Not used
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This method, is used to get the data from the indexed dataset
        """
        assert (index < len(self.__indexed_dataset))
        max_index = max(self.__indexed_dataset.keys())
        data = []
        current_index = index
        collected_items_count = 0
        while collected_items_count < page_size:
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
                collected_items_count += 1
            current_index += 1
        if current_index > max_index:
            next_index = None  # Signal end of dataset
        else:
            next_index = current_index
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
        }
