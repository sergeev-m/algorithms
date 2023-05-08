# L. Два велосипеда

from typing import Tuple


class Pig:
    def __init__(self, n=None, arr=None, s=None):
        self.n = n or int(input())
        self.arr = arr or list(map(int, input().split()))
        self.s = s or int(input())

    def binary_search(self, s: int, left: int, right: int) -> int:
        if self.arr[-1] < s:
            return -1
        if right <= left:
            return left + 1
        mid = (left + right) // 2
        if self.arr[mid] < s:
            return self.binary_search(s, mid + 1, right)
        else:
            return self.binary_search(s, left, mid)

    @property
    def one_two_bicycles(self) -> Tuple[int, int]:
        one = self.binary_search(self.s, 0, self.n)
        if one == -1:
            return -1, -1
        two = self.binary_search(self.s << 1, one, self.n)
        return one, two


def test():
    pig = Pig(6, [1, 2, 4, 4, 6, 8], 3)
    assert pig.one_two_bicycles == (3, 5)

    pig = Pig(6, [1, 2, 4, 4, 4, 4], 3)
    assert pig.one_two_bicycles == (3, -1)

    pig = Pig(6, [1, 2, 4, 4, 4, 4], 10)
    assert pig.one_two_bicycles == (-1, -1)

    pig = Pig(6, [1, 2, 4, 4, 4, 4], 1)
    assert pig.one_two_bicycles == (1, 2)


def main() -> None:
    pig = Pig()
    print(*pig.one_two_bicycles)


if __name__ == '__main__':
    # main()
    test()
