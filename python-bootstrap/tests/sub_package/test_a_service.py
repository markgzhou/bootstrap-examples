from source.sub_package.a_service import AService


class TestAService:
    class_for_test = AService('Mark')

    def test_hello_method(self):
        assert self.class_for_test.hello_method() == 'Hello Mark'

    @staticmethod
    def test_static_hello_method():
        assert AService.hello_static_method('Mark') == 'Hello Mark'
