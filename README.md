# Overview

These are some experiments in game development in 2D and 2.5D as per [the excellent youtube tutorial](https://www.youtube.com/watch?v=ECqUrT7IdqQ) by [the awesome  Stanislav Petrov](https://github.com/StanislavPetrovV)


# Controls

## Movement

The player moves forward, backward, strides left and right using the `W`, `S`, `A` and `D` keys, respectively.

Note that in `2D`, the keys are locked onto the up, down, left and right directions on the screen regardless of the player's orientation on screen, whereas in `3D` these are all relative to the players orientation.

## Turning

By default, the player turns (i.e. changes orientation) using the mouse. If configured (see below sections), you can instead use the `LEFT` and `RIGHT` arrow keys.

# Running the game

The following command line args are available to configure the game mode:

```bash
PS C:\Users\bettmensch\GitReps\doom-python> python main.py --help
pygame 2.5.2 (SDL 2.28.3, Python 3.11.8)
Hello from the pygame community. https://www.pygame.org/contribute.html
usage: main.py [-h] [-d {2,3}] [-c {m,k}] [-r] [-l {0,1,2}]

Run game in 2D or 3D, toggle texture rendering and controls.

options:
  -h, --help            show this help message and exit
  -d {2,3}, --dimension {2,3}
                        Dimensions in game.
  -c {m,k}, --control-rotation {m,k}
                        Whether to turn using left/right arrow keys, or the mouse.
  -r, --render-textures
                        Toggle texture rendering on/off. Only relevant in 3D.
  -l {0,1,2}, --level {0,1,2}
                        Select a level to play. Defaults to first level.
```


## **2D**

To run the game in `2D` using the mouse to turn left/right, run

`python main.py -d 2 -c m`.

![2D screenshot](./image/doom-python-2d-mouse.JPG)

To run the game in `2D` using the `LEFT`/`RIGHT` arrow keys to turn left/right, respectively, run

`python main.py -d 2 -c k`.

![2D screenshot](./image/doom-python-2d.JPG)

## **3D**

To run the game in `3D` (or "`2.5D`") without texture rendering (and with mouse turning controls), run

`python main.py -d 3`

![2.5D screenshot](./image/doom-python-3d-mouse.JPG)

To run the game in `3D` (or "`2.5D`") with texture rendering (and with mouse turning controls), run

`python main.py -d 3 -r`

![2.5D with texture screenshot](./image/doom-python-3d-mouse-texture.JPG)

Add the `-c k` flag to the above commands to switch to LEFT/RIGHT arrow key turning controls.