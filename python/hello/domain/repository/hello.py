from abc import ABC, abstractmethod
from hello.domain.entity.hello import Hello

class Hello(ABC):
    @abstractmethod
    def get_message(self) -> Hello:
        pass