
def realtype(sentence, wpm=80):
    """Function to get time based on how any words inputted in respect to the WPM param
    :arg : str, int
    :return : str
    """

    return (wpm/60) * len(str(sentence).split(sep=' '))

