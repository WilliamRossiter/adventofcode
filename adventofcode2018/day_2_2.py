
import fileinput

class PuzzleSolver:

    m_aBoxId = []
    m_boxIdCorrect = ""

    def ProcessFile(self, file):
        with fileinput.input(files=file) as f:
            for line in f:
                self.m_aBoxId.append(line)
        for boxIdA in self.m_aBoxId:
            for boxIdB in self.m_aBoxId:
                if boxIdA is boxIdB:
                    continue
                else:
                    cDiff = 0
                    for a, b in zip(boxIdA, boxIdB):
                        if a != b:
                            cDiff += 1
                    if cDiff == 1:
                        for a, b in zip(boxIdA, boxIdB):
                            if a == b:
                                self.m_boxIdCorrect += a

solver = PuzzleSolver()
solver.ProcessFile("input/day_2_1.txt")
print(solver.m_boxIdCorrect)
