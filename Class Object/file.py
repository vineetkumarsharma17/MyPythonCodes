def group_by_owners(files):
    lis=[]
    for i in files:
        lis.append(files[i])
    lis=list(set(lis))
    a={}
    b=[]
    for i in lis:
        b=[]
        for j in files:
            if(i==files[j]):
                b.append(j)
        a[i]=b

    return a

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))