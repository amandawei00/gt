import numpy as np

class Struct:
    def __init__(self, coords, paxis=[0,0,1], format='cart'):
        self.coords = coords
        self.paxis  = paxis

        if format=='cart':
            for i in range(len(coords)):
                x, y, z = coords[i][0], coords[i][1], coords[i][2]
                r   = np.sqrt(x * x + y * y + z * z)
                the = np.arcsin(z/r)
                phi = np.arccos(x/r/np.cos(the))
                coords[i]   = [x, y, z, r, the, phi]
        elif format == 'sph':
            for i in range(len(coords)):
                r, the, phi = coords[i][0], coords[i][1], coords[i][2]
                x = r * np.cos(the) * np.cos(phi)
                y = r * np.cos(the) * np.sin(phi)
                z = r * np.sin(the)
                coords[i] = [x, y, z, r, the, phi]

    def get_struct(self):
        return self.coords

    def rot(self, axis, theta):
        return 0
    def ref(self, axis):
        return 0

    def search_rot(self):
        return 0
    def search_ref(self):
        return 0
