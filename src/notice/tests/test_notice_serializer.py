from typing import Any

import pytest
from rest_framework.exceptions import ValidationError

from notice.models import Notice
from notice.serializers import NoticeSerializer, NoticeSummarizeListSerializer


@pytest.fixture
def create_notices():
    notice1 = Notice.objects.create(title="Title A", content="Content A", is_pinned=False)
    notice2 = Notice.objects.create(title="Title B", content="Content B", is_pinned=True)
    notice3 = Notice.objects.create(title="Title C", content="Content C", is_pinned=False)
    return [notice1, notice2, notice3]


@pytest.mark.django_db
@pytest.mark.feature
def test_notice_summarize_list_serializer_output(create_notices):
    # Given
    notices = create_notices

    # When
    serializer = NoticeSummarizeListSerializer(notices, many=True)
    data = serializer.data

    # Then
    assert len(data) == len(notices)
    for notice_data, notice in zip(data, notices):
        assert notice_data["id"] == notice.id
        assert notice_data["title"] == notice.title
        assert notice_data["is_pinned"] == notice.is_pinned
        assert "content" not in notice_data


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned",
    [
        ("Title 1", "The best way to learn Python is to practice coding every day.", False),
        ("What is the best way to learn Python?", "Answer1", False),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
        ),
    ],
)
def test_notice_serializer_is_valid_true_given_valid_data(
    title: str, content: str, is_pinned: bool
) -> None:
    # Given
    valid_data: dict[str, Any] = {
        "title": title,
        "content": content,
        "is_pinned": is_pinned,
    }

    # When
    serializer = NoticeSerializer(data=valid_data)
    is_valid: bool = serializer.is_valid()

    # Then
    assert is_valid is True
    assert serializer.errors == {}
    assert serializer.validated_data == valid_data


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned",
    [
        (None, "The best way to learn Python is to practice coding every day.", False),
        ("What is the best way to learn Python?", None, False),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            None,
        ),
        ("a" * 256, "The best way to learn Python is to practice coding every day.", False),
    ],
)
def test_notice_serializer_is_valid_false_given_invalid_data(
    title: str | None, content: str | None, is_pinned: bool | None
) -> None:
    # Given
    invalid_data: dict[str, Any] = {
        "title": title,
        "content": content,
        "is_pinned": is_pinned,
    }

    # When
    serializer = NoticeSerializer(data=invalid_data)
    is_valid: bool = serializer.is_valid()

    # Then
    assert is_valid is False
    assert serializer.errors != {}
    assert serializer.validated_data == {}


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned",
    [
        ("Title 1", "The best way to learn Python is to practice coding every day.", False),
        ("What is the best way to learn Python?", "Answer1", False),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
        ),
    ],
)
def test_notice_serializer_create_success_given_valid_data(
    title: str, content: str, is_pinned: bool
) -> None:
    # Given
    valid_data: dict[str, Any] = {
        "title": title,
        "content": content,
        "is_pinned": is_pinned,
    }
    serializer = NoticeSerializer(data=valid_data)
    assert serializer.is_valid()

    # When
    notice = serializer.save()

    # Then
    assert Notice.objects.count() > 0
    assert notice.title == title
    assert notice.content == content
    assert notice.is_pinned == is_pinned


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned, updated_title, updated_content, updated_is_pinned",
    [
        (
            "Title 1",
            "The best way to learn Python is to practice coding every day.",
            False,
            "Updated Title 1",
            "Updated Content 1",
            True,
        ),
        (
            "What is the best way to learn Python?",
            "Answer1",
            False,
            "Updated What is the best way to learn Python?",
            "Updated Answer1",
            False,
        ),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
            "Updated What is the best way to learn Python?",
            "Updated The best way to learn Python is to practice coding every day.",
            False,
        ),
    ],
)
def test_notice_serializer_update_success_given_valid_data(
    title: str,
    content: str,
    is_pinned: bool,
    updated_title: str,
    updated_content: str,
    updated_is_pinned: bool,
) -> None:
    # Given
    valid_data: dict[str, Any] = {"title": title, "content": content, "is_pinned": is_pinned}
    update_data: dict[str, Any] = {
        "title": updated_title,
        "content": updated_content,
        "is_pinned": updated_is_pinned,
    }
    notice = Notice.objects.create(**valid_data)
    serializer = NoticeSerializer(notice, data=update_data)
    assert serializer.is_valid()

    # When
    notice = serializer.save()

    # Then
    assert notice.title == updated_title
    assert notice.content == updated_content
    assert notice.is_pinned == updated_is_pinned


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, is_pinned, updated_title, updated_content, updated_is_pinned",
    [
        (
            "Title 1",
            "The best way to learn Python is to practice coding every day.",
            False,
            "Invalid Updated Title 1",
            None,
            None,
        ),
        (
            "What is the best way to learn Python?",
            "Answer1",
            False,
            None,
            "Invalid Updated Content 1",
            False,
        ),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
            None,
            None,
            "Invalid Updated Is Pinned",
        ),
        (
            "Title 1",
            "The best way to learn Python is to practice coding every day.",
            False,
            "a" * 256,
            "The best way to learn Python is to practice coding every day.",
            False,
        ),
    ],
)
def test_notice_serializer_update_failure_given_invalid_data(
    title: str,
    content: str,
    is_pinned: bool,
    updated_title: str | None,
    updated_content: str | None,
    updated_is_pinned: bool | str | None,
) -> None:
    # Given
    valid_data: dict[str, Any] = {"title": title, "content": content, "is_pinned": is_pinned}
    update_data: dict[str, Any] = {
        "title": updated_title,
        "content": updated_content,
        "is_pinned": updated_is_pinned,
    }
    notice = Notice.objects.create(**valid_data)
    serializer = NoticeSerializer(notice, data=update_data)

    # Then
    with pytest.raises(ValidationError):
        # When
        serializer.is_valid(raise_exception=True)
