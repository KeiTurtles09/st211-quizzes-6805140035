def letterGrade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    elif score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'F'
