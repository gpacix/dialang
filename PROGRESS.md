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
