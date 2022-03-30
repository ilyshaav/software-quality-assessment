from sympy.solvers import solve
from sympy import Symbol

def task1():
    data = [72.1, 90.35, 58.37, 161.36, 39.32,
            27.85, 3.32, 70.92, 29.29, 60.08,
            238.65, 408.75, 7.99, 11.88, 66.55,
            47.22, 56.38, 93.43, 71.37, 10.17,
            67.05, 82.28, 63.03, 29.86, 183.76, 25]
    chance10 = 0
    chance50 = 0
    for i in data:
        if i >= 10:
            chance10 += 1
        if i >= 50:
            chance50 += 1
    chance10 /= len(data)
    chance50 /= len(data)
    return (chance10, chance50)


def task4_1():
    t1, t2, t3 = 10, 20, 25
    mt1, mt2 = 50, 80
    m1, m2, m3 = 1, 1, 1
    e = 2.7
    N = 4 
    Nt = N - (m1 + m2 + m3)
    C = ((m1/(N)) + (m2/(N-m1))+(m3/(N-(m1+m2))))/(t1+t2+t3)
    l = C * (N - (m1+m2+m3))
    R1 = e**(-1*l*mt1)
    R2 = e**(-1*l*mt2)
    return (R1, R2)


def task4_3():
    t1, t2, t3, t4 = 10, 20, 30, 40
    N = 4
    i = 1
    C = (1/t1+t2+t3) / (N+1-(1*10+1*20+1*30) * 1)
    C = (C*C)**1/2
    l1 = C * (N-1+1)
    l2 = C * (N-2+1)
    l3 = C * (N-3+1)
    l4 = C * (N-4+1)
    P1 = l1 * 2.7 ** (l1)
    P2 = l2 * 2.7 ** (l2)
    P3 = l3 * 2.7 ** (l3)
    P4 = l4 * 2.7 ** (l4)
    return (P1, P2, P3, P4)


print("Задание 1")
res_task1 = task1()
print("Вероятность безотказной работы программы через 10 часов:")
print(res_task1[0])
print("Вероятность безотказной работы программы через 50 часов:")
print(res_task1[1])

print("Задание 4.1")
res_task4_1 = task4_1()
print(f"Вероятность безотказной работы программы через 50 часов:")
print(res_task4_1[0])
print(f"Вероятность безотказной работы программы через 80 часов:")
print(res_task4_1[1])

print("Задание 4.3")
res_task4_3 = task4_3()
print("Время нахождения и ликвидации ошибок:")
print("P1")
print(res_task4_3[0])
print("P2")
print(res_task4_3[1])
print("P3")
print(res_task4_3[2])
print("P4")
print(res_task4_3[3])

