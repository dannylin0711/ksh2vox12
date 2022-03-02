# ksh2vox12
Convert Kshootmania chart into VOX version 12

KSH File format specification: https://github.com/m4saka/ksh/blob/master/ksh_format.md

# Special
Biggest difference between vox 10 and 12 is how the laser position is represented. Vox10 uses 0-127 int, in Vox12 it's float value, which is much more accurate and precise, and this also brings the ability to make 1/64 lasers(The chart system is revamped in the game). 

## Perfect Curve
By convert perfect curve, using the comment system in ksh editor, adding "cstart" to the beginning of the laser start, and adding "cend" at where you want to stop the curve processing. Please do not add other comments while using this tool, it may cause unexpected errors. Currently the curve is always calculated using sin and cos, and doesn't contain any curve specifications, all 
```
--
//cstart
0011|00|b-
0000|00|:-
0000|00|0-
0000|00|:-
0000|00|b-
//cend
--
```

## Lane Splitting
The function is already implemented in kshoot, which is *center_split* keyword, use it for lane splitting.
```
--
//lane split effect
center_split=0	
center_split=125
zoom_top=30
zoom_bottom=0
0000|00|PP
0000|00|--
--
```

## Post Effect
In the recent version of Exceed Gear introduced the post effect system, there five effects you can apply, todo.
