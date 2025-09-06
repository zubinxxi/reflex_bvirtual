import reflex as rx 
from fastapi import FastAPI, Depends

from reflex_local_auth.user import LocalUser
from bvirtual.models.auth.auth_models import UserInfo, User_Role

# Create a FastAPI app
fastapi_app = FastAPI(title="My API")

class UsersAPI:
    """API for user-related operations."""
    users: list[UserInfo] = []


    @staticmethod
    def get_user_info_by_user_id(user_id: int) -> UserInfo:
        """Get user info by user ID."""
        return rx.session.exec(
            rx.select(UserInfo).where(UserInfo.user_id == user_id)
        ).first()

    @staticmethod
    def get_user_info_by_email(email: str) -> UserInfo:
        """Get user info by email."""
        return rx.session.exec(
            rx.select(UserInfo).where(UserInfo.email == email)
        ).first()

    @staticmethod
    def get_all_users() -> list[UserInfo]:
        """Get all users."""
        return rx.session.exec(rx.select(UserInfo)).all()

# Aquí es donde cambias el decorador.
@fastapi_app.get("/users/")
def get_users() -> list[UserInfo]:
    """API endpoint to get all users."""
    return UsersAPI.get_all_users()
        
