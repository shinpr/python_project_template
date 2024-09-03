from hello.domain.repository.hello import Hello as HelloRepository

class Hello:
    def __init__(self, helloRepository: HelloRepository):
        self.helloRepository = helloRepository

    def show_message(self) -> None:
        message = self.helloRepository.get_message()
        print(message.message) # TODO: usecaseから出す