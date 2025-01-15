def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    f=open(data)
    read=f.read()
    for num in read:
        if num.isdigit():
            s.append(num)    
    return max(s)
print(main('data\data08.txt'))
# Read data from file