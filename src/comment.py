from dataclasses import dataclass, field
from typing import Optional, List


class Yorum:
    def __init__(self, text: str,
                 topic: Optional[str],
                 sentiment: Optional[str],
                 source: Optional[str]):
        self.text = text
        self.topic = topic
        self.sentiment = sentiment
        self.source = source

    def __len__(self):
        return len(self.text.split(" "))


@dataclass
class Comment:
    text: str
    topic: str = field(default=None)
    sentiment: str = field(default=None)
    source: str = field(default=None)

    def __len__(self):
        return len(self.text.split(" "))

    @property
    def tokens(self) -> List[str]:
        return self.text.split(" ")

