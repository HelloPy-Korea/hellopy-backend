import pytest
from rest_framework.exceptions import ValidationError

from faq.models import FAQ
from faq.serializers import FAQSerializer


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted",
    [
        ("Question 1", "The best way to learn Python is to practice coding every day.", False),
        ("What is the best way to learn Python?", "Answer1", False),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
        ),
    ],
)
def test_faq_serializer_is_valid_true_given_valid_data(question, answer, is_deleted):
    # Given
    valid_data = {
        "question": question,
        "answer": answer,
        "is_deleted": is_deleted,
    }

    # When
    serializer = FAQSerializer(data=valid_data)
    is_valid = serializer.is_valid()

    # Then
    assert is_valid is True
    assert serializer.errors == {}
    assert serializer.validated_data == valid_data


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted",
    [
        (None, "The best way to learn Python is to practice coding every day.", False),
        ("What is the best way to learn Python?", None, False),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            None,
        ),
    ],
)
def test_faq_serializer_is_valid_false_given_invalid_data(question, answer, is_deleted):
    # Given
    invalid_data = {
        "question": question,
        "answer": answer,
        "is_deleted": is_deleted,
    }

    # When
    serializer = FAQSerializer(data=invalid_data)
    is_valid = serializer.is_valid()

    # Then
    assert is_valid is False
    assert serializer.errors != {}
    assert serializer.validated_data == {}


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted",
    [
        ("Question 1", "The best way to learn Python is to practice coding every day.", False),
        ("What is the best way to learn Python?", "Answer1", False),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
        ),
    ],
)
def test_faq_serializer_create_success_given_valid_data(question, answer, is_deleted):
    # Given
    valid_data = {
        "question": question,
        "answer": answer,
        "is_deleted": is_deleted,
    }
    serializer = FAQSerializer(data=valid_data)

    assert serializer.is_valid()

    # When
    faq = serializer.save()

    # Then
    assert FAQ.objects.count() > 0
    assert faq.question == question
    assert faq.answer == answer
    assert faq.is_deleted == is_deleted


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted, updated_question, updated_answer, updated_is_deleted",
    [
        (
            "Question 1",
            "The best way to learn Python is to practice coding every day.",
            False,
            "Updated Question 1",
            "Updated Answer 1",
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
def test_faq_serializer_update_success_given_valid_data(
    question, answer, is_deleted, updated_question, updated_answer, updated_is_deleted
):
    # Given
    valid_data = {"question": question, "answer": answer, "is_deleted": is_deleted}
    update_data = {
        "question": updated_question,
        "answer": updated_answer,
        "is_deleted": updated_is_deleted,
    }
    faq = FAQ.objects.create(**valid_data)
    serializer = FAQSerializer(faq, data=update_data)
    assert serializer.is_valid()

    # When
    faq = serializer.save()

    # Then
    assert faq.question == updated_question
    assert faq.answer == updated_answer
    assert faq.is_deleted == updated_is_deleted


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted, updated_question, updated_answer, updated_is_deleted",
    [
        (
            "Question 1",
            "The best way to learn Python is to practice coding every day.",
            False,
            "Invalid Update Question 1",
            None,
            None,
        ),
        (
            "What is the best way to learn Python?",
            "Answer1",
            False,
            None,
            "Invalid Updated Answer 1",
            False,
        ),
        (
            "What is the best way to learn Python?",
            "The best way to learn Python is to practice coding every day.",
            True,
            None,
            None,
            "Invalid Updated Is Deleted",
        ),
    ],
)
def test_faq_serializer_update_failure_given_invalid_data(
    question, answer, is_deleted, updated_question, updated_answer, updated_is_deleted
):
    # Given
    valid_data = {"question": question, "answer": answer, "is_deleted": is_deleted}
    update_data = {
        "question": updated_question,
        "answer": updated_answer,
        "is_deleted": updated_is_deleted,
    }
    faq = FAQ.objects.create(**valid_data)
    serializer = FAQSerializer(faq, data=update_data)

    # Then
    with pytest.raises(ValidationError):
        # When
        serializer.is_valid(raise_exception=True)
