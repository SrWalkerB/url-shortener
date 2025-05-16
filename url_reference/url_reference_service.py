from .url_reference_model import UrlReferenceModel
import base64
import os
from database.database_init import Database


class UrlReferenceService:
    length_base_64 = 10

    def insert(self, url_target: str):
        code = base64.b64encode(os.urandom(self.length_base_64)).decode()[:self.length_base_64]

        database = Database()
        session = database.get_session()

        session.add(UrlReferenceModel(url_target=url_target, url_code=code))

        session.commit()

        session.close()
        return code
        