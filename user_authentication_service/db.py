#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The User object representing the added user.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound(
                    "No user found with the specified criteria.")
            return user
        except NoResultFound as e:
            raise NoResultFound(f"Error in finding user: {e}")

    def update_user(self, user_id: int, **kwargs) -> None:
        try:
            user_to_update = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(User, key):
                    setattr(user_to_update, key, value)
                else:
                    raise ValueError(f"Invalid attribute: {key}")
            self._session.commit()
        except NoResultFound:
            raise NoResultFound(f"No user found with ID: {user_id}")
        except InvalidRequestError as e:
            raise InvalidRequestError(f"Invalid request error: {e}")
