# pyright: strict

from argparse import ArgumentParser

from file_reader import convert_to_grid
from common_types import Cell
from controller import GameOfLifeController


# TODO: Argparser + File Reader

def run(with_args: bool, grid: list[list[Cell]] | None = None) -> None:
    controller = GameOfLifeController()
    if with_args and grid is not None:
        controller.start_with_args(grid)
    else:
        controller.start_no_args()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=False,
        help="Input the name of the text file in the 'maps' directory."
    )

    args = parser.parse_args()

    valid_files = ... # TODO

    if args.file is not None and args.file in valid_files:
        run(with_args=True, grid=convert_to_grid(args.file))

    elif args.file is not None and args.file not in valid_files:
        print(f"File {args.file} not found!")
        print()
        run(with_args=False)

    else:
        run(with_args=False)

