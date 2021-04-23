import numpy as np

class Cube:
    def __init__(self):
        # Initial state: solved
        self.state = np.arange(1, 28).reshape((3, 3, 3))
        self.perm = []

    def mix(self):
        funcs = [self.L, self.R, self.U, self.D, self.B, self.F]

        while len(self.perm) <= np.random.randint(20, 30):
            func_idx = np.random.randint(len(funcs))
            clockwise = bool(np.random.randint(2))

            if len(self.perm) > 0:
                if self.perm[-1] == (funcs[func_idx].__name__, clockwise):
                    while self.perm[-1] != (funcs[func_idx].__name__, clockwise):
                        func_idx = np.random.randint(len(funcs))
                        clockwise = np.random.randint(100) % 2 == 0
                else:
                    self.perm.append((funcs[func_idx].__name__, clockwise))
                    self.state = funcs[func_idx](clockwise)
            else:
                self.perm.append((funcs[func_idx].__name__, clockwise))
                self.state = funcs[func_idx](clockwise)

    def R(self, clockwise=True):
        return self.rotate_and_perform(axes=(0, 2), clockwise=clockwise)

    def L(self, clockwise=True):
        return self.rotate_and_perform(axes=(2, 0), clockwise=clockwise)

    def U(self, clockwise=True):
        return self.rotate_and_perform(axes=(1, 0), clockwise=clockwise)

    def D(self, clockwise=True):
        return self.rotate_and_perform(axes=(0, 1), clockwise=clockwise)

    def B(self, clockwise=True):
        cube = self.state.copy()
        cube[2] = np.rot90(cube[2], k=1 if clockwise is True else 3)
        return cube

    def F(self, clockwise=True):
        cube = self.state.copy()
        cube[0] = np.rot90(cube[0], k=3 if clockwise is True else 1)
        return cube

    def rotate_and_perform(self, axes, clockwise):
        rotated_cube = np.rot90(self.state.copy(), axes=axes)
        rotated_cube[0] = np.rot90(rotated_cube[0], k=3 if clockwise is True else 1)
        return np.rot90(rotated_cube, axes=np.flip(axes))

    def print_state_permutation(self):
        for elem in self.perm:
            print(elem[0] + ('\'' if elem[1] is True else ''))

    def print_back_solve(self):
        if len(self.perm) > 0:
            for elem in np.flip(self.perm):
                print(elem[1] + ('\'' if eval(elem[0]) is False else ''))