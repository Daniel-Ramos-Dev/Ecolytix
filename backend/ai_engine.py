def generate_insight(value):

    if value < 300:
        return "Air quality is healthy."

    elif value < 450:
        return "Air quality is moderate."

    return "Air pollution detected."