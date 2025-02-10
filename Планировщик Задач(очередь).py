import heapq
import time
pq = []
name = ["Помыть посуду", "Сделать дз", "Отдохнуть", "Пойти погулять с собакой", "Пойти на тренеровку"]
duration = [2, 4, 2, 1.5, 6]
pr = [3, 1, 4, 2, 0]
for i in range(len(name)):
   heapq.heappush(pq, (pr[i], name[i]))
for i in range(len(name)):
   f = pr.index(min(pr))
   u = int(input(f"Реализовавать задачу {name[f]} 1 - да     2 - нет"))
   pr[f] = 10000000000
   if u == 1:
      f = duration[f]
      y = heapq.heappop(pq)
      for i in range(len(pq)):
          print(f"Pending{pq[i]}")
      print(f"In Progress {y}")
      time.sleep(f)
      print(f"Completed {y}")
      print("\n")