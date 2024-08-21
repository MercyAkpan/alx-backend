#!/usr/bin/env python3
"""
This module contains a function to
return the start and end indexes of a page
"""


def index_range(page, page_size):
    """
    This function returns a tuple of start and end index of a page
    """
    # Gets page 1 = (0,7); page 2 = (7,14)
    # If page_size = 7 ,NT: last index is exclusive
    # and first index, inclusive
    return ((page - 1) * page_size, page * page_size)
