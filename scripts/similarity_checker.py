def is_similar_problem(new_problem, previous_problems):

    new_title = new_problem["title"].lower()
    new_signature = set(new_problem["signature"])

    for old in previous_problems:

        old_title = old["title"].lower()
        old_signature = set(old["signature"])

        # Same title
        if new_title == old_title:
            return True

        # Signature overlap
        overlap = len(new_signature & old_signature)

        if overlap >= 2:
            return True

    return False