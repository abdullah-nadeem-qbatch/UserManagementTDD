import unittest
from User import User

class User_test(unittest.TestCase):
    def setUp(self):
        self.fixture = self._Fixture()


    def test_user_created(self):
        self.fixture.given_credentials('abd282', 'PaKiStAn123','Ali Ahmad', 'abd@gmail.com', '22')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(True)


    def test_user_already_exists(self):
        self.fixture.given_credentials('abd282', 'QbAtCh321', 'Bilal Shafiq', 'abc@gmail.com', '25')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(False)

    def test_invalid_username(self):
        self.fixture.given_credentials('Abdullah Nadeem', 'dlajfFJSL', 'Akbar', 'bcd@gmail.com', '21')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(False)


    def test_invalid_email(self):
        self.fixture.given_credentials('Abd2820', 'fklsajlf', 'Mushtaq', 'cde@com.gmail', '30')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(False)


    def test_invalid_name(self):
        self.fixture.given_credentials('Abd2820', 'fklsajlf', 'Mushtaq123', 'cde@gmail.com', '30')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(False)


    def test_weak_password(self):
        self.fixture.given_credentials('xyz125', '12341234', 'Karim', 'xyz@hotmail.com', '27')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(False)

    
    def test_age(self):
        self.fixture.given_credentials('xyz125', 'dajfadhds', 'Karim', 'xyz@hotmail.com', '2x')
        self.fixture.when_create_user_function_is_called()
        self.fixture.then_result_should_be(False)


    def test_missing_fields(self):
        self.fail()
    
    
    def test_user_not_exists_on_deletion(self):
        self.fixture.given_search_user_by_username(self.username)
        self.fixture.when_delete_user_function_is_called()
        self.fixture.then_result_should_be(False)


    def test_database_connection_established(self):
        self.fail()


    def test_user_updated(self):
        self.fixture.given_search_user_by_username(self.username)
        self.fixture.when_update_user_function_is_called()
        self.fixture.then_result_should_be(True)


    def test_user_deleted(self):
        self.fixture.given_search_user_by_username(self.username)
        self.fixture.when_delete_user_function_is_called()
        self.fixture.then_result_should_be(True)


    def test_user_found(self):
        self.fail()


    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.user = User()

        
        def given_credentials(self, username, password, name, email, age):
            self.username = username
            self.password = password
            self.name = name
            self.email = email
            self.age = age


        def given_search_user_by_username(self, username):
            self.username = username


        def when_create_user_function_is_called(self):
            self.result = self.user.create_user(self.username, self.password, self.name, self.email, self.age)

        
        def when_delete_user_function_is_called(self):
            self.result = self.user.delete_user(self.username)

        
        def when_update_user_function_is_called(self):
            self.result = self.user.update_user(self.username)


        def when_read_user_function_is_called(self):
            self.result = self.user.delete_user(self.username)


        def then_result_should_be(self, expected_result):
            self.assertAlmostEqual(expected_result, self.result)
