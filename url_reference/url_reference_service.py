from .url_reference_model import UrlReferenceModel
import base64
import os
from database.database_init import Database
from sqlmodel import select


class UrlReferenceService:
    length_base_64 = 10

    def insert(self, url_target: str):
        code = base64.b64encode(os.urandom(self.length_base_64)).decode()[:self.length_base_64]

        database = Database()
        session = database.get_session()

        check_if_exist_url_reference = session.exec(select(UrlReferenceModel).where(UrlReferenceModel.url_target == url_target)).first()
        
        if check_if_exist_url_reference is not None:
            return check_if_exist_url_reference.url_code

        session.commit()
        session.add(UrlReferenceModel(url_code=code, url_target=url_target))

        session.commit()
        session.close()
        return code
    
    def get_by_code(self, url_code):
        database = Database()
        session = database.get_session()

        check_reference = session.exec(select(UrlReferenceModel).where(UrlReferenceModel.url_code == url_code)).first()

        if check_reference:
            return check_reference.url_target
        
        return None

        