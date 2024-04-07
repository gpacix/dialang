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
