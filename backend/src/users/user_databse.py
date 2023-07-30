from typing import Dict, Any

from fastapi_users.models import UP
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


class CustomSQLAlchemyUserDatabase(SQLAlchemyUserDatabase):
    async def create(self, create_dict: Dict[str, Any]) -> UP:
        user = self.user_table(**create_dict)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user, ['posts'])
        return user
