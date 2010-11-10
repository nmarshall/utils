
def get_val(ky, item):
    '''
    simple function to get a value from the dictionary with a more helpful message than the standard keyerror
    '''
    val = item.get(ky, None)
    if val is None:
        msg = "There was no '%s' key in item %s"
        raise KeyError(msg %(ky, item))
    return val