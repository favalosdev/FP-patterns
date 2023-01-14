import abc
from typing import TypeVar, Generic, Callable

A = TypeVar('A')
B = TypeVar('B')

class Functor(Generic[A], metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fmap(self, f: Callable[[A], B]) -> 'Functor[B]': ...
