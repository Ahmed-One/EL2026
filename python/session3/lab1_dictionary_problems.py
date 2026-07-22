"""Dictionary Problems - Testing student capability with dictionary operations."""


def dictionary_operations(dict1: dict, dict2: dict):
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    s1_keys = set(dict1.keys())
    s2_keys = set(dict2.keys())
    # common_keys = {key for key in dict1 if key in dict2.keys()}
    common_keys = s1_keys.intersection(s2_keys)
    # unique_keys = {key for key in dict1 if not key in dict2.keys()}
    # unique_keys.add({key for key in dict2 if not key in dict1.keys()})
    unique_keys = set.union(s1_keys.difference(s2_keys), s2_keys.difference(s1_keys))
    dict1.update({key: dict2[key] for key in dict2.keys()})
    return {"merged": dict1, "common_keys": common_keys, "unique_keys": unique_keys}


def count_word_frequency(text: str):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    return {word: text.count(word) for word in text.split(" ")}


def dictionary_filtering(students_grades: dict):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    stgrad = students_grades
    return {name: stgrad[name] for name in stgrad.keys() if stgrad[name] >= 70}


def nested_dictionary_access(nested_dict: dict, keys_path: list):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    return_value = None
    ndict = nested_dict
    for key in keys_path:
        if key in ndict.keys():
            if isinstance(ndict[key], dict):
                ndict = ndict[key]
            else:
                return_value = ndict[key]
    return return_value


if __name__ == "__main__":
    # Test cases
    print("Testing dictionary_operations...")
    result = dictionary_operations({"a": 1, "b": 2}, {"b": 3, "c": 4})
    expected = {"merged": {"a": 1, "b": 3, "c": 4}, "common_keys": {"b"}, "unique_keys": {"a", "c"}}
    assert result == expected, f"Expected {expected}, got {result}"
    assert result["merged"] == {"a": 1, "b": 3, "c": 4}, "Merged dictionary incorrect"
    assert result["common_keys"] == {"b"}, "Common keys incorrect"
    assert result["unique_keys"] == {"a", "c"}, "Unique keys incorrect"

    print("Testing count_word_frequency...")
    result = count_word_frequency("hello world hello python world")
    expected = {"hello": 2, "world": 2, "python": 1}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing dictionary_filtering...")
    result = dictionary_filtering({"Alice": 85, "Bob": 65, "Charlie": 90, "Diana": 45})
    expected = {"Alice": 85, "Charlie": 90}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing nested_dictionary_access...")
    nested = {"level1": {"level2": {"level3": "found"}}}
    result = nested_dictionary_access(nested, ["level1", "level2", "level3"])
    assert result == "found", f"Expected 'found', got {result}"

    result = nested_dictionary_access(nested, ["level1", "nonexistent"])
    assert result is None, f"Expected None, got {result}"

    print("All tests passed!")
