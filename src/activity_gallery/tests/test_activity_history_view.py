from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from activity_gallery.models import ActivityHistory


class ActivityHistoryViewSetTest(APITestCase):
    def setUp(self):
        self.history1 = ActivityHistory.objects.create(
            title="History 1",
            content="Content 1",
            activity_date="2024-01-01",
            is_deleted=False,
        )
        self.history2 = ActivityHistory.objects.create(
            title="History 2",
            content="Content 2",
            activity_date="2024-02-01",
            is_deleted=False,
        )
        self.deleted_history = ActivityHistory.objects.create(
            title="Deleted History",
            content="Should not show up.",
            activity_date="2024-03-01",
            is_deleted=True,
        )

    def test_list_activity_history(self):
        url = reverse("activity-history-list")
        response = self.client.get(url, query_params={"page": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn("data", response.data)
        returned_ids = [item["id"] for item in response.data["data"]]
        self.assertIn(self.history1.id, returned_ids)
        self.assertIn(self.history2.id, returned_ids)
        self.assertNotIn(self.deleted_history.id, returned_ids)
