from src.comment import Comment
import pytest


__famous_quote__ = "Hello world."


def test_hello():
    assert __famous_quote__ == "Hello world."


def test_initialization1():
    assert Comment(text="Bu adamda ahlak olsa o filmde çıplak sahnede oynamazdı.",
                topic="Magazin",
                sentiment="Negative",
                source="ahaber")


def test_initialization2():
    assert Comment(text="Oyuncularınızı sakatlayacağız. Hakem cebimizde.",
                topic="Spor",
                sentiment="Negative",
                source="fotomaç")


def test_len():
    c = Comment(text="Tebrikler bu başarı hepimizin.")
    assert len(c) == 4


def test_tokens():
    c = Comment(text="Bu harika!")
    assert c.tokens == ["Bu", "harika!"]


def test_conftest(comments):
    assert len(comments[0]) == 2
    assert comments[1].topic == 'politics'
    assert comments[2].tokens == ['of', 'çok', 'iyyi.']


@pytest.mark.skip(reason="Not yet implemented.")
def test_remove_punts():
    assert False


def test_error():
    assert True
