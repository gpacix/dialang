# TODO

 __ add some more shapes  04/07/24 17:17:36 EDT
    __ polygon
    __ path
 __ plow through on common errors  04/24/24 22:16:29 EDT
 __ report errors, with line number and some context  04/24/24 22:16:29 EDT
 __ label placement options, possibly as a separate label element 04/11/24 21:42:42 EDT
 __ multi-line text (\n) 04/11/24 21:42:43 EDT
 __ make label automatically pick up the class from its container  04/11/24 21:43:23 EDT
 __ make including source code optional  04/11/24 21:44:40 EDT
 __ let the user declare persistent class and text-class (may conflict with edges-first)  04/07/24 23:24:46 EDT
 __ replace "click" with URL in rollover text, or add title  04/07/24 23:42:45 EDT
 __ add an auto size, making the item just wide enough for its label
 __ add multi-line labels, or wrap them, or both 04/07/24 17:55:23 EDT
 __ add simple things from markdown to text: bold, italic  04/07/24 19:30:32 EDT
 __ add URL links to edges, (maybe can refer to these by ID?)  04/07/24 19:30:26 EDT
 __ add arrows to the edges (this will be tricky)  04/07/24 21:05:12 EDT
    ++ get the angle right
    ++ position them 90% along the edge at first
    ++ position them correctly for circles 04/13/24 18:23:41 EDT  d. 04/13/24 20:07:20 EDT
    ++ position them correctly for rects (and rrects) 04/13/24 18:23:43 EDT  d. 04/13/24 20:37:30 EDT
    __ position them correctly for diamonds
    __ position them correctly for ovals
 __ figure out good syntax for no label 04/07/24 19:30:16 EDT
 __ respect the lr/ul positions for edge start/end  04/07/24 16:25:26 EDT
 __ add a background, or let the user do so: background color gray  04/07/24 14:26:05 EDT
 __ make the language case-insensitive  04/07/24 13:13:42 EDT
 __ start dealing with stroke, not just fill  04/07/24 19:00:17 EDT
 __ add synonyms, like r for radius, c for center  04/10/24 16:37:14 EDT
 __ seriously consider making labels optional, or maybe: 'id:' and 'id label:' and 'id "long label":' 04/10/24 16:38:17 EDT
 __ what about optional IDs? could be easy with the above : syntax
 __ what about Smalltalk-like 'argname: val' syntax?
 __ add rollover effects: start with just changing color (or leave this to CSS?)  04/07/24 21:47:39 EDT
 __ simple automatic layout of shapes  04/07/24 21:44:03 EDT
 __ indicate that some items are contained inside other ones  04/07/24 21:42:41 EDT
 __ describe links with A -- B <- C -> D syntax; maybe support ---, -->, etc. too  04/07/24 21:43:28 EDT
 __ write up a convention for what should be in stylesheets; maybe include bold and italic?  04/10/24 23:25:09 EDT
    we already intend to provide classes c0-c5, plus corresponding legible text classes
 __ multi-edges, like the T edges in t-edges.dgm  04/11/24 22:04:24 EDT
 __ rotated text  04/11/24 22:04:24 EDT
 __ let the user define new shapes, maybe as macros; disallow recursion 04/07/24 18:58:29 EDT
 __ allow ll, ur, lr as ways to position a node  04/24/24 21:29:32 EDT

# DONE
 ++ take a line and turn it into a dict  04/07/24 13:27:43 EDT  d. 04/07/24 13:47:25 EDT
 ++ if something is an int, emit it as an int, not a float with six trailing 0 digits  04/07/24 13:20:20 EDT d. 04/07/24 14:05:43 EDT
 ++ let the user specify the size of the image  04/07/24 15:54:57 EDT d. 04/07/24 16:11:02 EDT
 ++ add the labels already  04/07/24 15:55:08 EDT d. 04/07/24 16:48:29 EDT
 ++ add a text-color attribute for items  04/07/24 16:50:55 EDT  d. 04/07/24 16:59:30 EDT
 ++ add oval  04/07/24 17:17:36 EDT  d. 04/07/24 17:22:39 EDT
 ++ add circle  04/07/24 17:17:36 EDT  d. 04/07/24 17:54:08 EDT
 ++ fix stretching: guess at width, take minimum  d. 04/07/24 18:57:44 EDT
 ++ let user modify context from the command line  d. 04/07/24 19:25:42 EDT
 ++ let the user set the font 04/07/24 17:55:23 EDT  04/07/24 19:36:28 EDT
 ++ recognize double-quoted and single-quoted strings as single tokens  04/07/24 14:06:23 EDT d. 04/07/24 21:05:26 EDT
 ++ add URL links to nodes, text (maybe can refer to these by ID?)  04/07/24 19:30:26 EDT d. 04/07/24 21:30:19 EDT
 ++ let the user declare a class for an item (so CSS can affect it)  04/07/24 19:29:54 EDT d. 04/07/24 23:16:49 EDT
 ++ add diamond  04/07/24 17:17:36 EDT d. 04/08/24 01:04:50 EDT
 ++ entity-encode the URLs before putting in the output  d. 04/10/24 16:36:02 EDT
 ++ provide "style" option to embed a provided style from css/ directory  d. 04/10/24 23:15:10 EDT
 ++ include the ID as the element ID in the SVG, so it can be styled  04/11/24 21:41:56 EDT d. 04/13/24 15:09:50 EDT
 ++ add cloud  04/07/24 17:17:36 EDT  d. 04/14/24 00:30:00 EDT
 ++ add cylinder  04/07/24 17:17:36 EDT  d. 04/14/24 00:30:00 EDT
 ++ add "created by" comment; optionally include (entity-encoded) source code  04/11/24 21:44:40 EDT d. 04/24/24 21:18:03 EDT
 ++ add z or layer coordinate; make edges default to 0, nodes default to 1  04/24/24 20:43:50 EDT d. 04/24/24 21:49:53 EDT
 ++ unify the path-based shapes: cylinder, cloud, others?  04/30/24 18:42:06 EDT d. 04/30/24 19:13:48 EDT
 ++ add parallelogram 04/07/24 17:17:36 EDT d. 04/30/24 21:31:29 EDT
 ++ add hexagon 04/07/24 17:17:36 EDT d. 04/30/24 21:31:29 EDT
 ++ escape any "--" in the source code: not permitted in comments  04/24/24 23:22:43 EDT d. 04/30/24 21:55:08 EDT


# ID stuff:

> Specifies the element's ID. The ID must be unique within the node
> tree, must not be an empty string, and must not contain any whitespace
> characters.

> It must be valid in XML documents. A stand-alone SVG document uses XML
> 1.0 syntax, which specifies that valid IDs only include designated
> characters (letters, digits, and a few punctuation marks), and do not
> start with a digit, a full stop (.) character, or a hyphen-minus (-)
> character.

Sounds like we can assume these are OK: .-_
So replace spaces with _
Maybe replace all other punctuation with -, or .?
Need to check that the ID is unique among all IDs encountered;
if it isn't, append -1, -2, etc.
--04/11/24 21:53:56 EDT--

This seems to be the governing spec: https://www.w3.org/TR/xml-names11/#NT-NCName
Basically, any valid name that doesn't include a colon (:).

[4]   	NameStartChar	   ::=   	":" | [A-Z] | "_" | [a-z] | [#xC0-#xD6] | [#xD8-#xF6] | [#xF8-#x2FF] | [#x370-#x37D] | [#x37F-#x1FFF] | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]
[4a]   	NameChar	   ::=   	NameStartChar | "-" | "." | [0-9] | #xB7 | [#x0300-#x036F] | [#x203F-#x2040]
[5]   	Name	   ::=   	NameStartChar (NameChar)*

So let's ignore the non-ASCII stuff.

That gives us [A-Za-z_][A-Za-z_-.0-9]*
Looks good.
--04/11/24 22:02:03 EDT
