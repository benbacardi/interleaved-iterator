class UsedValue(object):
    pass

class SelectiveIterable(object):

    def __init__(self, iterables, key):
        self.iterables = [(i, UsedValue()) for i in iterables]
        self.key = key

    def _repopulate_latest(self):

        iterables = []
        for iterable, latest in self.iterables:
            if isinstance(latest, UsedValue):
                try:
                    latest = iterable.next()
                except StopIteration:
                    continue
            iterables.append((iterable, latest))
        if not len(iterables):
            raise StopIteration
        self.iterables = iterables

    def __iter__(self):
        return self

    def next(self):
        self._repopulate_latest()
        index, (iterable, result) = sorted(enumerate(self.iterables), key=lambda x: self.key(x[1][1]))[0]
        self.iterables[index] = (self.iterables[index][0], UsedValue())
        return result
