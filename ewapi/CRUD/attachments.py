from ewapi.DTO import Proposal
from ewapi.DTO.attachments_DTO import Attachment
from ewapi.utils.db_connection import get_session, get_next_id


def get_attachments() -> list:
    with get_session() as session:
        attachments = session.query(Attachment).all()
    return attachments


def get_attachment(proposal_id: int, attachment_id: int) -> Attachment:
    with get_session() as session:
        attachment = session.query(Attachment).where(
            Attachment.attachment_id == attachment_id and Proposal.proposal_id == proposal_id
        ).first()
    return attachment


def create_attachment(session,
                      proposal_id: int,
                      filename: str,
                      file_content: bytes) -> int:
    new_id = get_next_id(session, Attachment.attachment_id)
    new_attachment = Attachment(attachment_id=new_id,
                                proposal_id=proposal_id,
                                filename=filename,
                                file_content=file_content)
    session.add(new_attachment)
    return new_id
