from typing import TypeVar, Generic, Callable 
from patterns.functor import Functor 
from patterns.applicative import Applicative
from patterns.monad import Monad

A = TypeVar('A')
B = TypeVar('B')

class _BaseMaybe(Generic[A]):

    def is_just(self) -> bool:
        return False 

    def is_nothing(self) -> bool:
        return False

class Just(_BaseMaybe[A]):

    def __init__(self, value: A) -> None:
        self.value = value

    @property
    def value(self) -> A:
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def is_just(self) -> bool:
        return True

class Nothing(_BaseMaybe):
    
    def __init__(self) -> None:
        pass
    
    def is_nothing(self) -> bool:
        return True

class Maybe(Monad[A]):

    def __init__(self, maybe: _BaseMaybe[A]) -> None:
        self.maybe = maybe

    @property
    def maybe(self) ->_BaseMaybe[A]:
        return self._maybe

    @maybe.setter
    def maybe(self, value):
        self._maybe = value

    '''
    _ <*> Nothing = Nothing
    f <*> Just x  = Just f x
    '''
    def fmap(self, f: Callable[[A], B]) -> 'Functor[B]':
        if self.maybe.is_just():
            return Maybe(Just(f(self.maybe.value)))
        else:
            return Maybe(Nothing())

    @staticmethod
    def pure(a: A) -> 'Applicative[A]':
        return Maybe.ret(a) 

    '''
    Nothing <*> _ = Nothing
    Just f  <*> x = fmap f x
    '''
    def star(self, gf: 'Applicative[Callable[[A], B]]') -> 'Applicative[B]':
        if gf.maybe.is_just():
            return self.fmap(gf.maybe.value)
        else:
            return Maybe(Nothing())

    @staticmethod
    def ret(a: A) -> Monad[A]:
        return Maybe(Just(a)) 

    '''
    Nothing >>= _ = Nothing
    Just x  >>= f = f x
    '''
    def bind(self, f: Callable[[A], Monad[B]]) -> Monad[B]:
        if self.maybe.is_just():
            return f(self.maybe.value)
        else:
            return Maybe(Nothing())
