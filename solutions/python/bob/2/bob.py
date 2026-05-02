"""Function determining what Bob will reply to a given set of strings"""

def response(hey_bob):
    """Determine what Bob will reply."""
    if len(hey_bob.strip()) != 0 and hey_bob.strip()[-1] =='?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return 'Sure.'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    if len(hey_bob) == 0 or hey_bob.isspace():
        return 'Fine. Be that way!'
    return 'Whatever.'