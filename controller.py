# pyright: strict

from time import sleep
from model import GameOfLifeModel, make_blank_grid
from view import GameOfLifeView

class GameOfLifeController:
    def __init__(self,  model: GameOfLifeModel | None = None, view: GameOfLifeView = GameOfLifeView()):
        self.__model = model
        self.__view = view
    
    def start(self) -> None:
        model = self.__model
        view = self.__view

        view.introduction()

        ok_to_start = True

        if self.__model is None:
            ok_to_start = False

        while not ok_to_start:
            dimensions = view.ask_dimensions()
            if isinstance(dimensions, tuple):
                ok_to_start = True
                m, n = dimensions
                self.__model = GameOfLifeModel(grid = make_blank_grid(m=m, n=n), generation_count = 0)
                model = self.__model
        
        assert model is not None

        asking_cmd = True
        alive = False

        while asking_cmd:

            view.show_generation_number(generation=model.generation_count)
            view.show_grid(grid=model.grid)

            view.cmd_list()
            cmd = view.ask_cmd()
            if not isinstance(cmd, str):
                continue

            match cmd.lower().strip():
                case "d":
                    dims = view.ask_dimensions()

                    if not dims:
                        print("Please Input the Dimensions in the Valid Format.")

                    else:
                        assert isinstance(dims,tuple)
                        m, n = dims
                        self.__model = GameOfLifeModel(grid = make_blank_grid(m=m, n=n), generation_count = 0)
                        model = self.__model

                case "e":
                    coords = view.ask_coords()

                    if not coords:
                        print("Please Input the Coordinates in the Valid Format.\n")
                        
                    else:
                        assert isinstance(coords,tuple)
                        r, c = coords

                        changed = model.change_cell(r=r, c=c)
                        if changed:
                            alive = True
                    
                case "g":
                    if alive:
                        alive = model.update()
                        
                    else:
                        asking_cmd = False

                case "r":
                    while alive:
                        alive = model.update()

                        view.show_generation_number(model.generation_count)
                        view.show_grid(model.grid)

                        sleep(0.3)

                    asking_cmd = False
                case _:
                    raise ValueError

            cmd = None
        
        print("Game Over!")
