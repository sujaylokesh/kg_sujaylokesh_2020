import sys
def main(s1,s2):
    """#Approach 1
        #counting unique values in s1
        s1 = str(s1).lower()
        li = []
        for i in s1:
            li.append(i)
        set(li)
        if len(li) > len(set(li)):
            print("false")
        else:
            print("true") """
    #approach 2
    s1 = str(s1).lower()
    s2 = str(s1).lower()
    from collections import defaultdict
    df=defaultdict(list)
    for i in range(0,len(s1)):
        df[s1[i]].append(s2[i])
    temp = dict(df)
    for i in temp:
        if len(temp[i]) > 1:
            print("false")
            break
        else:
            print("true")
            break
    return

if __name__ == "__main__":
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    main(s1,s2)
