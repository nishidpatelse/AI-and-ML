from smart_study_assistant.recommendation import get_recommendations

def test_get_recommendations():
    recs = get_recommendations("student123", "math101")
    assert isinstance(recs, list)
    assert len(recs) > 0
