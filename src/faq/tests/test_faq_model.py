import pytest
from django.db.utils import DatabaseError

from faq.models import FAQ


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer",
    [
        ("What is Python?", "Python is a versatile programming language."),
        ("What is pytest?", "pytest is a testing framework for Python."),
        ("What is Django?", "Django is a high-level Python web framework."),
    ],
)
def test_create_faq_success_given_valid_data(question: str, answer: str) -> None:
    # Given
    faq_data: dict[str, str] = {"question": question, "answer": answer}

    # When
    faq = FAQ.objects.create(**faq_data)

    # Then
    assert faq.question == faq_data.get("question")
    assert faq.answer == faq_data.get("answer")


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer",
    [
        (None, "Python is a versatile programming language."),
        ("What is pytest?", None),
        (None, None),
    ],
)
def test_create_faq_fail_given_invalid_data(question: str | None, answer: str | None) -> None:
    # Given
    faq_data: dict[str, str | None] = {"question": question, "answer": answer}

    # Then
    with pytest.raises(DatabaseError):
        # When
        FAQ.objects.create(**faq_data)


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer",
    [
        ("What is Python?", "Python is a versatile programming language."),
        ("What is pytest?", "pytest is a testing framework for Python."),
        ("What is Django?", "Django is a high-level Python web framework."),
    ],
)
def test_read_faq_given_exist_faq_id(question: str, answer: str) -> None:
    # Given
    faq_data: dict[str, str] = {"question": question, "answer": answer}
    faq = FAQ.objects.create(**faq_data)

    # When
    fetched = FAQ.objects.get(id=faq.id)

    # Then
    assert fetched.question == faq_data.get("question")
    assert fetched.answer == faq_data.get("answer")


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "faq_id",
    [-1, 0],
)
def test_read_faq_given_non_exist_faq_id(faq_id: int) -> None:
    # Given
    # When
    with pytest.raises(FAQ.DoesNotExist):
        # Then
        FAQ.objects.get(id=faq_id)


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, updated_question, updated_answer",
    [
        (
            "What is Python?",
            "Python is a versatile programming language.",
            "What is Python?",
            "Python is a versatile programming language.",
        ),
        (
            "What is pytest?",
            "pytest is a testing framework for Python.",
            "What is pytest?",
            "pytest is a testing framework for Python.",
        ),
        (
            "What is Django?",
            "Django is a high-level Python web framework.",
            "What is Django?",
            "Django is a high-level Python web framework.",
        ),
    ],
)
def test_update_faq_success_given_valid_data(
    question: str,
    answer: str,
    updated_question: str,
    updated_answer: str,
) -> None:
    # Given
    faq_data: dict[str, str] = {"question": question, "answer": answer}
    faq = FAQ.objects.create(**faq_data)

    faq.question = updated_question
    faq.answer = updated_answer
    faq.save()

    updated = FAQ.objects.get(id=faq.id)
    assert updated.question == updated_question
    assert updated.answer == updated_answer


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, updated_question, updated_answer",
    [
        (
            "What is Python?",
            "Python is a versatile programming language.",
            None,
            "Python is a versatile programming language.",
        ),
        (
            "What is pytest?",
            "pytest is a testing framework for Python.",
            "What is pytest?",
            None,
        ),
        (
            "What is Django?",
            "Django is a high-level Python web framework.",
            None,
            None,
        ),
    ],
)
def test_update_faq_fail_given_invalid_data(
    question: str,
    answer: str,
    updated_question: str | None,
    updated_answer: str | None,
) -> None:
    # Given
    faq_data: dict[str, str] = {"question": question, "answer": answer}
    faq = FAQ.objects.create(**faq_data)

    # When
    faq.question = updated_question
    faq.answer = updated_answer

    # Then
    with pytest.raises(DatabaseError):
        faq.save()


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted",
    [
        ("What is Python?", "Python is a versatile programming language.", False),
        ("What is pytest?", "pytest is a testing framework for Python.", False),
        ("What is Django?", "Django is a high-level Python web framework.", False),
    ],
)
def test_delete_faq_when_soft_delete_operation(
    question: str, answer: str, is_deleted: bool
) -> None:
    # Given
    faq_data: dict[str, object] = {
        "question": question,
        "answer": answer,
        "is_deleted": is_deleted,
    }
    faq = FAQ.objects.create(**faq_data)
    faq_id = faq.id

    # When
    faq.delete()

    # Then
    deleted = FAQ.objects.get(id=faq_id)
    assert deleted.is_deleted is True


@pytest.mark.django_db
@pytest.mark.feature
@pytest.mark.parametrize(
    "question, answer, is_deleted",
    [
        ("What is Python?", "Python is a versatile programming language.", True),
        ("What is pytest?", "pytest is a testing framework for Python.", True),
        ("What is Django?", "Django is a high-level Python web framework.", True),
    ],
)
def test_delete_faq_when_hard_delete_operation(
    question: str, answer: str, is_deleted: bool
) -> None:
    # Given
    faq_data: dict[str, str | bool] = {
        "question": question,
        "answer": answer,
        "is_deleted": is_deleted,
    }
    faq = FAQ.objects.create(**faq_data)
    faq_id = faq.id

    # When
    faq.delete(force_delete=True)

    # Then
    with pytest.raises(FAQ.DoesNotExist):
        FAQ.objects.get(id=faq_id)
