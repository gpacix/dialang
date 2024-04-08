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
