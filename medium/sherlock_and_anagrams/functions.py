def sherlockAndAnagrams(s):
    # Anagram count
    anagrams = 0

    # Change s to array
    s = unwrap(s)

    # We obtain all possible substrings ss from s using a sliding window. 
    ss = getSubstrings(s)

    # DEBUG(ss)

    # For each window size present in ss, we check the strings for anagrams
    for v in ss.values():
        for ssax, ssa in enumerate(v):
            for ssbx, ssb in enumerate(v): 
                if ssax > ssbx:
                    if isAnagram(ssa, ssb):
                        anagrams += 1

    return anagrams


def unwrap(string):
    """Changes string to array."""
    return [c for c in string]


def getSubstrings(s):
    """
    Gets the substrings in s using the sliding window concept.
    """
    substrings = {}

    # Generate the size of the sliding window
    # The window should be of size 1 to len(s)
    for i in range(len(s)):
        window = i + 1

        substrings[window] = []
        
        # Extract the number of substrings obtainable with the given window size
        # If s is of length 5, and window is size 1, we can have 5.
        # Similarly, 5, 2 => 4.
        #   5, 3 => 3
        # Thus, n, m => n - m + 1
        for j in range(len(s) - window + 1):
            # Group the strings by window size, as anagrams cannot be of different lengths
            substrings[window].append((s[j: j + window]))

    return substrings


def isAnagram(s1, s2):
    """
    Checks if s1 and s2 are anagrams by counting the number of occurrences of each letter in s1 and s2.
    """
    set1 = set(s1)
    set2 = set(s2)

    if set1 == set2:
        for char in set1:
            if s1.count(char) != s2.count(char):
                return False
    else: 
        return False

    return True


def DEBUG(*args, **kwargs):
    print(*args, **kwargs)