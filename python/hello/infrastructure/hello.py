from hello.domain.repository.hello import Hello as HelloInterface
from hello.domain.entity.hello import Hello as HelloEntity

class Hello(HelloInterface):
    def get_message(self) -> HelloEntity:
        hello = HelloEntity(
            message="Hello, World!"
        )
        return hello