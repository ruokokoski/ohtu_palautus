from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username) != None:
            raise UserInputError("Username in use")
        
        valid_username = True
        valid_password = True
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3 or not username.isalpha() or not username.islower():
            valid_username = False
        
        if len(password) < 8 or password.isalpha():
            valid_password = False

        if valid_password and len(username) < 3:
            raise UserInputError("Too short username")
        
        if valid_username:
            if len(password) < 8:
                raise UserInputError("Too short password")
            elif password.isalpha():
                raise UserInputError("Invalid password")
            
        if password != password_confirmation:
            raise UserInputError("Passwords do not match")
        


user_service = UserService()
