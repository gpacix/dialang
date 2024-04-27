[12:57:58 gpaci@mac drawing-language]$ python diagram.py
['', 'color blue', 'rect A "Starting Point" center 100 100 size 100 50', 'rrect B "Ending Point" ul 300 300 size 100 150 color green', 'edge E from A lr to B', '']
[12:58:07 gpaci@mac drawing-language]$ python diagram.py
['color blue', 'rect A "Starting Point" center 100 100 size 100 50', 'rrect B "Ending Point" ul 300 300 size 100 150 color green', 'edge E from A lr to B']
[13:00:35 gpaci@mac drawing-language]$

[14:04:01 gpaci@mac drawing-language]$ python diagram.py
tokens: ['color', 'blue']
parsed: {'list': [], 'name': 'color', 'id': 'blue'}
tokens: ['rect', 'A', '"Starting_Point"', 'center', '100', '100', 'size', '100', '50']
parsed: {'list': ['"Starting_Point"'], 'name': 'rect', 'id': 'A', 'center': (100, 100), 'size': (100, 50)}
tokens: ['rrect', 'B', '"Ending_Point"', 'ul', '300', '300', 'size', '100', '150', 'color', 'green']
parsed: {'list': ['"Ending_Point"'], 'name': 'rrect', 'id': 'B', 'ul': (300, 300), 'size': (100, 150), 'color': 'green'}
tokens: ['edge', 'E', 'from', 'A.lr', 'to', 'B']
parsed: {'list': [], 'name': 'edge', 'id': 'E', 'from': 'A.lr', 'to': 'B'}
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
<rect x="50.000000" y="75.000000" width="100" height="50" rx="0" ry="0" fill="blue" />
</svg>
[14:04:19 gpaci@mac drawing-language]$

[14:18:33 gpaci@mac drawing-language]$ python diagram.py
tokens: ['color', 'blue']
parsed: {'list': [], 'name': 'color', 'id': 'blue'}
tokens: ['rect', 'A', '"Starting_Point"', 'center', '100', '100', 'size', '100', '50']
parsed: {'list': ['"Starting_Point"'], 'name': 'rect', 'id': 'A', 'center': (100, 100), 'size': (100, 50)}
tokens: ['rrect', 'B', '"Ending_Point"', 'ul', '300', '300', 'size', '100', '150', 'color', 'green']
parsed: {'list': ['"Ending_Point"'], 'name': 'rrect', 'id': 'B', 'ul': (300, 300), 'size': (100, 150), 'color': 'green'}
tokens: ['edge', 'E', 'from', 'A.lr', 'to', 'B']
parsed: {'list': [], 'name': 'edge', 'id': 'E', 'from': 'A.lr', 'to': 'B'}
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="None" />
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" />
</svg>
[14:18:56 gpaci@mac drawing-language]$

[14:45:41 gpaci@mac drawing-language]$ python diagram.py
tokens: ['color', 'blue']
parsed: {'list': [], 'name': 'color', 'id': 'blue'}
tokens: ['rect', 'A', '"Starting_Point"', 'center', '100', '100', 'size', '100', '50']
parsed: {'list': ['"Starting_Point"'], 'name': 'rect', 'id': 'A', 'center': (100, 100), 'size': (100, 50)}
tokens: ['rrect', 'B', '"Ending_Point"', 'ul', '300', '300', 'size', '100', '150', 'color', 'green']
parsed: {'list': ['"Ending_Point"'], 'name': 'rrect', 'id': 'B', 'ul': (300, 300), 'size': (100, 150), 'color': 'green'}
tokens: ['edge', 'E', 'from', 'A.lr', 'to', 'B']
parsed: {'list': [], 'name': 'edge', 'id': 'E', 'from': 'A.lr', 'to': 'B'}
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" />
<line x1="100" y1="100" x2="350" y2="375" style="stroke:blue;stroke-width:3" />
</svg>
[14:47:05 gpaci@mac drawing-language]$  # note how the edge is on top of the nodes

[15:06:06 gpaci@mac drawing-language]$ python diagram.py
[{'list': [], 'name': 'color', 'id': 'blue'}, {'list': ['"Starting_Point"'], 'name': 'rect', 'id': 'A', 'center': (100, 100), 'size': (100, 50)}, {'list': ['"Ending_Point"'], 'name': 'rrect', 'id': 'B', 'ul': (300, 300), 'size': (100, 150), 'color': 'green'}, {'list': [], 'name': 'edge', 'id': 'E', 'from': 'A.lr', 'to': 'B', 'color': 'yellow'}]
['<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />', '<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />', '<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" />']
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" />
</svg>
[15:06:22 gpaci@mac drawing-language]$

[15:22:43 gpaci@mac drawing-language]$ echo -e 'color blue\nrect A "Starting_Point" center 100 100 size 100 50' | python diagram.py
[{'list': [], 'name': 'color', 'id': 'blue'}, {'list': ['"Starting_Point"'], 'name': 'rect', 'id': 'A', 'center': (100, 100), 'size': (100, 50)}]
['<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />']
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />
</svg>
[15:22:53 gpaci@mac drawing-language]$ python diagram.py < input.dgm
<svg width="1000" height="750" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" />
</svg>
[15:23:57 gpaci@mac drawing-language]$ python diagram.py < input.dgm > output.svg
[15:24:04 gpaci@mac drawing-language]$

[15:41:02 gpaci@mac drawing-language]$ python random-graph.py | python diagram.py > randgraph.svg
[15:41:22 gpaci@mac drawing-language]$ # open that image!

[16:24:19 gpaci@mac drawing-language]$ python diagram.py input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" />
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" />
</svg>
[16:27:37 gpaci@mac drawing-language]$

[16:47:00 gpaci@mac drawing-language]$ python diagram.py input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="50" y="100" textLength="95" lengthAdjust="spacingAndGlyphs" fill="black">"Starting_Point"</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="300" y="375" textLength="95" lengthAdjust="spacingAndGlyphs" fill="black">"Ending_Point"</text>
</svg>
[16:48:53 gpaci@mac drawing-language]$

[17:12:37 gpaci@mac drawing-language]$ python diagram.py < input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="50" y="106" textLength="95" lengthAdjust="spacingAndGlyphs" fill="white">"Starting_Point"</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="300" y="381" textLength="95" lengthAdjust="spacingAndGlyphs" fill="black">"Ending_Point"</text>
</svg>
[17:13:14 gpaci@mac drawing-language]$ cat input.dgm
diagram Example width 800 height 600
color blue
rect A "Starting_Point" center 100 100 size 100 50 text-color white
rrect B "Ending_Point" ul 300 300 size 100 150 color green
edge E from A.lr to B color yellow
[17:13:19 gpaci@mac drawing-language]$

[17:20:47 gpaci@mac drawing-language]$ python diagram.py < input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="50" y="106" textLength="95" lengthAdjust="spacingAndGlyphs" fill="white">"Starting_Point"</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="300" y="381" textLength="95" lengthAdjust="spacingAndGlyphs" fill="black">"Ending_Point"</text>
<rect x="250" y="85" width="100" height="70" rx="35.0" ry="35.0" fill="#0080FF" /><text x="250" y="126" textLength="95" lengthAdjust="spacingAndGlyphs" fill="black">Oval</text>
</svg>
[17:21:27 gpaci@mac drawing-language]$

python diagram.py < input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="100" y="106" textLength="95" fill="white" text-anchor="middle" lengthAdjust="spacingAndGlyphs">"Starting_Point"</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="350" y="381" textLength="95" fill="black" text-anchor="middle" lengthAdjust="spacingAndGlyphs">"Ending_Point"</text>
<rect x="250" y="85" width="100" height="70" rx="35.0" ry="35.0" fill="#0080FF" /><text x="300" y="126" textLength="95" fill="black" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<circle cx="200" cy="420" r="50" fill="#FF8000" /><text x="200" y="420" textLength="95" fill="black" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text>
</svg>
[17:52:47 gpaci@mac drawing-language]$

[18:49:40 gpaci@mac drawing-language]$ python diagram.py < input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="100" y="106" textLength="95" fill="white" text-anchor="middle" lengthAdjust="spacingAndGlyphs">"Starting_Point"</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="350" y="381" textLength="95" fill="black" text-anchor="middle" lengthAdjust="spacingAndGlyphs">"Ending_Point"</text>
<rect x="250" y="85" width="100" height="70" rx="35" ry="35" fill="#0080FF" /><text x="300" y="126" textLength="40" fill="black" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<circle cx="200" cy="420" r="50" fill="#FF8000" /><text x="200" y="426" textLength="20" fill="black" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text>
</svg>
[18:54:14 gpaci@mac drawing-language]$

[19:21:31 gpaci@mac drawing-language]$ python diagram.py text-color=gray edge_width=10 < input.dgm
error:
  unknown default: text-color
valid defaults are: color text_color edge_width diagram_width diagram_height font_half_height font_average_width
[19:23:36 gpaci@mac drawing-language]$ python diagram.py text_color=gray edge_width=10 < input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:10" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="100" y="106" textLength="95" fill="white" text-anchor="middle" lengthAdjust="spacingAndGlyphs">"Starting_Point"</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="350" y="381" textLength="95" fill="gray" text-anchor="middle" lengthAdjust="spacingAndGlyphs">"Ending_Point"</text>
<rect x="250" y="85" width="100" height="70" rx="35" ry="35" fill="#0080FF" /><text x="300" y="126" textLength="40" fill="gray" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<circle cx="200" cy="420" r="50" fill="#FF8000" /><text x="200" y="426" textLength="20" fill="gray" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text>
</svg>
[19:23:44 gpaci@mac drawing-language]$

[21:02:52 gpaci@mac drawing-language]$ python diagram.py input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="100" y="106" textLength="95" fill="white" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Starting Point</text>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="350" y="381" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Ending Point</text>
<rect x="250" y="85" width="100" height="70" rx="35" ry="35" fill="#0080FF" /><text x="300" y="126" textLength="40" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<circle cx="200" cy="420" r="50" fill="#FF8000" /><text x="200" y="426" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text>
</svg>
[21:03:36 gpaci@mac drawing-language]$ cat input.dgm
diagram Example width 800 height 600
color blue
rect A "Starting Point" center 100 100 size 100 50 text-color white
rrect B "Ending Point" ul 300 300 size 100 150 color green
oval C Oval center 300 120 size 100 70 color #0080FF
circle CC center 200 420 radius 50 color #FF8000
edge E from A.lr to B color yellow
[21:03:41 gpaci@mac drawing-language]$

[21:26:07 gpaci@mac drawing-language]$ python diagram.py input.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<line x1="100" y1="100" x2="350" y2="375" style="stroke:yellow;stroke-width:3" />
<a xlink:href="https://news.ycombinator.com" xlink:title="click"><rect x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text x="100" y="106" textLength="95" fill="white" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Starting Point</text></a>
<rect x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text x="350" y="381" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Ending Point</text>
<rect x="250" y="85" width="100" height="70" rx="35" ry="35" fill="#0080FF" /><text x="300" y="126" textLength="40" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<a xlink:href="https://www.duckduckgo.com" xlink:title="click"><circle cx="200" cy="420" r="50" fill="#FF8000" /><text x="200" y="426" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text></a>
</svg>
[21:26:44 gpaci@mac drawing-language]$

[23:19:40 gpaci@mac drawing-language]$ cat input-css.dgm
diagram Example width 800 height 600 stylesheet colorful.css
color blue
rect A "Starting Point" center 100 100 size 100 50  url https://news.ycombinator.com  text-color white
rrect B "Ending Point" ul 300 300 size 100 150 color green class "unimportant trivial" text-class unimportant
oval C Oval center 300 120 size 100 70 color #0080FF
circle CC center 200 420 radius 50 color #FF8000 url https://www.duckduckgo.com class important
edge E from A.lr to B color yellow
edge F from B to C class unimportant
[23:19:44 gpaci@mac drawing-language]$ python diagram.py input-css.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="colorful.css" type="text/css" />
<line class="edge" x1="100" y1="100" x2="350" y2="375" stroke="yellow" stroke-width="3" />
<line class="edge unimportant" x1="350" y1="375" x2="300" y2="120" stroke="gray" stroke-width="3" />
<a xlink:href="https://news.ycombinator.com" xlink:title="click"><rect class="node" x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text class="text" x="100" y="106" textLength="95" fill="white" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Starting Point</text></a>
<rect class="node unimportant trivial" x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text class="text unimportant" x="350" y="381" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Ending Point</text>
<rect class="node" x="250" y="85" width="100" height="70" rx="35" ry="35" fill="#0080FF" /><text class="text" x="300" y="126" textLength="40" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<a xlink:href="https://www.duckduckgo.com" xlink:title="click"><circle class="node important" cx="200" cy="420" r="50" fill="#FF8000" /><text class="text" x="200" y="426" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text></a>
</svg>
[23:19:53 gpaci@mac drawing-language]$

[01:01:31 gpaci@mac drawing-language]$ cat input-css.dgm
diagram Example width 800 height 600 stylesheet colorful.css
color blue
rect A "Starting Point" center 100 100 size 100 50  url https://news.ycombinator.com  text-color white
rrect B "Ending Point" ul 300 300 size 100 150 color green class "unimportant trivial" text-class unimportant
oval C Oval center 300 120 size 100 70 color #0080FF
circle CC center 200 420 radius 50 color #FF8000 url https://www.duckduckgo.com class important
edge E from A.lr to B color yellow
edge F from B to C class unimportant
rect Z " " center 100 300 size 50 50
diamond D "I'm a Diamond!" center 100 200  size 100 50 class diamondic
diamond D2 "Another" center 200 200  size 50 50 class diamondic
[01:03:02 gpaci@mac drawing-language]$ python diagram.py input-css.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="colorful.css" type="text/css" />
<line class="edge" x1="100" y1="100" x2="350" y2="375" stroke="yellow" stroke-width="3" />
<line class="edge unimportant" x1="350" y1="375" x2="300" y2="120" stroke="gray" stroke-width="3" />
<a xlink:href="https://news.ycombinator.com" xlink:title="click"><rect class="node" x="50" y="75" width="100" height="50" rx="0" ry="0" fill="blue" /><text class="text" x="100" y="106" textLength="95" fill="white" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Starting Point</text></a>
<rect class="node unimportant trivial" x="300" y="300" width="100" height="150" rx="10" ry="10" fill="green" /><text class="text unimportant" x="350" y="381" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Ending Point</text>
<rect class="node" x="250" y="85" width="100" height="70" rx="35" ry="35" fill="#0080FF" /><text class="text" x="300" y="126" textLength="40" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<a xlink:href="https://www.duckduckgo.com" xlink:title="click"><circle class="node important" cx="200" cy="420" r="50" fill="#FF8000" /><text class="text" x="200" y="426" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text></a>
<rect class="node" x="75" y="275" width="50" height="50" rx="0" ry="0" fill="blue" /><text class="text" x="100" y="306" textLength="10" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs"> </text>
<g transform="translate(100,200)"><polygon class="node diamondic" points="-50 0 0 25 50 0 0 -25" fill="blue" /></g><text class="text" x="100" y="206" textLength="60" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">I'm a Diamond!</text>
<g transform="translate(200,200)"><polygon class="node diamondic" points="-25 0 0 25 25 0 0 -25" fill="blue" /></g><text class="text" x="200" y="206" textLength="30" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Another</text>
</svg>
[01:03:08 gpaci@mac drawing-language]$ # we have diamonds. Finally.

04/10/24 --

[23:15:28 gpaci@mac dialang]$ lf *emb*
-rw-r--r--  1 gpaci  staff  753 Apr 10 23:08 input-pastel-embedded.dgm
[23:15:33 gpaci@mac dialang]$ cat input-pastel-embedded.dgm 
diagram Example width 800 height 600 style pastel
rect L "Just a Label"  center 150 150 size 100 50  class invisible
rect SP "Starting Point" center 100 100 size 100 50  url https://news.ycombinator.com
rrect EP "Ending Point" ul 300 300 size 100 150 class c6 text-class c6
oval Oval center 300 120 size 100 70 class c3 text-class c3
circle CC center 200 420 radius 50 url https://www.duckduckgo.com class c4 text-class c4
edge E from SP.lr to EP class c5 text-class c5
edge F from EP to Oval class thick text-class c4
rect Z " " center 100 300 size 50 50  class c0 text-class c0
diamond D "Shine" center 100 200  size 100 50  class c1 text-class c1
diamond D2 "On" center 200 200  size 50 50  class c5 text-class c5
edge G from D2 to CC class "c2 thin"[23:15:40 gpaci@mac dialang]$ 
[23:16:00 gpaci@mac dialang]$ python diagram.py input-pastel-embedded.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<style>
svg { background-color: white; }

.node { opacity: 1.0; fill: #CCEEFF; stroke: #CCEEFF; stroke-width: 0; }

.text { fill: #5030B0; stroke: #5030B0; font-family: skia,helvetica,sans-serif; }

.edge { stroke-width: 3; fill: #5030B0; stroke: #5030B0; }

.edge.thin { stroke-width: 1; }
.edge.thick { stroke-width: 5; }


.c0 { fill: #5030B0; stroke: #5030B0; }
.c1 { fill: #DDDDFF; stroke: #DDDDFF; }
.c2 { fill: #CCEEFF; stroke: #CCEEFF; }
.c3 { fill: #DDFFDD; stroke: #DDFFDD; }
.c4 { fill: #FFFFCC; stroke: #FFFFCC; }
.c5 { fill: #FFDDFF; stroke: #FFDDFF; }
.c6 { fill: #FFDDBB; stroke: #FFDDBB; }

.text.c0 { fill: #5030B0; stroke: #5030B0; }
.text.c1 { fill: #5030B0; stroke: #5030B0; }
.text.c2 { fill: #5030B0; stroke: #5030B0; }
.text.c3 { fill: #5030B0; stroke: #5030B0; }
.text.c4 { fill: #5030B0; stroke: #5030B0; }
.text.c5 { fill: #5030B0; stroke: #5030B0; }
.text.c6 { fill: #5030B0; stroke: #5030B0; }

/* invisible must be the last class in the sheet: */
.invisible { fill: none; stroke: none; }
</style>

<line class="edge c5" x1="100" y1="100" x2="350" y2="375" stroke="gray" stroke-width="3" />
<line class="edge thick" x1="350" y1="375" x2="300" y2="120" stroke="gray" stroke-width="3" />
<line class="edge c2 thin" x1="200" y1="200" x2="200" y2="420" stroke="gray" stroke-width="3" />
<rect class="node invisible" x="100" y="125" width="100" height="50" rx="0" ry="0" fill="gray" /><text class="text" x="150" y="156" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Just a Label</text>
<a xlink:href="https://news.ycombinator.com" xlink:title="click"><rect class="node" x="50" y="75" width="100" height="50" rx="0" ry="0" fill="gray" /><text class="text" x="100" y="106" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Starting Point</text></a>
<rect class="node c6" x="300" y="300" width="100" height="150" rx="10" ry="10" fill="gray" /><text class="text c6" x="350" y="381" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Ending Point</text>
<rect class="node c3" x="250" y="85" width="100" height="70" rx="35" ry="35" fill="gray" /><text class="text c3" x="300" y="126" textLength="40" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<a xlink:href="https://www.duckduckgo.com" xlink:title="click"><circle class="node c4" cx="200" cy="420" r="50" fill="gray" /><text class="text c4" x="200" y="426" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text></a>
<rect class="node c0" x="75" y="275" width="50" height="50" rx="0" ry="0" fill="gray" /><text class="text c0" x="100" y="306" textLength="10" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs"> </text>
<g transform="translate(100,200)"><polygon class="node c1" points="-50 0 0 25 50 0 0 -25" fill="gray" /></g><text class="text c1" x="100" y="206" textLength="50" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Shine</text>
<g transform="translate(200,200)"><polygon class="node c5" points="-25 0 0 25 25 0 0 -25" fill="gray" /></g><text class="text c5" x="200" y="206" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">On</text>
</svg>
[23:16:20 gpaci@mac dialang]$ lf css/
total 32
-rw-r--r--   1 gpaci  staff    35 Apr  7 22:48 default.css
-rw-r--r--   1 gpaci  staff   507 Apr  8 00:55 colorful.css
-rw-r--r--   1 gpaci  staff   859 Apr 10 22:12 clean.css
-rw-r--r--   1 gpaci  staff  1009 Apr 10 22:26 pastel.css
drwxr-xr-x   6 gpaci  staff   192 Apr 10 22:30 .
drwxr-xr-x  75 gpaci  staff  2400 Apr 10 23:15 ..
[23:16:39 gpaci@mac dialang]$

[15:00:18 gpaci@mac dialang]$ cat input-label-clean.dgm
diagram Example width 800 height 600 stylesheet clean.css
rect L "Just a Label"  center 150 150 size 100 50  class invisible
rect SP "Starting Point" center 100 100 size 100 50  url https://news.ycombinator.com class c2 text-class c2
rrect EP "Ending Point" ul 300 300 size 100 150 class c2 text-class c2
oval Oval center 300 120 size 100 70 class c3 text-class c3
circle CC center 200 420 radius 50 url https://www.duckduckgo.com class c4 text-class c4
edge E from SP.lr to EP class c5 text-class c5
edge F from EP to Oval class thick text-class c4
rect Z " " center 100 300 size 50 50  class c0 text-class c0
diamond D "Shine" center 100 200  size 100 50  class c1 text-class c1
diamond D2 "On" center 200 200  size 50 50  class c1 text-class c1
edge G from D2 to CC class "c2 thin"
[15:00:30 gpaci@mac dialang]$

$ date
Sat Apr 13 14:59:54 EDT 2024
[14:59:54 gpaci@mac ~]$

[15:08:06 gpaci@mac dialang]$ python diagram.py input-label-clean.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="clean.css" type="text/css" />
<line id="E" class="edge c5" x1="100" y1="100" x2="350" y2="375" stroke="gray" stroke-width="3" />
<line id="F" class="edge thick" x1="350" y1="375" x2="300" y2="120" stroke="gray" stroke-width="3" />
<line id="G" class="edge c2 thin" x1="200" y1="200" x2="200" y2="420" stroke="gray" stroke-width="3" />
<rect id="L" class="node invisible" x="100" y="125" width="100" height="50" rx="0" ry="0" fill="gray" /><text id="L-label" class="text" x="150" y="156" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Just a Label</text>
<a xlink:href="https://news.ycombinator.com" xlink:title="click"><rect id="SP" class="node c2" x="50" y="75" width="100" height="50" rx="0" ry="0" fill="gray" /><text id="SP-label" class="text c2" x="100" y="106" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Starting Point</text></a>
<rect id="EP" class="node c2" x="300" y="300" width="100" height="150" rx="10" ry="10" fill="gray" /><text id="EP-label" class="text c2" x="350" y="381" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Ending Point</text>
<rect id="Oval" class="node c3" x="250" y="85" width="100" height="70" rx="35" ry="35" fill="gray" /><text id="Oval-label" class="text c3" x="300" y="126" textLength="40" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Oval</text>
<a xlink:href="https://www.duckduckgo.com" xlink:title="click"><circle id="CC" class="node c4" cx="200" cy="420" r="50" fill="gray" /><text id="CC-label" class="text c4" x="200" y="426" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">CC</text></a>
<rect id="Z" class="node c0" x="75" y="275" width="50" height="50" rx="0" ry="0" fill="gray" /><text id="Z-label" class="text c0" x="100" y="306" textLength="10" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs"> </text>
<g transform="translate(100,200)"><polygon id="D" class="node c1" points="-50 0 0 25 50 0 0 -25" fill="gray" /></g><text id="D-label" class="text c1" x="100" y="206" textLength="50" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Shine</text>
<g transform="translate(200,200)"><polygon id="D2" class="node c1" points="-25 0 0 25 25 0 0 -25" fill="gray" /></g><text id="D2-label" class="text c1" x="200" y="206" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">On</text>
</svg>
[15:08:43 gpaci@mac dialang]$


[20:57:13 gpaci@mac dialang]$ cat many-edges-rects.dgm
diagram Many-edges width 800 height 600 stylesheet css/clean.css
rect C "Center" center 400 300 size 100 100 class c2
rect R1 "#1" center 600 300 size 100 60  color #0000FF40
rect R2 "#2" center 600 200 size 100 60  color #00FFFF40
rect R3 "#3" center 100 100 size 100 62  color #00FF0040
rect R4 "#4" center 500 60 size 100 60  color #FFFF0040
rect R5 "#5" center 390 100 size 100 60  color #FF000040
rect R6 "#6" center 100 500 size 100 60  color #FF00FF40
edge a1 from C to R1
edge a2 from C to R2
edge a3 from C to R3
edge a4 from C to R4
edge a5 from C to R5
edge a6 from C to R6
[20:57:37 gpaci@mac dialang]$ python diagram.py many-edges-rects.dgm
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="css/clean.css" type="text/css" />
<line id="a1" class="edge" x1="400" y1="300" x2="545" y2="300" stroke="gray" stroke-width="3" />
<g transform="translate(550,300) rotate(0)"><polygon id="a1-he" class="edge " points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<line id="a2" class="edge" x1="400" y1="300" x2="545.469084" y2="232.114427" stroke="gray" stroke-width="3" />
<g transform="translate(550,230) rotate(-26.565051)"><polygon id="a2-he" class="edge " points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<line id="a3" class="edge" x1="400" y1="300" x2="154.142322" y2="133.800209" stroke="gray" stroke-width="3" />
<g transform="translate(150,131) rotate(-146.309932)"><polygon id="a3-he" class="edge " points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<line id="a4" class="edge" x1="400" y1="300" x2="448.841897" y2="94.864031" stroke="gray" stroke-width="3" />
<g transform="translate(450,90) rotate(-67.380135)"><polygon id="a4-he" class="edge " points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<line id="a5" class="edge" x1="400" y1="300" x2="390.293610" y2="134.991372" stroke="gray" stroke-width="3" />
<g transform="translate(390,130) rotate(-92.862405)"><polygon id="a5-he" class="edge " points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<line id="a6" class="edge" x1="400" y1="300" x2="154.134633" y2="467.188450" stroke="gray" stroke-width="3" />
<g transform="translate(150,470) rotate(146.309932)"><polygon id="a6-he" class="edge " points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<rect id="C" class="node c2" x="350" y="250" width="100" height="100" rx="0" ry="0" fill="gray" /><text id="C-label" class="text" x="400" y="306" textLength="60" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Center</text>
<rect id="R1" class="node" x="550" y="270" width="100" height="60" rx="0" ry="0" fill="#0000FF40" /><text id="R1-label" class="text" x="600" y="306" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">#1</text>
<rect id="R2" class="node" x="550" y="170" width="100" height="60" rx="0" ry="0" fill="#00FFFF40" /><text id="R2-label" class="text" x="600" y="206" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">#2</text>
<rect id="R3" class="node" x="50" y="69" width="100" height="62" rx="0" ry="0" fill="#00FF0040" /><text id="R3-label" class="text" x="100" y="106" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">#3</text>
<rect id="R4" class="node" x="450" y="30" width="100" height="60" rx="0" ry="0" fill="#FFFF0040" /><text id="R4-label" class="text" x="500" y="66" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">#4</text>
<rect id="R5" class="node" x="340" y="70" width="100" height="60" rx="0" ry="0" fill="#FF000040" /><text id="R5-label" class="text" x="390" y="106" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">#5</text>
<rect id="R6" class="node" x="50" y="470" width="100" height="60" rx="0" ry="0" fill="#FF00FF40" /><text id="R6-label" class="text" x="100" y="506" textLength="20" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">#6</text>
</svg>
[20:57:46 gpaci@mac dialang]$

04/24/24 --

"dashed" and "dotted" classes for edges if supported by the stylesheet, and "nohover":

[23:13:54 gpaci@mac dialang]$ cat examples/backdrop3.dgm
diagram Backdrop width 800 height 600 stylesheet ../css/clean3.css
# Put this rect (and its label) below where edges are:
rect B "Backdrop" z -1 ul 0 0 size 800 600 class "c3 nohover"
# These don't specify z, so it's 1, because they're nodes:
rect A "foreground 1" ul 100 100 size 100 60 class c2
rect C "foreground 2" ul 500 350 size 100 60 class c1 text-class c1
rect D "foreground 3" ul 100 350 size 100 60 class c4 text-class c4
# this edge is behind everything except the backdrop, B:
# (it doesn't specify a z, so it's 0, because it's an edge)
edge e1 from A to C class "c4 dotted"
# this edge is in front of everything else, even A:
edge e2 from A to D z 2 class "c2 dashed"
[23:19:37 gpaci@mac dialang]$ cat op/backdrop3.svg
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<!-- generated by https://github.com/gpacix/dialang; source for this diagram:
diagram Backdrop width 800 height 600 stylesheet ../css/clean3.css
# Put this rect (and its label) below where edges are:
rect B "Backdrop" z -1 ul 0 0 size 800 600 class "c3 nohover"
# These don't specify z, so it's 1, because they're nodes:
rect A "foreground 1" ul 100 100 size 100 60 class c2
rect C "foreground 2" ul 500 350 size 100 60 class c1 text-class c1
rect D "foreground 3" ul 100 350 size 100 60 class c4 text-class c4
# this edge is behind everything except the backdrop, B:
# (it doesn't specify a z, so it's 0, because it's an edge)
edge e1 from A to C class "c4 dotted"
# this edge is in front of everything else, even A:
edge e2 from A to D z 2 class "c2 dashed"
-->
<link xmlns="http://www.w3.org/1999/xhtml" rel="stylesheet" href="../css/clean3.css" type="text/css" />
<rect id="B" class="node  c3 nohover" x="0" y="0" width="800" height="600" rx="0" ry="0" fill="gray" /><text id="B-label" class="text " x="400" y="306" textLength="80" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">Backdrop</text>
<line id="e1" class="edge  c4 dotted" x1="150" y1="130" x2="495.766817" y2="347.339142" stroke="gray" stroke-width="3" />
<g transform="translate(500,350) rotate(32.005383)"><polygon id="e1-he" class="arrowhead  c4 dotted" points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
<rect id="A" class="node  c2" x="100" y="100" width="100" height="60" rx="0" ry="0" fill="gray" /><text id="A-label" class="text " x="150" y="136" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">foreground 1</text>
<rect id="C" class="node  c1" x="500" y="350" width="100" height="60" rx="0" ry="0" fill="gray" /><text id="C-label" class="text  c1" x="550" y="386" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">foreground 2</text>
<rect id="D" class="node  c4" x="100" y="350" width="100" height="60" rx="0" ry="0" fill="gray" /><text id="D-label" class="text  c4" x="150" y="386" textLength="95" fill="black" font-family="helvetica,arial,sans-serif" text-anchor="middle" lengthAdjust="spacingAndGlyphs">foreground 3</text>
<line id="e2" class="edge  c2 dashed" x1="150" y1="130" x2="150" y2="345" stroke="gray" stroke-width="3" />
<g transform="translate(150,350) rotate(90)"><polygon id="e2-he" class="arrowhead  c2 dashed" points="-20 0 -20 -10 0 0 -20 10" fill="gray" /></g>
</svg>
[23:19:54 gpaci@mac dialang]$