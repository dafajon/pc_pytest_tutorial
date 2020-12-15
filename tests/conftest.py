import pytest
from src.comment import Comment
from typing import Tuple


@pytest.fixture()
def comments() -> Tuple[Comment, ...]:
    c1 = Comment("bu harika.")
    c2 = Comment("cebahe zihniyeti hayınlığa devam ediyor.", topic='politics')
    c3 = Comment("of çok iyyi.")

    return c1, c2, c3
