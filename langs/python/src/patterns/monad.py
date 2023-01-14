import abc
from typing import TypeVar, Callable
from applicative import Applicative

A = TypeVar('A')
B = TypeVar('B')

class Monad(Applicative[A], metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def ret(a: A) -> 'Monad[A]': ...

    @abc.abstractmethod
    def bind(self, f: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        ...
