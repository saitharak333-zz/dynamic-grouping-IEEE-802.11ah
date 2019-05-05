# import time
# from time import sleep
#
# def delay_func(st,val):
#     if time.time() - st > val:
#         pass
#
# val = 500
# channel = 0
# bc = 15
# st = time.time()
# delay_func(st,val)
# i = [0 for i in range(1000)]
# if channel == 0:
#     bc -= 1
# # sleep(0.0000001)
# # sleep(250.07 * (10**(-6)))
# en = time.time()
# print(en - st)

while True:
    a = 4
    while a > 2:
        a -= 1
        print(a)
    else:
        # pass
        check_fun(a)



def check_fun(a):
    if a == 2:
        break
