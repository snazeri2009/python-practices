from abc import ABC, abstractclassmethod


class InValidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.is_open = False

    def open(self):
        if self.is_open:
            raise InValidOperationError("stream is already open")
        self.is_open = True

    def close(self):
        if not self.is_open:
            raise InValidOperationError("stream is already closed")
        self.is_open = False

    @abstractclassmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from a file...")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network...")


myFileStream = FileStream()
print(isinstance(myFileStream, Stream))
myFileStream.open()
myFileStream.read()
myFileStream.close()


myNetworkStream = NetworkStream()
print(isinstance(myNetworkStream, Stream))
myNetworkStream.open()
myNetworkStream.read()
myNetworkStream.close()
