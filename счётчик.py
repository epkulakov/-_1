import asyncio

async def dobl_1(i):
    global x
    for i in range(i):
         x+=1
    return x
async def dobl_2(i):
    global x
    for i in range(i):
        x += 1
    return x

x = 0
i = int(input('До скольки надо повысить счётчик:'))
i = i//2
asyncio.run(dobl_1(i))
asyncio.run(dobl_2(i))
i = i*2
if i == x:
    print(f"Переменая равняется = {x}")