def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    b=[]
    f=open(data, 'r')   
# Read data from file
    read_text=f.read()
    for i in read_text:
        if i.isdigit():
            a.append(i)
        if i.isalpha():
            b.append(i)
    return [len(a),len(b)]
print(main('data\data05.txt'))