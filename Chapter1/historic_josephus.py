__author__ = 'zephaniahgrunschlag'

'''
According to legend (and p. 8 of "Concrete Math") Josephus and a co-conspirator survived
a 41 member suicide circle in which each person killed not his next in line, but the one
after.

Where did Josephus and his friend stand in order to survive?
'''

import io
from util.zio import RedirectStdout

class HistoricJosephus:

    def __init__(self, N):
        self.N = N
        self.alive = [n for n in range(1, N+1)]
        self.sword_idx = 0

    def kill_next(self):
        killer = self.alive[self.sword_idx]
        num_alive = len(self.alive)
        victim_idx = (self.sword_idx + 2) % num_alive
        victim = self.alive[victim_idx]
        print("survivors:", self.alive)
        print("%d alive\n %d at idx %d --slays--> %d at idx %d" % (num_alive, killer, self.sword_idx, victim, victim_idx))
        del self.alive[victim_idx]
        self.sword_idx = victim_idx % (num_alive-1)

    def run(self):
        if len(self.alive) == 1:
            return 1
        while len(self.alive) > 2:
            self.kill_next()
        print("LAST MEN STANDING: %d and %d" % (self.alive[0], self.alive[1]))
        print("HOLDER OF SWORD: %s" % self.alive[self.sword_idx])
        survivor = self.alive[1-self.sword_idx]
        print("SURVIVOR AFTER SUICIDE: %d" % survivor)
        return survivor

if __name__ == "__main__":
    j = HistoricJosephus(41)
    out = io.StringIO()
    with RedirectStdout(out):
        j.run()

    results = []
    N = 100
    with RedirectStdout(out):
        for n in range(1, N+1):
            j = HistoricJosephus(n)
            results.append(j.run())

    format_str = "%s\t|\t%s"
    print(format_str % ("n", "J(n)"))
    print(format_str % ("-----", "-----"))
    for n in range(1, N+1):
        print(format_str % (n, results[n-1]))



