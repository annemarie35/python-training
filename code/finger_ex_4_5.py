# Use find to implement a function satisfying the specification.

def find_last(s, sub):
    """s and sub are non-empty strings
       Returns the index of the last occurrence of sub in s.
       Returns None if sub does not occur in s"""
    if s.find(sub) == -1 or s == '' or sub == '':
        return None

    occurrence_index = s.find(sub)

    while occurrence_index != -1:
        next_pos = s.find(sub, occurrence_index + 1)
        if next_pos == -1:
            break
        occurrence_index = next_pos

    return occurrence_index


find_last('hello world hello', 'world')