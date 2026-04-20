#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs:
            index: The current index in the dataset (0-indexed).
            next_index: The next index to query with,
            or None if there is no next index.
            page_size: The current page size.
            data: The page of the dataset corresponding to
            the current index and page size.
        Args:
            index (int): The current index in the dataset (0-indexed).
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary containing pagination information
            and the dataset page.
        """
        dataset = self.indexed_dataset()
        max_index = max(dataset.keys())

        assert index is None or (
            type(index) is int and 0 <= index <= max_index
        )

        data = []
        current_index = 0 if index is None else index
        next_index = current_index
        count = 0

        while count < page_size and next_index <= max_index:
            if next_index in dataset:
                data.append(dataset[next_index])
                count += 1
            next_index += 1

        return {
            "index": current_index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
