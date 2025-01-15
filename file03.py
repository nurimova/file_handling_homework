def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

# Read data from file
    s=[]
    f=open(data,'r')
    read_text=f.read()
    for i in read_text:
        if i.isdigit():
            s.append(i)
    return s
print(main('data\data03.txt'))