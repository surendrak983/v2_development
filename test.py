from services.attachment_service import (
    AttachmentService
)

svc = AttachmentService()

print(
    svc.get_company_folder(
        "500325"
    )
)