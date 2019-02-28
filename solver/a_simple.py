from .basesolver import BaseSolver


class Solver(BaseSolver):
    # Greedy solver as presented during
    # 'Get Ready for Hash Code 2018' (https://youtu.be/rosx_Xa-R5Y)

    def __init__(self, input_str):
        self.input_str = input_str
        self.number_of_pictures, self.row_count = 0, 0
        self.photos = []
        self.results = []

        # read all the input
        self.read_input()

    def write(self, output_str):
        with open(output_str, 'w') as f:
            f.write(str(len(self.results)))
            f.write('\n')
            for s in self.results:
                f.write(" ".join([str(iii) for iii in list(s)]))
                f.write('\n')

    def solve(self):
        print("not_implemented_yet")
