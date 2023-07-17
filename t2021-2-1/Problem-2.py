a=int(input("Enter the range "))
list_of_series=[]
def OddSeries(a):
    for i in range(1,a+1):
        list_of_series.append(i*2-1)
    print(list_of_series)
OddSeries(a)
def generate_series(x):
    series = []
    num = 1

    while num <= x:
        series.append(num)
        num += 2

    return series
    
# example
x = int(input())
result = generate_series(x)
print(result)