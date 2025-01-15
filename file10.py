def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    f=open(data)
    read=f.read()
    for row in read:
        l=read.split(\n)
        s.append(len(l))
    return max(s)
# Read data from file