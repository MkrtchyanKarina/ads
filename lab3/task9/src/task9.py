from utils import File


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def shortest_distance(n: int, dots: list[Dot]) -> float:
    dots = sorted(dots, key=lambda point: point.x)
    return separation(n, dots)


def separation(n: int, dots: list[Dot]):
    if n <= 3:
        return slow_shortest_distance(n, dots)
    middle = n // 2
    mid_dot = dots[middle]
    dl = separation(middle, dots[:middle])
    dr = separation(middle, dots[middle:])
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(dots[i].x - mid_dot.x) < d:
            strip.append(dots[i])
    return min(d, centre_dots(strip, len(strip), d))


def centre_dots(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda dot: dot.y)
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            min_dist = min(min_dist, euclidean_dist(strip[i], strip[j]))
    return min_dist


def euclidean_dist(dot1: Dot, dot2: Dot) -> float:
    return round(((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)**0.5, 4)





def slow_shortest_distance(n, dots):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, euclidean_dist(dots[i], dots[j]))
    return min_dist


def limits(n: int, dots: list[Dot]) -> bool:
    if 1 <= n <= 10**5 and len(dots) == n and all(abs(d.x) <= 10**9 and abs(d.y) <= 10**9 for d in dots):
        return True
    else:
        return False


def quick_sort_txt():
    f = File(__file__)
    arguments = f.read()
    n = int(arguments[0])
    dots = []
    for i in range(1, n+1):
        x, y = map(int, arguments[i].split(" "))
        dots.append(Dot(x, y))
    if limits(n, dots):
        res = str(shortest_distance(n, dots))
        f.write(res)


if __name__ == "__main__":
    quick_sort_txt()