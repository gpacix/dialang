# Dialang Documentation

## Nodes

Nodes all have a shape, an ID, and a label:

```
rect r1 "First Rectangle" ...
```

Here, `rect` is the shape, `r1` is the ID, and `First Rectangle` is
the label.  If your label has no spaces, you don't need quotes. Either
double or single quotes work for labels.

You also need to specify a position and a size for your node; there
are a number of ways to do this:
```
diagram Positioning width 800 height 600 style clean
rect ruls "Upper-Left and Size" ul 10 10 size 200 50 class c1
rect rullr "Upper-Left and Lower-right" ul 310 10 lr 600 60 class c2
rect rcs "Center and Size" center 110 235 size 200 50 class c3
rect rcur "Center and Upper-Right" center 460 235 ur 610 210 class c4
```

You can specify `ul/ll/ur/lr/center/size` in any order. You must give
enough information to figure out the corners of the rectangle; for
instance, `ul` and `ll` are not enough and will cause an error.

The current list of available shapes is:
  - `rect` : rectangle
  - `rrect` : rounded rectangle
  - `oval` : racetrack-shaped
  - `diamond` : diamond shape, with points up and down
  - `cloud` : cloud outline
  - `cylinder` : cylinder outline
  - `para` : parallelogram (aren't you glad I don't make you type that all out?)
  - `hex` : hexagon, with top and bottom sides level and long
  - `circle` : circle, with a center and radius

All of them specify their size and position like `rect`, *except for
`circle`*.  For `circle`, you must supply a `center` (2 numbers) and a
`radius` (1 number).  (You cannot abbreviate either attribute name.)

`circle circle1 "A Circle" center 200 300 radius 100`


## Node Labels

You can omit a node label by supplying `" "`; the quotes are
mandatory, since you're setting it to a single space.

Labels have their own styles, though if you set a node's style, its
label will default to the same style.  This lets the stylesheet author
pick text colors that will contrast with the node colors.

Labels can be misinterpreted if they begin with a reserved word;
quoting will not help with this, but adding an initial or final space
to the label will:

`rect rcen " center" center 100 100 size 80 60`

While a label can appear anywhere in the line, you should place it
directly after the ID to maintain your sanity.

### Label Stretching

The program tries to make labels fit inside their node; the results
can be extreme to the point of being illegible.  One workaround is to
make an invisible node that is much wider, and put the label on that.

```
diagram Label_Squashing width 800 height 800 style clean
rect r1 class c0 center 60  40 size 100 60 "Word"
rect r2 center 60 140 size 100 60 "Word Word"
rect r3 center 60 240 size 100 60 "Word Word Word"
rect r4 center 60 340 size 100 60 "Word Word Word Word"
rect r5 center 60 440 size 100 60 "Word Word Word Word Word"
rect r6 center 60 540 size 100 60 "Word Word Word Word Word Word"
rect r7 center 60 640 size 100 60 "Word Word Word Word Word Word Word Word Word Word Word Word"
```

### Rotating Labels

(Note that only the labels are rotated, not the node they are
associated with.)

You can rotate a label by supplying the `trotate` attribute.  This is
given in degrees clockwise.  (Again, I apologize to math teachers
everywhere.) So this:

`circle circle1 "A Circle" trotate -45 center 200 300 radius 100`

...gives you a circle with the words "A Circle" in it, with the
initial "A" in the lower left, and the final "e" in the upper right.

`rrect rounded1 "A Rounded Rect" trotate -90 center 400 300 size 100 100`

...gives you a rounded rectangle with the words "A Rounded Rect" in
it, with the "A" at the bottom and the "t" at the top, so you have to
flop your head to the left to read it (the way books are shelved in
many European countries).

`diamond diamond1 "A Diamond" trotate 90 center 400 300 size 100 100`

...gives you a diamond with the words "A Diamond" in it, with the "A"
at the top and the "d" at the bottom, so you have to flop your head to
the right to read it (the way books are shelved in the U.S.).

Similarly, if you want upside-down text, you can set `trotate 180`,
though you should begin to wonder about the life choices
that brougt you to that point.

## Node URLs

`url`: you can specify a URL to go to when the node is clicked on

`diamond d1 "Diamond" center 100 100 size 100 80 url https://en.wikipedia.org/wiki/Diamond`

Specify the `http` or `https` and hostname along with the path to
avoid strange results.


## Edges

Edges have an ID, but no label; e.g.:

```
edge undir2 from r3 to r2
```

All edges must have a `from` and a `to` attribute, each of which takes
a single node ID.

Edges can have an arrow at their head end, their tail end, or both.
You specify this with the `arrow` attribute:

```
edge dir1 from r1 to r2 arrow head
edge dir2 arrow head from r3 to r5
edge dir3 arrow tail from r4 to r2
edge dir4 arrow both from r5 to r1
```

The default value for `arrow` is `none`, which you can specify if you
really want to.

If an edge has ID `abc` in the source file, the SVG ID of the edge is
the same: `abc`.  The SVG ID of its arrowheads (if they exist) is
`abc-he` for the head (destination) end, and `abc-ta` for the tail
(source) end.

Every edge has CSS class `edge`.  This is mandatory.  You can,
however, add other classes with the `class` attribute of edges. If you
want to add multiple classes, you *must* list them space-separated
inside one outer pair of quotes: `class "additionalclass otherclass"`.

Every arrowhead has the CSS class `arrowhead` (and not `edge`).
Arrowheads pick up all other classes that their edges have:

```
edge e1 arrow head from n1 to n2 class important
```

The line part of the edge: id = `e1`, class = `edge important`

The arrowhead part of the edge: id = `e1-he`, class = `arrowhead important`

### Styles for Edges

Styles and stylesheets should let you specify "thick" and "thin" as
classes for edges; these make the edge thicker or thinner than the
default edge width, typically by about 50%.

Styles and stylesheets should let you specify "dashed" and "dotted" as
classes for edges; these do what you would expect.

Styles and stylesheets should let you specify "important" and
"unimportant" as classes for edges; these make the edge either more or
less prominent than normal edges.


### Layers and Edges

Edges by default have a z value of -1, which means they are under the
default layer of nodes, which is (z =) 0. You can specify a higher z
value for an edge if you want it to be above one or more nodes. You
can also specify a lower z value for a node you want to be below
everything else (e.g. a background rectangle).
