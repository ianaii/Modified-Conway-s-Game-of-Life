# pyright: strict

from controller import GameOfLifeController

# TODO: Argparser + File Reader

def run():
    controller = GameOfLifeController()
    controller.start()

if __name__ == "__main__":
    run()
