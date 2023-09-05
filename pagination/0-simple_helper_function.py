#!/usr/bin/env python3
"""
return a tuple of size two containing a start index and an end 
index corresponding to the range of indexes to return in a list 
for those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
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
