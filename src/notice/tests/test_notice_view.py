import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from notice.models import Notice

pytestmark = pytest.mark.django_db


@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def notices() -> list[Notice]:
    notice1 = Notice.objects.create(
        title="Important Update",
        content="This is an important update.",
        is_pinned=True,
        is_deleted=False,
    )
    notice2 = Notice.objects.create(
        title="Maintenance Notice",
        content="Scheduled maintenance at midnight.",
        is_pinned=False,
        is_deleted=False,
    )
    return [notice1, notice2]


@pytest.fixture
def deleted_notices() -> list[Notice]:
    notice1 = Notice.objects.create(
        title="Important Update",
        content="This is an important update.",
        is_pinned=True,
        is_deleted=True,
    )
    return [notice1]


def test_list_notice_only_is_pinned_is_true(client: APIClient, notices: list[Notice]) -> None:
    # Given
    is_pinned_notice_count = 1
    url = reverse("notice-list")

    # When
    response = client.get(url, {"page": 1, "is_pinned": True})

    # Then
    assert response.status_code == status.HTTP_200_OK

    data = response.data["data"]

    assert len(data) == is_pinned_notice_count
    assert all(item["is_pinned"] for item in data)


def test_list_notice_only_is_pinned_is_false(client: APIClient, notices: list[Notice]) -> None:
    """
    Test that in the notice list:
        - Only notices that are pinned have 'is_pinned' set to True.
        - Pinned notices appear before unpinned ones.
    """
    is_pinned_notice_count = 1
    url = reverse("notice-list")
    response = client.get(url, {"page": 1, "is_pinned": False})
    assert response.status_code == status.HTTP_200_OK

    data = response.data["data"]

    # Verify that pinned notices appear first.
    assert len(data) == is_pinned_notice_count
    assert all(not item["is_pinned"] for item in data)


def test_list_notice(client: APIClient, notices: list[Notice]) -> None:
    url = reverse("notice-list")
    response = client.get(url, {"page": 1})
    assert response.status_code == status.HTTP_200_OK

    assert len(response.data["data"]) == len(notices)


def test_retrieve_notice(client: APIClient, notices: list[Notice]) -> None:
    for notice in notices:
        url = reverse("notice-detail", args=[notice.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["data"].get("id") == notice.id
        assert response.data["data"].get("title") == notice.title


def test_retrieve_non_existent_notice(client: APIClient) -> None:
    url = reverse("notice-detail", args=[0])  # A non-existent ID
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["status"] == "ERROR"
    assert "error" in response.data
    assert response.data["error"]["code"] == "not_found"


def test_retrieve_deleted_notice(client: APIClient, deleted_notices: list[Notice]) -> None:
    for deleted_notice in deleted_notices:
        url = reverse("notice-detail", args=[deleted_notice.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["status"] == "ERROR"
        assert "error" in response.data
        assert response.data["error"]["code"] == "not_found"
