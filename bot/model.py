

class People():
    def __init__(self, kb = 0, kg = 0, zb = 0, zg = 0):

        self.kb = kb
        self.kg = kg

        self.zb = zb
        self.zg = zg


    def as_list(self) -> list:
        return [self.kb, self.kg, self.zb, self.zg]
    
    def from_list(self, arr:list):
        self.kb = arr[0]
        self.kg = arr[1]
        self.zb = arr[2]
        self.zg = arr[3]
    
    def from_answer(self, answer:str):
        s = answer.split("_")
        self.kb = s[0]
        self.kg = s[1]
        self.zb = s[2]
        self.zg = s[3]
       
    def __str__(self):
        return f"{self.kb}_{self.kg}_{self.zb}_{self.zg}"
    
    def as_answer(self) -> str:
        return f"{self.kb}_{self.kg}_{self.zb}_{self.zg}"
    
    def increce_by_id(self, item_id:int):
        arr = self.as_list()
        arr[item_id] = str(int(arr[item_id]) + 1)
        self.from_list(arr)

    def decrece_by_id(self, item_id:int):
        arr = self.as_list()
        arr[item_id] = "0"
        self.from_list(arr)
