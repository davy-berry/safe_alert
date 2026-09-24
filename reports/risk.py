from .models import Category


def calculate_risk_score(category):
    return category.risk_weight


def calculate_priority(risk_score):
    if risk_score < 30:
        return "low"

    if risk_score < 60:
        return "medium"

    if risk_score < 80:
        return "high"

    return "critical"
