class Buffer:
    def __init__(self):
        self.args_list = []
        self.el_sum = int()

    def add(self, *args):
        for _ in args:
            self.args_list.append(_)
        if len(self.args_list) >= 5:
            for i in range(len(self.args_list) // 5):
                self.el_sum = 0
                for j in range(5):
                    self.el_sum += self.args_list.pop(0)
                print(self.el_sum)

    def get_current_part(self):
        return self.args_list
