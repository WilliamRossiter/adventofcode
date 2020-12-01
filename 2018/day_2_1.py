
import fileinput

class PuzzleSolver:

    m_cTwice = 0
    m_cThrice = 0

    def ProcessLine(self, line):
        dict = { }
        for c in line:
            if not dict.get(c):
                dict[c] = 1
            else:
                dict[c] += 1
        for n in dict.values():
            if n == 2:
                self.m_cTwice += 1
                break
        for n in dict.values():
            if n == 3:
                self.m_cThrice += 1

    def ProcessFile(self, file):
        with fileinput.input(files=file) as f:
            for line in f:
                self.ProcessLine(line)
        print("%d" % (self.m_cTwice * self.m_cThrice))

solver = PuzzleSolver()
solver.ProcessFile("input/day_2_1.txt")
