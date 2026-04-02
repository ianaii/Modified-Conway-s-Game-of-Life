# pyright: strict 

from copy import deepcopy
from common_types import CellState, Cell

class GameOfLifeModel:
    def __init__(self, grid: list[list[Cell]], generation_count: int):
        self.__grid = grid
        self.__generation_count = generation_count

    @property
    def grid(self) -> list[list[Cell]]:
        return deepcopy(self.__grid)

    @property
    def generation_count(self) -> int:
        return self.__generation_count
    
    @property
    def dimensions(self) -> tuple[int,int]:
        return (len(self.__grid), len(self.__grid[0]))
    
    def count_live_neighbors(self, r: int, c: int) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

        count = 0
        for dr, dc in dirs:
            if is_in_bounds(grid=self.__grid, r=r+dr, c=c+dc):
                cell = self.__grid[r+dr][c+dc]
                if cell.cell_state is CellState.ALIVE:
                    count += 1
        
        return count
    
    def count_dead_neighbors(self, r: int, c: int) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

        count = 0
        for dr, dc in dirs:
            if is_in_bounds(grid=self.__grid, r=r+dr, c=c+dc):
                cell = self.__grid[r+dr][c+dc]
                if cell.cell_state is CellState.DEAD:
                    count += 1
            
            else:
                count += 1

        return count
    
    def update(self) -> bool:
        m, n = self.dimensions

        new_grid = deepcopy(self.__grid)

        for i in range(m):
            for j in range(n):
                cell = self.__grid[i][j]
                new_cell = new_grid[i][j]
                
                live_neighbors = self.count_live_neighbors(r=i, c=j)
                match cell.cell_state:
                    case CellState.ALIVE:
                        if live_neighbors < 2 or live_neighbors > 3:
                            new_cell.swap_state()

                    case CellState.DEAD:
                        if live_neighbors == 3:
                            new_cell.swap_state()
        
        
        self.__generation_count += 1
        self.__grid = new_grid

        return new_grid != make_blank_grid(m=m, n=n)
    
    def change_cell(self, r: int, c: int) -> bool:
        m, n = self.dimensions

        if r in range(m) and c in range(n):
            self.__grid[r][c].swap_state()
            return True
        else:
            return False


# HELPER FUNCTIONS
def is_in_bounds(grid: list[list[Cell]], r: int, c: int) -> bool:
    return r in range(len(grid)) and c in range(len(grid[0]))

def make_blank_grid(m: int, n: int) -> list[list[Cell]]:
    grid: list[list[Cell]] = list()

    for _ in range(m):
        grid.append([Cell(CellState.DEAD) for _ in range(n)])

    return grid
