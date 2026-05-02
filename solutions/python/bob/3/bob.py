"""Function determining what Bob will reply to a given set of strings"""

def response(hey_bob):
    """Determine what Bob will reply."""
    hey_bob = hey_bob.strip()
    if len(hey_bob) != 0 and hey_bob[-1] =='?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return 'Sure.'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    if len(hey_bob) == 0 :
        return 'Fine. Be that way!'
    return 'Whatever.'