from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from faq.models import FAQ


class FAQViewSetTest(APITestCase):
    def setUp(self):
        # Create FAQs for testing
        self.faq1 = FAQ.objects.create(
            question="What is Python?", answer="A programming language.", is_deleted=False
        )
        self.faq2 = FAQ.objects.create(
            question="What is DRF?", answer="Django Rest Framework.", is_deleted=False
        )
        # This FAQ is marked as deleted and should not appear in queries
        self.deleted_faq = FAQ.objects.create(
            question="Deleted FAQ", answer="Should not show up.", is_deleted=True
        )

    def test_list_faq(self):
        url = reverse("faq-list")  # Assumes your router has registered viewset with basename 'faq'
        response = self.client.get(url, query_params={"page": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Validate that only non-deleted FAQs are returned
        self.assertIn("data", response.data)
        returned_ids = [item["id"] for item in response.data["data"]]
        self.assertIn(self.faq1.id, returned_ids)
        self.assertIn(self.faq2.id, returned_ids)
        self.assertNotIn(self.deleted_faq.id, returned_ids)

    def test_retrieve_faq(self):
        url = reverse("faq-detail", args=[self.faq1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"].get("id"), self.faq1.id)
        self.assertEqual(response.data["data"].get("question"), self.faq1.question)

    def test_retrieve_non_existent_faq(self):
        url = reverse("faq-detail", args=[0])  # A non-existent ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("ERROR", response.data["status"])
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"]["code"], "not_found")

    def test_retrieve_deleted_faq(self):
        # Attempt to retrieve a FAQ that has been marked as deleted
        url = reverse("faq-detail", args=[self.deleted_faq.id])
        response = self.client.get(url)
        # Expect error response for deleted faq
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("ERROR", response.data["status"])
        self.assertIn("error", response.data)
        self.assertEqual(response.data["error"]["code"], "not_found")
