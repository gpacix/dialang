# Dialang Documentation

## Edges

Edges have an ID, but no label; e.g.:

```
edge undir2 from r3 to r2
```

All edges must have a `from` and a `to` attribute, each of which takes
a single node ID.

Edges can have an arrow at their head end (tail and both are coming
later).  You specify this with the `arrow` attribute:

```
edge dir1 from r1 to r2 arrow head
edge dir2 arrow head from r3 to r5
```

The default value for `arrow` is `none`, which you can specify if you
really want to.

Every edge has CSS class `edge`.  This is mandatory.  You can,
however, add other classes with the `class` attribute of edges. If you
want to add multiple classes, you *must* list them space-separated
inside one outer pair of quotes: `class "additionalclass otherclass"`.

Styles and stylesheets should let you specify "thick" and "thin" as
classes for edges; these make the edge thicker or thinner than the
default edge width, typically by about 50%.

Styles and stylesheets should let you specify "dashed" and "dotted" as
classes for edges; these do what you would expect.

Edges by default have a z value of -1, which means they are under the
default layer of nodes, which is (z =) 0. You can specify a higher z
value for an edge if you want it to be above one or more nodes. You
can also specify a lower z value for a node you want to be below
everything else (e.g. a background rectangle).
