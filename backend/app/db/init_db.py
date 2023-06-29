# @Author: Lanbao Shen
# @Create: 2023/6/28 21:30
from sqlalchemy.orm import Session

from app import schemas
from app import crud
from app.core.config import settings
from app.db.base_class import Base
from app.db.session import engine

# https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # TODO: Change to Alembic migrations
    Base.metadata.create_all(bind=engine)
    user = crud.user.get_by_username(db, username=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            email=settings.FIRST_SUPERUSER_EMAIL,
            is_superuser=True
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
