def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    s=[]
    f=open(data)
    read=f.read()
    for num in read:
        if num.isdigit():
            s.append(num)    
    return min(s)
print(main('data\data08.txt'))