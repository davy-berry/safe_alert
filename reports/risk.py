from .models import Category


def calculate_risk_score(category):
    """Return the risk score for a category based on its configured weight."""
    return category.risk_weight


def calculate_priority(risk_score):
    """Map a numeric risk score to the matching urgency priority label."""
    if risk_score < 30:
        return "low"

    if risk_score < 60:
        return "medium"

    if risk_score < 80:
        return "high"

    return "critical"
