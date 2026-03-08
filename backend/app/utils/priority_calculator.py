
def calculate_priority(score):
    if score >=10:
        return "Emergency"
    if score >=7:
        return "High"
    if score >=4:
        return "Medium"
    return "Low"
