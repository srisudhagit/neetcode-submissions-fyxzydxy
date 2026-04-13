class TimeMap:

    def __init__(self):
        self.keyStore = {} # key is key value is (value,timestamp) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        reqValues = self.keyStore.get(key,[])
        l, r = 0, len(reqValues)-1
        res = ""
        if not reqValues:
            return ""

        while l <= r:
            m = (l + r) //2

            if reqValues[m] and reqValues[m][1] <= timestamp:
                res = reqValues[m][0]
                l = m+1

            else:
                r = m-1

        return res





        
