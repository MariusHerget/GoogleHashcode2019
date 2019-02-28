from .basesolver import BaseSolver


class Solver(BaseSolver):
    # Greedy solver as presented during
    # 'Get Ready for Hash Code 2018' (https://youtu.be/rosx_Xa-R5Y)

    def __init__(self, input_str):


    def write(self, output_str):
        with open(output_str, 'w') as f:
            f.write(str(len(self.results)))
            f.write('\n')
            for s in self.results:
                f.write(" ".join([str(iii) for iii in list(s)]))
                f.write('\n')

    def solve(self):
        print("Not implemented yet.")

    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            self.row_count, self.column_count, self.min_ingredient, self.max_area = tuple(
                map(int, first_line.split(' '))
            )

            self.grid = []
            for i in range(self.row_count):
                self.grid.append(f.readline().rstrip())

        print("Problem statement:")
        print(self.row_count, self.column_count, self.min_ingredient, self.max_area)
        print(self.grid)
