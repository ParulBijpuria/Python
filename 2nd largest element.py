if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x = y = arr[0]
    for i in range(1,n):
        if(arr[i]>x and arr[i]>y):
            y=x
            x=arr[i]
        elif(arr[i]>y and arr[i]<x):
            y=arr[i]
        elif x==y:
            y=arr[i]
    print y
