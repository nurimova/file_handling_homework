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
    ls=read.split('\n')
    for num in ls:
        ls1=num.split(' ')
        last_item = ls1[-1]
        point = last_item.count('.')
        if point==2:
            n=last_item[0:-2]
            s.append(float(n))
        else:
            s.append(float(ls1[1]))

    return min(s)
print(main('data\data08.txt'))