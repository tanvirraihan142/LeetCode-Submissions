class FrequencyTracker:
    def __init__(self):
        self.data = collections.defaultdict(int)
        self.freq = collections.defaultdict(set)

    def add(self, number):
        self.data[number] += 1
        v = self.data[number]
        if v > 1:
            self.freq[v-1].remove(number)
        self.freq[v].add(number)

    def deleteOne(self, number):
        if self.data[number] > 0:
            self.data[number] -= 1
            v = self.data[number]
            if v > -1:
                self.freq[v+1].remove(number)
            self.freq[v].add(number)

    def hasFrequency(self, frequency):
        if frequency not in self.freq:
            return False
        return len(self.freq[frequency]) > 0