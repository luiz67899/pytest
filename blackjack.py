def card_score(cards):
    numbers = [c for c in cards if c in "23456789"]
    faces = [c for c in cards if c in 'JQK']
    n_aces = sum([1 for c in cards if c == "A"])
    score = sum([int(i) for i in numbers]) + len(faces) * 10
    while (score + n_aces * 11) > 21 :
        score += 1
        n_aces -= 1
    return score if score < 21 else 0 

