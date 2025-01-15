def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    f=open(data,'r')
    read_text=f.read()
    return len(read_text)
print(main('data\data02.txt'))