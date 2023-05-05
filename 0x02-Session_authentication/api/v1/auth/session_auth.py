#!/usr/bin/env python3
"""Module for the Session Authentication class"""


import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Contains the properties and methods of the
    session authentication class
    """

    user_id_by_session_id: dict = {}

    def create_session(
        self,
        user_id: str = None
    ) -> str:
        """creates a session id for a user_id
        """

        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = uuid.uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(
        self,
        session_id: str = None
    ) -> str:
        """returns a user_id based on a session_id"""

        if session_id is None:
            return None
        if session_id is None:
            return None
        return self.user_id_by_session_id.get(session_id)
