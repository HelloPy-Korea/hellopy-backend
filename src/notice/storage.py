import os

from django.core.files.storage import FileSystemStorage


class NoticeCKEditorStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        # notice/ckeditor 하위 경로로 저장
        notice_path = os.path.join("notice/ckeditor", name)
        return super().get_available_name(notice_path, max_length=max_length)
