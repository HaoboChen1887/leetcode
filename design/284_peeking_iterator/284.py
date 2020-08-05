class PeekingIterator:
    # to implement peek, we need to store the next value (effectively the current value)
    # we reset _next everytime next get called, if iterator hasNext(), then _next gets updated
    # the internal hasNext() only need to check whether _next is None
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._next = iterator.next()
        self._iterator = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        

    def next(self):
        """
        :rtype: int
        """
        if not self._next:
            raise StopIteration()
        res = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None