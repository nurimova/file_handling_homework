def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    f=open(data, 'r')
    read_text=f.read()
    ls=read_text.split('\n')
    for item in ls:
        s.append(len(item))
    return max(s)
print(main('data\data06.txt')) 