from ..persistence import ConnectionManager
from ..model import User
from .errors import EmailAlreadyExistsError
from flask import current_app
from psycopg2 import IntegrityError

class UserDAO():

    def __init__(self, connection_manager: ConnectionManager):
        self.connection_manager = connection_manager

    def insert(self, user: User):
        try: 
            with self.connection_manager as conn:
                cur = conn.cursor()
                insert_sql = """
                    INSERT INTO USERS (
                        email,
                        password
                    ) VALUES (%s, %s)
                """
                record = (user.email, user.password)
                cur.execute(insert_sql, record)
                conn.commit()
        except IntegrityError as e:
            current_app.logger.error(e)
            raise EmailAlreadyExistsError(e)
        

    def update(self, user: User):
        pass


    def get_by_id(self, user_id: int) -> User:
        with self.connection_manager as conn:
            cur = conn.cursor()
            query = """
                SELECT ID, EMAIL, PASSWORD FROM USERS WHERE ID = %s;
            """
            cur.execute(query, (user_id,))
            record = cur.fetchone()
            if record:
                return User(id=record[0], email=record[1], password=record[2])



    ##TODO unit test this.
    def get_by_email(self, user_email: str) -> User:
        with self.connection_manager as conn:
            cur = conn.cursor()
            query = """
                SELECT ID, EMAIL, PASSWORD FROM USERS WHERE EMAIL = %s;
            """
            cur.execute(query, (user_email,))
            record = cur.fetchone()
            if record:
                return User(id=record[0], email=record[1], password=record[2])