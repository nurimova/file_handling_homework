def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
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
        if i.isalpha():
            s.append(i)
    return s
print(main('data\data04.txt'))