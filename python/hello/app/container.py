from injector import Injector, Module, provider
from hello.infrastructure.hello import Hello as HelloRepository
from hello.usecase.hello import Hello as HelloInteractor

class MyModule(Module):
    @provider
    def provide_hello_repository(self) -> HelloRepository:
        return HelloRepository()

    @provider
    def provide_hello_interactor(self, helloRepository: HelloRepository) -> HelloInteractor:
        return HelloInteractor(
            helloRepository=helloRepository
        )

class Container:
    def __init__(self):
        self.injector = Injector([MyModule()])