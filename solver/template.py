from .basesolver import BaseSolver


class Solver(BaseSolver):
    # Greedy solver as presented during
    # 'Get Ready for Hash Code 2018' (https://youtu.be/rosx_Xa-R5Y)

    def __init__(self, input_str):
        self.input_str = input_str
        self.number_of_pictures, self.row_count, self.number_of_pictures_horizontal = 0, 0, 0
        self.photos = []
        self.vertical = []
        self.horizontal = []
        self.results = []

        # read all the input
        self.read_input()
         for i in range(0,self.number_of_pictures):
                line = f.readline().rstrip().split(' ')
                self.photos.append({\
                "orientation": line[0],\
                "number_of_tags": line[1],\
                "tags": line[2:]\
                })

    def write(self, output_str):
        with open(output_str, 'w') as f:
            f.write(str(len(self.results)))
            f.write('\n')
            for s in self.results:
                f.write(" ".join([str(iii) for iii in list(s)]))
                f.write('\n')

    def solve(self):
        print("not_implemented_yet")
