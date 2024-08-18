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

08/17/24 19:16:28 EDT --

Should the grid layout just keep repeating forever?
In other words, start over from the beginning line?
That could be useful, and probably not very confusing.

Then you could do things like:

diagram LayoutInputGrid size auto
layout grid 160 160 80 80
012
endlayout
rect r0 class c0
rect r1 class c1
rect r2 class c2
rect r3 class c3
rect r4 class c4
rect r5 class c5

...and get two rows of three, and if you add r6 - r8,
you'd get three rows of three, etc.

Also I had an idea last week that it should *not* add its size to
a line that already has a size (tough to figure out, though, since ul and lr
together imply a size).  That way, you could easily override the default
size for a couple items.
--08/17/24 19:18:12 EDT

Another idea is to have the ability to assign different widths to some columns,
and different heights to some rows, though that starts to sound unduly complicated.
Right now I think if you want a wider first column, you can just override the widths
or something... I'll give it a try.
-- 08/17/24 19:20:48 EDT

08/19/24 11:10:13 EDT --

(On the St. John's campus, sitting on a bench.)

Got the pitch/size/offset working yesterday or the day before.

So I think a different layout, maybe called "columns", could accommodate the
first-column-wider use case, as well as the "keep filling in this layout until
another layout is selected" use case.

Potential syntax:
```
layout columns 4 pitch 160 80 size 150 70 offset 50 30
endlayout
```

Or, for differing columns:
```
layout columns offset 50 30
pitch 160 80 size 150 70
pitch  80 80 size  70 70
pitch  80 80 size  70 70
pitch  80 80 size  70 70
endlayout
```

Maybe the first syntax isn't needed; we could achieve it with:
```
layout columns offset 50 30
pitch 160 80 size 150 70
pitch 160 80 size 150 70
pitch 160 80 size 150 70
pitch 160 80 size 150 70
endlayout
```

Except isn't the height going to always be the same?
Or do we want to automatically determine the height?
Hmm....

```
layout columns offset 50 30 pitch 80 height 70
pitch 160 size 150
pitch  80 size  70
pitch  80 size  70
pitch  80 size  70
endlayout
```

But why not just say "width" and "height"?
```
layout columns offset 50 30 cellheight 80 height 70
cellwidth 160 width 150
cellwidth  80 width  70
cellwidth  80 width  70
cellwidth  80 width  70
endlayout
```

I'm assuming here that the first (unsized) element after the layout will
go in the first column of the first row, through the fourth element,then
the fifth element will be in the first column of the second row, etc.:

```
AAA BB CC DD
EEE FF GG HH
III JJ KK LL
```

People will probably want to left/center/right and top/middle/bottom justify shapes
inside their cells.  I think I'm OK letting them do their own layout and not making
this one any more complicated.

So should there be a similar one for rows?  Are people really going to need that?
Enough of them that I should write it?

Can we just use the columns one, but tell it to rotate the layout 90°?
Seems kind of like a hack, and would still complicate the code.

Reduce repetition with an `x` command?

```
layout columns offset 50 30
pitch 160 80 size 150 70
pitch  80 80 size  70 70
x 3
endlayout
```

`x 1` would do nothing; `x 2` would simply repeat the line above;
`x 3` would mean "three copies of the line above".
Seems good, useful, and simple to implement.

So a completely uniform four-column layout would look like this:
```
layout columns offset 50 30 cellheight 80 height 70
cellwidth 160 width 150
x 4
endlayout
```

I think this makes the one-line syntax unnecessary.

--08/19/24 11:34:00 EDT
08/19/24 11:41:00 EDT --

Maybe we should back-port the offset/cellheight/height syntax to
layout grid (GridLayout) as offset/pitch/size so as to
(a) be more consistent
(b) be clearer

So then it would look like:
```
diagram LayoutInputGrid size auto
# newer pitch, size syntax:
layout grid pitch 160 160  size 158 159  offset 40 20
012
345
endlayout
rect r0 class c0
rect r1 class c1
rect r2 class c2
rect r3 class c3
rect r4 class c4
rect r5 class c5
```

Yeah, that works, and shows we don't hate our users.

Maybe have a `defaults` preprocessor, the way we have the `layouter` preprocessor?
I'm not sure how to decide what to add to the core language.

--08/19/24 11:50:58 EDT--

The `defaults` preprocessor would allow things like:
```
default color blue size 160 60
# will be colored blue:
r3 "Explicitly-sized" ul 20 20 size 100 50
# will be 100x50:
r4 "Default-sized" ul 140 20 class c3
```

Actually, we could just build this into `layouter`.
We probably need to either translate `size` into `radius` for circles, or
just let them take `size`, and be ellipses with a special actual-circle syntax.

Of course, then `layouter` (or a separate `defaults` preprocessor) needs to know a lot more
about the syntax of the items.  Maybe defaults are something it makes more sense to add
to the core language and `diagram` code.

Before I forget: last week I realized it would be cool to name the language "Minard",
after J. C. Minard, the guy who did the Napoleon-to-and-from-Moscow chart.

--08/19/24 11:58:40 EDT--

Still not sure whether to specify a height for rows defined in the columns layout.
Maybe a minimum height?  And then the layout engine does what? It knows the size of
the items as it adds them, so it can absolutely position the lower ones.

--08/19/24 12:00:24 EDT--

(Bells tolled for Noon.)

Well, even if we know the height of the *items* in a row, we don't know how much
vertical spacing to use, so we either need to specify spacing (which we don't do
elsewhere) or we need to specify the height (which we do already with pitch in the
grid layout).  Specifying height seems like a better idea, for consistency. And
minimum height seems like it would be too complicated; if something is too tall to
fit, then it's too tall to fit; it's not the end of the world.

So we'll specify row-height in the column layout.

--08/19/24 12:04:01 EDT
