# AI assignment 2. Evolutionary algorithms.
#### INITIALIZATION
Algorithm creates population which consists of one parent. Parent it is set of 70 random black polygons with 70 percent transparency. 
#### CROSSOVER
As we have only one parent at first iteration so it is automatically selected as the best.
As algorithm have only one parent so crossover is just copy of parent’s set of polygons.
#### MUTATION
After copy of parent’s polygons algorithm mutates one random parameter of one random polygon on random variable. Set of parameters consist of: x coordinates for each point(4) (from 1 to 512), y coordinates for each point(4) (from 1 to 512), R level (from 0 to 255), G level (from 0 to 255), B level (from 0 to 255) and transparency(from 1 to 99).
#### FITNESS FUNCTION 
Fitness function is pixel by pixel sum of squares of r g b levels compare between original image and child image.
Algorithm use numpy for better executing time. 
#### SELECTION
After calculations of child fitness, we decide to bring it or not. Smaller fitness is better fitness. If child is not better, we go to the next iteration without changing parent. It is a competition between child and parent.

------
## Getting Started
1. Use python 3.6 and higher.
2. Install or update Pillow before executing.
#### Execute commands:
```
$ python3 AI2.py
```
## Examples
[Input](https://github.com/plohoicod/ai_art/blob/master/4.2.03.tiff)
[Result](https://github.com/plohoicod/ai_art/blob/master/egor_polivtsev.png)
