from repository.attachment_repository import (
    AttachmentRepository
)

repo = AttachmentRepository()

rows = repo.get_latest()

for row in rows:
    print(row)