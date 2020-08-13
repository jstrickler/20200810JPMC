
class TrimmedFile:

    def __init__(self, file_name):
        self.file_in = open(file_name)

    def __next__(self):
        line = self.file_in.readline()
        if line == '':
            raise StopIteration
        else:
            return line.strip('\n\r')

    def __iter__(self):
        return self

tf = TrimmedFile('DATA/mary.txt')
for line in tf:
    print(line)
