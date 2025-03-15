import pytest
from django.db.utils import DatabaseError

from notice.models import Notice


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned",
    [
        ("Welcome", "Welcome to our notice board.", False),
        ("Update", "The system will be updated at midnight.", False),
        ("Reminder", "Don't forget the meeting tomorrow.", False),
    ],
)
def test_create_notice_success_given_valid_data(title: str, content: str, is_pinned: bool) -> None:
    # Given
    notice_data: dict[str, str] = {"title": title, "content": content, "is_pinned": is_pinned}

    # When
    notice = Notice.objects.create(**notice_data)

    # Then
    assert notice.title == notice_data.get("title")
    assert notice.content == notice_data.get("content")
    assert notice.is_pinned == notice_data.get("is_pinned")


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned",
    [
        (None, "Welcome to our notice board.", False),
        ("Update", None, False),
        ("Update", "Welcome to our notice board", None),
        (None, None, None),
    ],
)
def test_create_notice_fail_given_invalid_data(
    title: str | None, content: str | None, is_pinned: bool | None
) -> None:
    # Given
    notice_data: dict[str, str | bool | None] = {
        "title": title,
        "content": content,
        "is_pinned": is_pinned,
    }

    # Then
    with pytest.raises(DatabaseError):
        # When
        Notice.objects.create(**notice_data)


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned",
    [
        ("Welcome", "Welcome to our notice board.", False),
        ("Update", "The system will be updated at midnight.", False),
        ("Reminder", "Don't forget the meeting tomorrow.", True),
    ],
)
def test_read_notice_given_exist_notice_id(title: str, content: str, is_pinned: bool) -> None:
    # Given
    notice_data: dict[str, str] = {"title": title, "content": content, "is_pinned": is_pinned}
    notice = Notice.objects.create(**notice_data)

    # When
    fetched = Notice.objects.get(id=notice.id)

    # Then
    assert fetched.title == notice_data.get("title")
    assert fetched.content == notice_data.get("content")
    assert fetched.is_pinned == notice_data.get("is_pinned")


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "notice_id",
    [-1, 0],
)
def test_read_notice_given_non_exist_notice_id(notice_id: int) -> None:
    # Given
    # When
    with pytest.raises(Notice.DoesNotExist):
        # Then
        Notice.objects.get(id=notice_id)


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned, updated_title, updated_content, updated_is_pinned",
    [
        (
            "Welcome",
            "Welcome to our notice board.",
            False,
            "Update Welcome",
            "Update Welcome to our notice board.",
            True,
        ),
        (
            "Update",
            "The system will be updated at midnight.",
            False,
            "Update Update",
            "Update The system will be updated at midnight.",
            True,
        ),
        (
            "Reminder",
            "Don't forget the meeting tomorrow.",
            True,
            "Update Reminder",
            "Update Don't forget the meeting tomorrow.",
            False,
        ),
    ],
)
def test_update_notice_success_given_valid_data(
    title: str,
    content: str,
    is_pinned: bool,
    updated_title: str,
    updated_content: str,
    updated_is_pinned: bool,
) -> None:
    # Given
    notice_data: dict[str, str] = {"title": title, "content": content, "is_pinned": is_pinned}
    notice = Notice.objects.create(**notice_data)

    notice.title = updated_title
    notice.content = updated_content
    notice.is_pinned = updated_is_pinned
    notice.save()

    updated = Notice.objects.get(id=notice.id)
    assert updated.title == updated_title
    assert updated.content == updated_content
    assert updated.is_pinned == updated_is_pinned


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned, updated_title, updated_content, updated_is_pinned",
    [
        (
            "Welcome",
            "Welcome to our notice board.",
            False,
            None,
            "Welcome to our notice board.",
            False,
        ),
        (
            "Update",
            "The system will be updated at midnight.",
            False,
            "Update",
            None,
            False,
        ),
        (
            "Reminder",
            "Don't forget the meeting tomorrow.",
            True,
            None,
            None,
            None,
        ),
    ],
)
def test_update_notice_fail_given_invalid_data(
    title: str,
    content: str,
    is_pinned: bool,
    updated_title: str | None,
    updated_content: str | None,
    updated_is_pinned: bool | None,
) -> None:
    # Given
    notice_data: dict[str, str] = {"title": title, "content": content, "is_pinned": is_pinned}
    notice = Notice.objects.create(**notice_data)

    # When
    notice.title = updated_title
    notice.content = updated_content
    notice.is_pinned = updated_is_pinned

    # Then
    with pytest.raises(DatabaseError):
        notice.save()


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_deleted",
    [
        ("Welcome", "Welcome to our notice board.", False),
        ("Update", "The system will be updated at midnight.", False),
        ("Reminder", "Don't forget the meeting tomorrow.", False),
    ],
)
def test_delete_notice_when_soft_delete_operation(
    title: str, content: str, is_deleted: bool
) -> None:
    # Given
    notice_data: dict[str, object] = {
        "title": title,
        "content": content,
        "is_deleted": is_deleted,
    }
    notice = Notice.objects.create(**notice_data)
    notice_id = notice.id

    # When
    notice.delete()

    # Then
    deleted = Notice.objects.get(id=notice_id)
    assert deleted.is_deleted is True


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_deleted",
    [
        ("Welcome", "Welcome to our notice board.", True),
        ("Update", "The system will be updated at midnight.", True),
        ("Reminder", "Don't forget the meeting tomorrow.", True),
    ],
)
def test_delete_notice_when_hard_delete_operation(
    title: str, content: str, is_deleted: bool
) -> None:
    # Given
    notice_data: dict[str, str | bool] = {
        "title": title,
        "content": content,
        "is_deleted": is_deleted,
    }
    notice = Notice.objects.create(**notice_data)
    notice_id = notice.id

    # When
    notice.delete(force_delete=True)

    # Then
    with pytest.raises(Notice.DoesNotExist):
        Notice.objects.get(id=notice_id)
