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

    def solve(self):
        """Solves the problem.
        Stores the solution internally.

        :return: Nothing, everything should be save internally.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def write(self, output_str):
        """Writes a solution file with the solved solution.

        :param output_str: The output filepath where to save the solution.
        :return: Nothing.
        """
        raise NotImplementedError("This method needs to be implemented.")

    def read_input(self):
        with open(self.input_str, 'r') as f:
            first_line = f.readline()

            self.number_of_pictures = int(first_line)
            self.number_of_pictures_horizontal = 0
            self.photos = []
            for i in range(0,self.number_of_pictures):
                line = f.readline().rstrip().split(' ')
                self.photos.append({\
                "orientation": line[0],\
                "number_of_tags": line[1],\
                "tags": line[2:]\
                })

                if line[0] == "H":
                    self.horizontal.append({\
                    "orientation": line[0],\
                    "number_of_tags": line[1],\
                    "tags": line[2:]\
                    })
                    self.number_of_pictures_horizontal = self.number_of_pictures_horizontal+1
                else:
                    self.vertical.append({\
                    "orientation": line[0],\
                    "number_of_tags": line[1],\
                    "tags": line[2:]\
                    })

            for c in self.horizontal:
                for d in self.horizontal:
                    self.horizontalSlides.append({\
                        "orientation": c.get('orientation'),\
                        "number_of_tags": int(c.get('number_of_tags'))+ int(d.get('number_of_tags')),\
                        "tags": c.get('tags') + d.get('tags') \
                        })


        """
        print(self.horizontal)
        print(self.vertical)
        """

        print("Problem statement:")
        print("Number of pictures in horizontal: ", self.number_of_pictures)
        print(self.number_of_pictures)


        