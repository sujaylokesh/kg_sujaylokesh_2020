import sys
def main(s1,s2):
    #Approach 1
    #counting unique values in s1
    s1 = str(s1).lower()
    li = []
    for i in s1:
        li.append(i)
    set(li)
    if len(li) > len(set(li)):
        print("false")
    else:
        print("true")
    return

if __name__ == "__main__":
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    main(s1,s2)
