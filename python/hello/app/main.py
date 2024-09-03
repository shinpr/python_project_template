from hello.app.container import Container
from hello.usecase.hello import Hello as HelloInteractor

def main():
    container = Container()
    hello_interactor = container.injector.get(HelloInteractor)
    hello_interactor.show_message()

if __name__ == "__main__":
    main()
