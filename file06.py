def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
    s=[]
    f=open(data, 'r')
    read_text=f.read()
    for row in read_text:
        row.split(\\n)
        s.append(len(row))
    return s 
print(main('data\data06.txt')) 