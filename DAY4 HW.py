#모의고사-1
def solution(answers):
    import itertools
    inf_m1=iter(itertools.cycle([1,2,3,4,5]))
    inf_m2=itertools.cycle([2,1,2,3,2,4,2,5])
    inf_m3=itertools.cycle([3,3,1,1,2,2,4,4,5,5])
    scores=[0,0,0]
    print(3)