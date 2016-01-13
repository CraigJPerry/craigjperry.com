Title: My First 3D Design
Date: 2016-01-09 19:41
Category: 3D Printing
Tags: 3d-printing, lulzbot-mini, quadcopters, rc-aircraft, remote-control, emax-nighthawk-280
Slug: my-first-3d-design
Authors: Craig J Perry
Summary: Designing and Printing A Protective Underplate For an EMAX Nighthawk 280 Pro

The [EMAX Nighthawk Pro 280](http://www.emaxmodel.com/nighthawk-pro-280.html)
racing quadcopter has its power distribution & control board
exposed underneath the quad. It is conformally coated but that's
not enough so I designed and 3D printed a protective underplate.

## Measuring Up

I traced the outline of the power distribution board (PDB) on
paper. Then i added some straight lines to make measuring the
odd shape easier.

## OpenSCAD

I've been playing with SketchUp, 123Design and OpenSCAD. I chose
the latter here since this job is mostly transferring some
measurements to CAD and adding a couple of small design ideas.

[underplate.scad](https://github.com/CraigJPerry/Nighthawk280ProtectionKit/blob/master/underplate.scad)

It's been ages since i wrote code in a procedural language. Having
dependencies on global variables feels so wrong! I'll need to read
up some idiomatic OpenSCAD examples, i see it comes with a fair
library.

Talking of old knowledge, it's been ages since i had to do any
geometry. I had to google Pythagoras because i forgot to take
the square root but i got my arctangent trig problem first time
off the top of my head. I'll happily take that.

## Sharing The Design

I exported an STL of the finished design, which github knows
how to render so you can view it in your browser which is cool!

[underplate.stl](https://github.com/CraigJPerry/Nighthawk280ProtectionKit/blob/master/underplate.stl)

Now to finally create a thingiverse account after free-loading
so many things from there!

## What Did I Learn?

3D Printing may be consumer level tech nowadays but designing
for manufacture is still hard. Taking accurate measurements of
fiddly shapes is tricky, i need to learn some more in that space.

Getting my prints to come out at the sizes i requested is easier
than expected but that's thanks to the Lulzbot guys. I have had
to adjust the filament size in Cura a few times. The diameter
seems to change by +/- 0.3mm every metre or so. 10% is a lot to
my mind.

ABS is tough, really tough. HIPS is also tough enough for this
application while being cheaper and lighter but it's definitely
more brittle and inter-layer adhesion isn't quite as good as ABS.





