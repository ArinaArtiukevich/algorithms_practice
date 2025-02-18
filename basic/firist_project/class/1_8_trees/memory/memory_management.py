class MemoryStructure:
    def __init__(self, n: int):
        dstructure = []
        for i in range(n):
            dstructure.append([0, i+1, 0])
        #     0 - first empty
        self.dstructure = [dstructure, 0]

    def set_node(self, num: int):
        self.dstructure[0][self.dstructure[1]][0] = num
        self.dstructure[1] = self.dstructure[0][self.dstructure[1]][1]

    def del_node(self, id_node: int):
        self.dstructure[0][id_node][1] = self.dstructure[1]
        self.dstructure[0][id_node][0] = 0
        self.dstructure[1] = id_node


if __name__ == '__main__':
   mstr = MemoryStructure(3)
   mstr.set_node(10)
   mstr.set_node(100)

   mstr.del_node(0)
   mstr.del_node(1)

