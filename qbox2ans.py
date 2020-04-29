class point:
    def __init__(self, x, y, data=None):
        self.x        = x
        self.y        = y
        self.userdata = data

    def __str__(self):
        return f'point object with at {self.x, self.y}'

class cell:
    def __init__(self, x, y, half_width, half_height):
        self.x  = x
        self.y  = y
        self.half_width = half_width
        self.half_height = half_height

        self.min_x = self.x - self.half_width
        self.max_x = self.x + self.half_width
        self.min_y = self.y - self.half_height
        self.max_y = self.y + self.half_height


    def contains(self, pt):
        x, y = pt.x, pt.y

        if x <= self.max_x and x >= self.min_x and y <= self.max_y and y >= self.min_y:
            return True

        return False 


    def intersect(self, cel):
        if (self.min_x > cel.max_x or cel.min_x > self.max_x) or (
                 self.min_y > cel.max_y or cel.min_y > self.max_y):
            return False

        return True

    def __str__(self):
        return f'cell object with bottom left point at {self.min_x, self.min_y} and top right at {self.max_x, self.max_y}'


class quad_tree:
    hgt = 1
    def __init__(self, cell, cap=4, lvl=0):
        self.boundary = cell
        self.capacity = cap
        self.points   = []
        self.divided  = False
        self.n_points = 0
        self.level    = lvl

        if self.level + 1 > quad_tree.hgt:
            quad_tree.hgt = self.level + 1


    def subdivide(self):
        new_w = self.boundary.half_width / 2
        new_h = self.boundary.half_height / 2
       
        x = self.boundary.x
        y = self.boundary.y

        self.divided = True
        
        self.ne = quad_tree(cell(x+new_w, y+new_h, new_w, new_h), self.capacity, self.level+1)
        self.nw = quad_tree(cell(x-new_w, y+new_h, new_w, new_h), self.capacity, self.level+1)
        self.se = quad_tree(cell(x+new_w, y-new_h, new_w, new_h), self.capacity, self.level+1)
        self.sw = quad_tree(cell(x-new_w, y-new_h, new_w, new_h), self.capacity, self.level+1)

    def insert(self, pt):   
        if not self.boundary.contains(pt):
            return False

        self.n_points += 1

        if (len(self.points) < self.capacity):
            self.points.append(pt)
            return True

        if not self.divided:
            self.subdivide()


        if (self.nw.insert(pt)): return True
        if (self.ne.insert(pt)): return True
        if (self.sw.insert(pt)): return True
        if (self.se.insert(pt)): return True

        return False

    def query(self, range):
        found = []
        if not self.boundary.intersect(range):
            return found

        for pt in self.points:
            if range.contains(pt):
                found.append(pt)

        if self.divided:
            found.extend(self.ne.query(range))
            found.extend(self.nw.query(range))
            found.extend(self.se.query(range))
            found.extend(self.sw.query(range))

        return found

if __name__ == '__main__':
    ''' Given problem is 2D array query problem so it is better to use quad tree.
        Insert food packet positions into a quad tree and query it using cage position to find survivors '''
    t = int(input())
    for _ in range(t):
        l, w = list(map(int, input().split()))
        c  = cell(l//2, w//2, l//2, w//2)
        qt = quad_tree(c, 4)
        n, m = list(map(int, input().split()))
        cages = []
        for _ in range(n):
            centre = list(map(int, input().split()))
            cages.append(centre)
        for _ in range(m):
            x, y = list(map(int, input().split()))
            qt.insert(point(x, y))
        for x, y in cages:
            qrcell = cell(x, y, 2, 2)
            fnd = qt.query(qrcell)
            l = len(fnd)
            if l == 0 or l > 1:
                n -= 1
            m -= l
        print(n, m)
