def count_words(filepath, words_list):
    """
    returns the number of words in a file


    Parameters
    ----------
    filepath : string, The path of the file.

    words_list : list, The list of words to count

    Returns
    -------
    Int
        The number of words in the file

    """

    # Open the text file
    with open(filepath) as file:
        text = file.read()
    # Count number of times these words appear
    n = 0
    for word in text.split():
        if word.lower() in words_list:
            n += 1
    return n
