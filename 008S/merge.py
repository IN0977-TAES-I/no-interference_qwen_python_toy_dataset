def classify(value):
    if value > 100:
        return "very high"
    elif value > 50:
        return "medium"
    else:
        return "very low"


def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)
