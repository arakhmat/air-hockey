import numpy as np

class Score(object):

    def __init__(self, dim):
        self._score = {'top': 0, 'bottom': 0}
        self.dim = dim

    def get_top(self):
        return self._score['top']

    def get_bottom(self):
        return self._score['bottom']

    def update(self, puck):
        x, y = puck.position

        scored = None
        if y < self.dim.top_goal:
            self._score['bottom'] += 1
            puck.default_position[:] = self.dim.puck_default_position_bottom
            scored = 'bottom'
        elif y > self.dim.bottom_goal:
            self._score['top'] += 1
            puck.default_position[:] = self.dim.puck_default_position_top
            scored = 'top'

        if not (self.dim.rink_left < x < self.dim.rink_right):
            if np.random.randint(2):
                puck.default_position[:] = self.dim.puck_default_position_top
            else:
                puck.default_position[:] = self.dim.puck_default_position_bottom
            scored = 'out_of_bounds'
        return scored

    def __repr__(self):
        return str(self._score)

    def reset(self):
        self._score['top']    = 0
        self._score['bottom'] = 0