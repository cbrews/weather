from typing import Any


class NotFound(Exception):
    """
    Wrapper exception for not found errors
    """

    def __init__(self, obj: type, *args: Any, **kwargs: Any):
        self.obj = obj
        super().__init__(*args, **kwargs)
