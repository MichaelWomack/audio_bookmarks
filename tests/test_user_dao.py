import pytest
from app.model import User
from app.persistence import UserDAO
from tests.conftest import get_test_connection_manager

@pytest.mark.usefixtures('setup_test_db')
class TestUserDAO(object):

    @pytest.fixture
    def dao( self ):
	    connection_manager = get_test_connection_manager()
	    return UserDAO( connection_manager=connection_manager )


    def test_insert_user(self, dao: UserDAO):
        user = User(email='fake@email.com', password='fake_pswd')
        dao.insert(user)
        user = dao.get_by_id(1)
        assert user != None
        assert user.email == 'fake@email.com'
        assert user.password == 'fake_pswd'
