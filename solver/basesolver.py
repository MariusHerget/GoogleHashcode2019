class BaseSolver(object):
    """Don't touch this!
    This class makes sure that those two methods gets implemented,
    as needed in main.py.
    """

    def __init__(self, input_str):
        """Initialisation of the given problem.

        :param input_str: The input filepath to process.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def checkcommontags(self, tags1, tags2):
        counter = 0
        for tag in enumerate(tags1):
            for tag2 in enumerate(tags2):
                if tag[1] == tag2[1]:
                    counter += 1
        return counter

    def score(self, tags1, tags2):
        i = self.checkcommontags(tags1, tags2)
        j = len(tags1) - i
        h = len(tags2) - i
        return min(i, j, h)

    def solve(self):
        """Solves the problem.
        Stores the solution internally.

        :return: Nothing, everything should be save internally.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def write(self, output_str, slideshow):
        solutionString = str(len(slideshow)) + "\n"
        for slide in slideshow:
            solutionString += str(slide.get('index')) + "\n"

        print(solutionString)
        """Writes a solution file with the solved solution.

        :param output_str: The output filepath where to save the solution.
        :return: Nothing.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            self.number_of_pictures = int(first_line)

            self.photos = []
            for i in range(0,self.number_of_pictures):
                line = f.readline().rstrip().split(' ')
                self.photos.append({\
                "orientation": line[0],\
                "number_of_tags": line[1],\
                "tags": line[2:],\
                "index": i\
                })

                if line[0] == "H":
                    self.horizontal.append({\
                    "orientation": line[0],\
                    "number_of_tags": line[1],\
                    "tags": line[2:]\
                    })
                else:
                    self.vertical.append({\
                    "orientation": line[0],\
                    "number_of_tags": line[1],\
                    "tags": line[2:]\
                    })
        """
        print(self.horizontal)
        print(self.vertical)
"""

        print("Problem statement:")
        print("Number of pictures: ", self.number_of_pictures)
        print(self.photos)
        