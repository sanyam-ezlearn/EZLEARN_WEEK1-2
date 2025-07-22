'''Buddy Strings'''
def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return len(set(s)) < len(s)
    diffs = [(a, b)for a, b in zip(s, goal) if a != b]
    return len(diffs) == 2 and diffs[0] == diffs[1][::-1]

s = "ab"
goal = "ba"

print(buddyStrings(s, goal))