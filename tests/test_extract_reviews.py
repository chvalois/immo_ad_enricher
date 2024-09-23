from ..utils import extract_reviews

def test_extract_reviews_all_present():
    # Test case where all reviews are present
    text = (
        "Proche des commerces : 8/10\n"
        "Environs calmes et sans nuisance sonore : 9/10\n"
        "Proche de la nature : 7/10\n"
        "Modernité du bien : 6/10\n"
        "Luminosité du bien : 9/10\n"
        "Taille du bien : 10/10\n"
        "Bonus du bien (comme piscine, terrasse, dépendance) : 5/10"
    )

    expected_reviews = {
        'review_proche_comm': 8,
        'review_calme': 9,
        'review_proche_nature': 7,
        'review_moderne': 6,
        'review_luminosite': 9,
        'review_taille': 10,
        'review_bonus': 5,
    }

    reviews = extract_reviews(text, 'FR')

    assert reviews == expected_reviews


def test_extract_reviews_some_missing():
    # Test case where some reviews are missing
    text = (
        "Proche des commerces : 8/10\n"
        "Proche de la nature : 7/10\n"
        "Modernité du bien : 6/10\n"
        "Bonus du bien (comme piscine, terrasse, dépendance) : 5/10"
    )

    expected_reviews = {
        'review_proche_comm': 8,
        'review_proche_nature': 7,
        'review_moderne': 6,
        'review_bonus': 5,
    }

    reviews = extract_reviews(text, 'FR')

    # Check that only the present reviews are extracted
    assert reviews == expected_reviews


def test_extract_reviews_none_present():
    # Test case where no reviews are present
    text = "This text contains no ratings at all."

    expected_reviews = {}

    reviews = extract_reviews(text, 'FR')

    # No reviews should be extracted
    assert reviews == expected_reviews


def test_extract_reviews_invalid_format():
    # Test case where the review format is incorrect
    text = (
        "Proche des commerces : N/A\n"
        "Environs calmes et sans nuisance sonore : 9 points\n"
        "Proche de la nature : 7/5\n"
    )

    expected_reviews = {
    }

    reviews = extract_reviews(text, 'FR')

    # Only the valid review should be extracted
    assert reviews == expected_reviews