"""
Project: SimpleForm
Author: Alan Reis Anjos
License: Creative Commons Attribution 4.0 International License
License Details: https://creativecommons.org/licenses/by/4.0/
"""

def showItemList(count: int, spacing: int, orderedList: bool):
    assert isinstance(count, int), f"The count must be an integer."
    assert isinstance(spacing, int), f"The spacing must be an integer."
    assert isinstance(orderedList, bool), f"The orderedList must be a boolean."

    return f"{ spacing * " " }{ f'{ count }.' if orderedList else '-'}"