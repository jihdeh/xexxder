from typing import List


class PersonEntity:
    """Person Entity

    Person entity data structure
    """

    id = str
    name = str
    films = List[str]

    def __getitem__(self, key: str):
        return self[key]
