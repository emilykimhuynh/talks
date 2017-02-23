def has_duplicates(string):
    
    # because there are only 128 standard ASCII characters
    if len(string) > 128:
        return True
    
    # we use a set instead of a dictionary since we don't need
    # to count any values
    chars = set()
    
    # iterate over the input string
    for c in string:
        if c not in chars:
            chars.add(c)
        else:
            return True

    # if we've made it here, then there are no duplicate chars
    return False

print has_duplicates("abc123")
print has_duplicates("abc12a3")
