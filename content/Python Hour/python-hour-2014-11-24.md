Title: Python Hour - 24 November 2014
Slug: python-hour-2014-11-24
Date: 2014-11-24 11:00 UTC-07:00
Tags: teaching python, 2-D interpolation
Summary: Summary of PyHOGs meeting on November 24, 2014
Author: Earle Wilson

### Meeting Summary

Attendance: Parker M., Michelle W. and Earle W.

For most of the meeting, the group discussed some strategies for introducing Python in the classroom. Parker motivated the discussion by sharing his plans for using Python in his Puget Sound oceanography course, which he will offer next quarter. The challenge he outlined is getting students to use Python to explore data and model output without letting that experience detract from the main objectives of the course.


Michelle advised that a few hands-on instructional sessions will be necessary. Earle supported this idea and suggested borrowing some ideas from the [Software Carpentry](http://software-carpentry.org/) teaching lab, in particular the strategy of introducing instructive yet interesting examples that students will find immediately useful. Everyone seemed to agree that teaching the fundamentals of the language, without providing interesting applications, will not be the best use of time and will likely disengage students. In other words, 

	:::python
	def foobar():
		print "Hello World. We promise to come up with a better example."

Parker asked about how to interpolate from one 2-D plaid grid to another. Earle suggested using the [scipy.interpolate.interp2d](http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.interp2d.html) function.

