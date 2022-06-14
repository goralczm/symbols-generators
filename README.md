# Symbols Generator
This script was made just for fun in my free time
<ul>
	<li>Generates all sort of pyramids including ones based on width, height, one sided and reverse ones</li>
	<li>Generates black hole containing symbols more dense towards center of black hole</li>
	<li>Generates tree with trunk and leaves more dense towards tree crown</li>
</ul>

# Requirements
<ul>
	<li> 3.9.4</li>
</ul>

# Installation
<ol>
	<li>
		Download repository
		<br>
		<pre>git clone https://github.com/goralczm/symbols-generators</pre>
	</li>
</ol>

# Functions
<ul>
	<li>
		<b>OneSidePyramid(height, inverse=False, symbol='#')</b> - prints rows containg number of 'symbol' in shape of one sided pyramid
		<br>
		<ul>
			<li>height - integer with pyramid height</li>
			<li>inverse - optional boolean variable, determines if pyramid should be printed inverse or not</li>
			<li>symbol - optional string variable, if not assigned- default value is hashtag ('#'), contains symbol which should be pyramid printed with</li>
		</ul>
		<br>

		```
		OneSidePyramid(3)<br>#<br>##<br>###
		```

	</li>
	<li>
		<b>PyramidBasedWidth(width, symbol='#', background=' ')</b> - prints pyramid of given width
		<br>
		<ul>
			<li>width - integer with pyramid width</li>
			<li>symbol - optional string variable, if not assigned- default value is hashtag ('#'), contains symbol which should be pyramid printed with</li>
			<li>background - optional string variable, if not assigned- default value is space (' '), contains symbol which should be pyramids background printed with</li>
		</ul>
		<br>
		
		```
		PyramidBasedWidth(5, '&')<br>  &  <br> &&& <br>&&&&&
		```

	</li>
	<li>
		<b>PyramidBasedHeight(height, inverse=False, symbol='#', background=' ')</b> - prints pyramid of given height
		<br>
		<ul>
			<li>height - integer with pyramid height</li>
			<li>inverse - optional boolean variable, determines if pyramid should be printed inverse or not</li>
			<li>symbol - optional string variable, if not assigned- default value is hashtag ('#'), contains symbol which should be pyramid printed with</li>
			<li>background - optional string variable, if not assigned- default value is space (' '), contains symbol which should be pyramids background printed with</li>
		</ul>
		<br>

		```
		PyramidBasedHeight(5, True, '%')<br>%%%%%%%%%<br> %%%%%%% <br>  %%%%%  <br>   %%%   <br>    %    
		```

	</li>
	<li>
		<b>BlackHole(width, height, density=4, tolerance=4, rejection=0, mode='diamond', offset=[0, 0], symbol='#', background=' ')</b> - generates txt file containing generated black hole
		<br>
		<ul>
			<li>width - integer with black hole width</li>
			<li>height - integer with black hole height</li>
			<li>density - optional integer/float value, if not assigned- default value is 4, determines how dense black hole should be</li>
			<li>tolerance - optional integer/float value, if not assigned- default value is 4, determines how much of outer symbols should be generated</li>
			<li>rejection - optional integer value, if not assigned- default value is 0 (value of 0 means disabled, other bigger than 0 is enabled), determines percentage of how many symbols should not be generated</li>
			<li>mode='diamond' - optional string value (available are 'diamond' and 'circle'), if not assigned- default value is diamond, determines type of calculating distance from center for each 'pixel' from which is generating system based of</li>
			<li>offset - optional list value, if not assigned- default value is [0, 0], moves center of black hole 'offset[0]' 'pixels' left and 'offset[1]' 'pixels' top</li>
			<li>symbol - optional string variable, if not assigned- default value is hashtag ('#'), contains symbol which should be pyramid printed with</li>
			<li>background - optional string variable, if not assigned- default value is space (' '), contains symbol which should be pyramids background printed with</li>
		</ul>
		<br>
		
		```
		BlackHole(128, 128, 4, 3, 1, 'circle')<br>#output visible in 'black_hole.txt' file
		```

	</li>
	<li>
		<b>Tree(gridSize, density=4, tolerance=4, rejection=0, mode='diamond', symbol='#', background=' ')</b> - generates txt file containig generated tree
		<br>
		<ul>
			<li>gridSize - integer with tree 'image' size</li>
			<li>density - optional integer/float value, if not assigned- default value is 4, determines how dense black hole should be</li>
			<li>tolerance - optional integer/float value, if not assigned- default value is 4, determines how much of outer symbols should be generated</li>
			<li>rejection - optional integer value, if not assigned- default value is 0 (value of 0 means disabled, other bigger than 0 is enabled), determines percentage of how many symbols should not be generated</li>
			<li>mode='diamond' - optional string value (available are 'diamond' and 'circle'), if not assigned- default value is diamond, determines type of calculating distance from center for each 'pixel' from which is generating system based of</li>
			<li>offset - optional list value, if not assigned- default value is [0, 0], moves center of black hole 'offset[0]' 'pixels' left and 'offset[1]' 'pixels' top</li>
			<li>symbol - optional string variable, if not assigned- default value is hashtag ('#'), contains symbol which should be pyramid printed with</li>
			<li>background - optional string variable, if not assigned- default value is space (' '), contains symbol which should be pyramids background printed with</li>
		</ul>
		<br>
		
		```
		Tree(128, 2, 3.5, 2, 'circle')<br>#output visible in 'tree.txt' file
		```
	</li>
</ul>