from typing import TypeVar, Callable 
from patterns.functor import Functor
from patterns.applicative import Applicative
from patterns.monad import Monad

A = TypeVar('A')
B = TypeVar('B')

class ListM(Monad[A], list[A]):

    def __init__(self, *args):
        list.__init__(self, *args)

    def fmap(self, f: Callable[[A], B]) -> Functor[B]:
        return ListM(map(f, self))

    @staticmethod
    def pure(a: A) -> Applicative[A]:
        return ListM.ret(a) 

    def star(self, gf: Applicative[Callable[[A], B]]) -> Applicative[B]:
        return ListM([f(a) for f in gf for a in self])

    @staticmethod
    def ret(a: A) -> Monad[A]:
        return ListM([a])

    def bind(self, f: Callable[[A], Monad[B]]) -> Monad[B]:
        return ListM([b for a in self for b in f(a)])
