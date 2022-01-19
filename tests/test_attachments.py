from ewapi import CRUD
from ewapi.utils.db_connection import create_db_engine, get_session


class TestAttachment:
    def test_verify_attachment(self):
        create_db_engine(test=False)
        with get_session() as session:
            with open("tests/resources/financial_cat.jpg", 'rb') as file:
                file_content = file.read()
                attachment_id = CRUD.attachments.create_attachment(session=session,
                                                                   proposal_id=1,
                                                                   filename="test.jpg",
                                                                   file_content=file_content)
                session.commit()
                attachment = CRUD.attachments.get_attachment(1, attachment_id)
                assert attachment.file_content == file_content
