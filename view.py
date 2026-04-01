# pyright: strict

from common_types import Cell

RANKING = {
    "1": "st",
    "2": "nd",
    "3": "rd",
}

class GameOfLifeView():
    def __process_input(self, user_input: str) -> bool | tuple[int,int]:
        tup_str_answer = tuple(user_input.split())
        
        if len(tup_str_answer) == 2:
            try:
                tup_int_answer = tuple(int(x) for x in tup_str_answer)
            except ValueError:
                return False

            assert len(tup_int_answer) == 2

            return tup_int_answer
        else:
            return False    
    
    def __int_rank(self, num: int) -> str:
        if str(num)[-1] in RANKING:
            return RANKING[str(num)[-1]]
        else:
            return "th"
        
    def show_grid(self, grid: list[list[Cell]]) -> None:
        for idx in range(len(grid)):
            print("".join((str(x) for x in grid[idx])))
        print()
    
    def show_generation_number(self, generation: int) -> None:
        print(
        f"Generation: {generation}{self.__int_rank(num=generation)}"
        )

    def ask_dimensions(self) -> bool | tuple[int,int]:
        answer = input(
        "What do you want your grid dimensions to be? (Dimensions: r c)\n- "
        )
        print()
        return self.__process_input(answer)
    
    def ask_coords(self) -> bool | tuple[int,int]:
        answer = input(
        "Which cell do you want to change? (Location: i j)\n- "
        )
        print()
        return self.__process_input(answer)
    
    def cmd_list(self) -> None:
        print(
        "Commands:\n" \
        "d : Reset the Grid Dimensions\n" \
        "e : Edit the Current Grid\n" \
        "g : Advance the Game by One Generation\n" \
        "r : Run the Game Automatically\n" \
        )

    def ask_cmd(self) -> bool | str:
        answer = input(
        "Which command do you want to run?\n- "
        )
        print()
        if answer in list("degrDEGR"):
            return answer
        else:
            return False

    def introduction(self) -> None:
        print(
        "Welcome to a Modified Version of Conway's Game of Life!\n" \
        "Made By: Ian\n" \
        "License: MIT License\n" \
        
        "\nRules:\n" \
        "1. Any live cell with fewer than two live neighbors dies,\n" \
        "   as if by underpopulation.\n" \
        "2. Any live cell with two or three live neighbors lives on\n" \
        "   to the next generation.\n" \
        "3. Any live cell with more than three live neighbors dies,\n" \
        "   as if by overpopulation.\n" \
        "4. Any dead cell with exactly three live neighbors becomes\n" \
        "   a live cell, as if by reproduction.\n"
        )
    
