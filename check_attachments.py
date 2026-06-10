from repository.attachment_repository import (
    AttachmentRepository
)

repo = AttachmentRepository()

for row in repo.get_latest(20):

    print(row)