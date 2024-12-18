import sys
sys.setrecursionlimit(10000000)
data = sys.stdin.readline().rstrip()
# print(data[0:0+3])
ppap = []
result = "NP"
for i in data:
    ppap.append(i)
    if len(ppap) >= 4 and ppap[-4:] == ['P','P','A','P']:
        for _ in range(4):
            ppap.pop()
        ppap.append('P')
if len(ppap) == 1 and ppap[0] == 'P':
    result = "PPAP"
print(result)

# 메모리초과
# def ppap(data):
#     if data == "P":
#         return True
#     for i in range(len(data)):
#         if data[i:i+4] == "PPAP":
#             temp_data = 'P'+data[i+5:-1]
#             # print(temp_data)
#             return ppap(temp_data)        
#     return False
# if ppap(data):
#     print("PPAP")
# else:
#     print("NP")