from .basesolver import BaseSolver


class Solver(BaseSolver):
    # Greedy solver as presented during
    # 'Get Ready for Hash Code 2018' (https://youtu.be/rosx_Xa-R5Y)

    def __init__(self, input_str):
        self.input_str = input_str
        self.number_of_pictures, self.row_count = 0, 0
        self.photos = []
        self.vertical = []
        self.horizontal = []
        self.results = []

        # read all the input
        self.read_input()


    def solve(self):
        slideshow = [self.photos[0]]
        tempPhotos = self.photos[1:]
        while len(tempPhotos) > 0:
            scores = []
            for p in tempPhotos:
                scores.append(self.score(slideshow[-1].get('tags'), p.get('tags')))
            index = scores.index(max(scores))
            slideshow.append(tempPhotos[index])
            tempPhotos.pop(index)

        return slideshow

