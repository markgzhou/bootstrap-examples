class AService:

    def __init__(self, name):
        self.name = name

    def hello_method(self, ):
        return f'Hello {self.name}'

    @staticmethod
    def hello_static_method(name: str):
        return f'Hello {name}'
