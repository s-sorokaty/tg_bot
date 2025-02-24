

class People():
    def __init__(self, bb = 0, bg = 0, kb = 0, kg = 0, zb = 0, zg = 0, sb = 0, sg = 0, ob = 0, og= 0,):
        self.bb = bb
        self.bg = bg

        self.kb = kb
        self.kg = kg

        self.zb = zb
        self.zg = zg

        self.sb = sb
        self.sg = sg

        self.ob = ob
        self.og = og

    def as_list(self) -> list:
        return [self.bb, self.bg, self.kb, self.kg, self.zb, self.zg, self.sb, self.sg, self.ob, self.og]
    
    def from_list(self, arr:list):
        self.bb = arr[0]
        self.bg = arr[1]
        self.kb = arr[2]
        self.kg = arr[3]
        self.zb = arr[4]
        self.zg = arr[5]
        self.sb = arr[6]
        self.sg = arr[7]
        self.ob = arr[8]
        self.og = arr[9]
    
    def from_answer(self, answer:str):
        s = answer.split("_")
        self.bb = s[0]
        self.bg = s[1]
        self.kb = s[2]
        self.kg = s[3]
        self.zb = s[4]
        self.zg = s[5]
        self.sb = s[6]
        self.sg = s[7]
        self.ob = s[8]
        self.og = s[9]

    def as_answer(self) -> str:
        return f"{self.bb}_{self.bg}_{self.kb}_{self.kg}_{self.zb}_{self.zg}_{self.sb}_{self.sg}_{self.ob}_{self.og}"
    
    def increce_by_id(self, item_id:int):
        arr = self.as_list()
        arr[item_id] = str(int(arr[item_id]) + 1)
        self.from_list(arr)

    def decrece_by_id(self, item_id:int):
        arr = self.as_list()
        arr[item_id] = "0"
        self.from_list(arr)
