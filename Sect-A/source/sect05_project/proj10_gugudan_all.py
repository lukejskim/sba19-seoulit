# 구구단 전체 출력

for m in range(2, 10):
    print('%s \n\t[%d 단 출 력]' % ('='*20, m))
    for n in range(1, 10):
        print('\t {} x {} = {}'.format(m, n, m*n))

