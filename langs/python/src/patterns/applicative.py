import abc
from typing import TypeVar, Callable 
from functor import Functor

A = TypeVar('A')
B = TypeVar('B')

class Applicative(Functor[A], metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def pure(a: A) -> 'Applicative[A]': ...

    @abc.abstractmethod
    def star(self, gf: 'Applicative[Callable[[A], B]]') -> 'Applicative[B]':
        ...
