CppBetterThanPython = []
while True:
    a = int(input())
    if a == 0: 
        break
    else: CppBetterThanPython.append(a)
PythonIsHard = []
while len(CppBetterThanPython) > 0:
    if len(CppBetterThanPython) == 1:
        PythonIsHard.append(CppBetterThanPython[0])
        CppBetterThanPython.pop()
        break
    sum = CppBetterThanPython[0] + CppBetterThanPython[-1]
    PythonIsHard.append(sum)
    CppBetterThanPython.pop(0)
    CppBetterThanPython.pop(-1)
print(*PythonIsHard)