history = []

def generate_insight(value):

    history.append(value)

    if len(history) > 10:
        history.pop(0)

    if len(history) < 3:
        return "Collecting environmental data..."

    old_avg = sum(history[:3]) / 3
    recent_avg = sum(history[-3:]) / 3

    if recent_avg > old_avg + 30:
        return "Pollution trend worsening detected."

    elif recent_avg < old_avg - 30:
        return "Air quality improving trend detected."

    return "Environmental conditions stable."