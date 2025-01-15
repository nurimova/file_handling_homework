def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data, 'r')
    read_text=f.read()
    return read_text.split(',')
print(main('data\data01.txt'))

       
     