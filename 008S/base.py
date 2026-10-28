def classify(value):
    if value > 100:
        return "high"
    elif value > 50:
        return "medium"
    else:
        return "low"


def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)
