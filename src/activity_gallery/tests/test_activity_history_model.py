import pytest
from django.db.utils import DatabaseError

from activity_gallery.models import ActivityHistory


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, activity_date",
    [
        ("Activity 1", "Content 1", "2024-01-01"),
        ("Activity 2", "Content 2", "2024-06-01"),
        ("Activity 3", "Content 3", "2023-12-31"),
    ],
)
def test_create_activity_history_success_given_valid_data(title, content, activity_date):
    # Given
    data = {
        "title": title,
        "content": content,
        "activity_date": activity_date,
    }
    # When
    history = ActivityHistory.objects.create(**data)
    # Then
    assert history.title == title
    assert history.content == content
    assert str(history.activity_date) == activity_date


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, activity_date",
    [
        (None, "Content", "2024-01-01"),
        ("Title", None, "2024-01-01"),
        ("Title", "Content", None),
        (None, None, None),
    ],
)
def test_create_activity_history_fail_given_invalid_data(title, content, activity_date):
    # Given
    data = {
        "title": title,
        "content": content,
        "activity_date": activity_date,
    }
    # Then
    with pytest.raises((DatabaseError, ValueError, TypeError)):
        # When
        ActivityHistory.objects.create(**data)


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, activity_date",
    [
        ("Activity 1", "Content 1", "2024-01-01"),
        ("Activity 2", "Content 2", "2024-06-01"),
    ],
)
def test_read_activity_history_given_exist_id(title, content, activity_date):
    # Given
    history = ActivityHistory.objects.create(
        title=title, content=content, activity_date=activity_date
    )
    # When
    fetched = ActivityHistory.objects.get(id=history.id)
    # Then
    assert fetched.title == title
    assert fetched.content == content
    assert str(fetched.activity_date) == activity_date


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "history_id",
    [-1, 0],
)
def test_read_activity_history_given_non_exist_id(history_id):
    # Given
    # When / Then
    with pytest.raises(ActivityHistory.DoesNotExist):
        ActivityHistory.objects.get(id=history_id)


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, activity_date, new_title, new_content, new_activity_date",
    [
        ("Activity 1", "Content 1", "2024-01-01", "Updated 1", "Updated Content 1", "2024-02-01"),
        ("Activity 2", "Content 2", "2024-06-01", "Updated 2", "Updated Content 2", "2024-07-01"),
    ],
)
def test_update_activity_history_success_given_valid_data(
    title, content, activity_date, new_title, new_content, new_activity_date
):
    # Given
    history = ActivityHistory.objects.create(
        title=title, content=content, activity_date=activity_date
    )
    # When
    history.title = new_title
    history.content = new_content
    history.activity_date = new_activity_date
    history.save()
    updated = ActivityHistory.objects.get(id=history.id)
    # Then
    assert updated.title == new_title
    assert updated.content == new_content
    assert str(updated.activity_date) == new_activity_date


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "title, content, activity_date, new_title, new_content, new_activity_date",
    [
        ("Activity 1", "Content 1", "2024-01-01", None, "Updated Content", "2024-02-01"),
        ("Activity 2", "Content 2", "2024-06-01", "Updated", None, "2024-07-01"),
        ("Activity 3", "Content 3", "2024-06-01", "Updated", "Updated Content", None),
    ],
)
def test_update_activity_history_fail_given_invalid_data(
    title, content, activity_date, new_title, new_content, new_activity_date
):
    # Given
    history = ActivityHistory.objects.create(
        title=title, content=content, activity_date=activity_date
    )
    # When
    history.title = new_title
    history.content = new_content
    history.activity_date = new_activity_date
    # Then
    with pytest.raises((DatabaseError, ValueError, TypeError)):
        history.save()


@pytest.mark.django_db
@pytest.mark.feature
def test_delete_activity_history_hard_delete():
    # Given
    history = ActivityHistory.objects.create(
        title="To Delete", content="Delete me", activity_date="2024-01-01"
    )
    history_id = history.id
    # When
    # If using soft delete, use hard delete method; otherwise, keep as is
    history.delete(force_delete=True)
    # Then
    with pytest.raises(ActivityHistory.DoesNotExist):
        ActivityHistory.objects.get(id=history_id)


@pytest.mark.django_db
@pytest.mark.feature
def test_delete_activity_history_when_soft_delete_operation() -> None:
    # Given
    history = ActivityHistory.objects.create(
        title="To Delete", content="Delete me", activity_date="2024-01-01"
    )

    # When
    history.delete()

    # Then
    deleted = ActivityHistory.all_objects.get(id=history.id)
    assert deleted.is_deleted is True
