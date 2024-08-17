## Thoughts on the design:

This is mostly going to be free of semantics, operating at the shape level.

Objects will be able to refer to other objects' positions.  Initially,
this will just be so we can have edges going from node to node without
having to update positions in both places.

Later, maybe we will have a full constraint solver or something. If we
throw in routing of edges so they don't intersect (or minimze
intersection), then that's an interesting direction.

Might make sense to have a CSV output/input format.

Start with auto-placement?  or relative placement directions?

So sample:

color blue
rect A "Starting Point" center 100 100 size 100 50
rrect B "Ending Point" ul 300 300 size 100 150 color green
edge E from A lr to B

This should generate a blue rectangle from 50, 75 to 150,125,
a green rounded rectangle from 300, 300 to 400, 450,
and a blue edge going from 150, 125 to 350, 375 (occluded by the second rect)

Other shapes we can have:
circle
oval
ellipse
hexagon
parallelogram
left-leaning parallelogram
diamond
square?
up-trianlge
down-triangle
cylinder
90° rotations of the above

(Should we allow users to define their own shapes?
 Seems like a good future feature.)

(Or maybe let them define macros.)

I think we should have some defaults:
color: color to use for things if no overriding color specified (INOS)
edge-color: color to use for edges INOS
node-color: color to use for nodes INOS

OK, let's make that diagram above.

--04/07/24 12:44:54 EDT

08/17/24 18:49:23 EDT --

I'm going to do layout as a separate tool; I did some work last week on it,
and it seems pretty nice to use:
  3154 Aug 11 20:06 layouter.py
  
I'll add that to the repo, then fix it:
It's pretty clear we need 3 pairs of numbers: object size, cell size, and grid's offset.
Right now, I have object size, padding, but no grid offset.
I may want to do things in terms of object centers, but ul is fine to start.

Oh, and earlier today I hosed my magit setup. Argh.

--08/17/24 18:52:07 EDT
