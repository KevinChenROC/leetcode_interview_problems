import queue
from threading import Lock


class Foo(object):
    def __init__(self):
        self.lock = Lock()
        self.q = queue.Queue()
        n = 3
        self.printed = [False] * (n)
        for i in range(n):
            self.q.put(i)

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() output "first". Do not change or remove this line.
        idx = self.q.get()
        if idx == 0:
            with self.lock:
                self.printed[idx] = True
                printFirst()
                return

        self.q.put(idx)
        self.first(printFirst)

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() output "second". Do not change or remove this line.

        idx = self.q.get()
        if idx == 1:
            # need a lock because printed is shared.
            with self.lock:
                if self.printed[idx - 1]:
                    printSecond()
                    self.printed[idx] = True
                    return

        self.q.put(idx)
        self.second(printSecond)

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        idx = self.q.get()
        if idx == 2:
            with self.lock:
                if self.printed[idx - 1]:
                    printThird()
                    self.printed[idx] = True
                    return

        self.q.put(idx)
        self.third(printThird)


# Input
# [1,2,3]
# [1,3,2]
# [3,1,2]
# Outputs
# "firstsecondthird"
# "firstsecondthird"
# "firstsecondthird"
