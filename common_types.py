# pyright: strict

from enum import Enum, auto 
from abc import ABC, abstractmethod
from typing import Any

class CellState(Enum):
    DEAD = auto()
    ALIVE = auto()

class AbstractCell(ABC):
    @abstractmethod
    def __init__(self, state: CellState):
        ...

    @property    
    @abstractmethod
    def cell_state(self) -> CellState:
        ...
    
    @abstractmethod
    def swap_state(self) -> None:
        ...



class Cell(AbstractCell):
    def __init__(self, state: CellState):       
        self.__state = state

    def __str__(self) -> str:
        match self.__state:
            case CellState.DEAD:
                return "⬛"
            case CellState.ALIVE:
                return "⬜"
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, AbstractCell):
            return False
        return self.cell_state is other.cell_state

    @property
    def cell_state(self) -> CellState:
        return self.__state
    
    def swap_state(self) -> None:
        match self.__state:
            case CellState.ALIVE:
                self.__state = CellState.DEAD
            case CellState.DEAD:
                self.__state = CellState.ALIVE


