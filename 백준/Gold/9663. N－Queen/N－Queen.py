N = input()
N = int(N)

pos = [0]*N
flag_row = [False]*N
flag_plus = [False]*((N*2)+1)
flag_minus = [False]*((N*2)+1)
globals()['count'] =0
def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(N):
        if(     not flag_row[j]            # j행에 퀸이 배치 되지 않았다면
            and not flag_plus[i + j]        # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_minus[i - j + N-1]):  # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[i] = j  # 퀸을 j행에 배치
            if i == N-1:  # 모든 열에 퀸을 배치하는 것을 완료
                globals()['count'] += 1
            else:
                flag_row[j] = flag_plus[i + j] = flag_minus[i - j + N-1] = True
                set(i + 1)  # 다음 열에 퀸을 배치
                flag_row[j] = flag_plus[i + j] = flag_minus[i - j + N-1] = False
set(0)
print(globals()['count'])