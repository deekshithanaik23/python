start=3
end=5
result1=""
for j in range(start,end+1,1):
    part1=str(j)
    part2=".txt"
    fname=part1+part2
    for i in range(1,11,1):
        print(j,i,j*i)
    print()
