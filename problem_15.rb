#!/usr/bin/ruby

def countPaths
	a = Array.new(21) {Array.new(21, 0)}
	for x in 0...21
		a[0][x] = 1
		a[x][0] = 1
	end

	for x in 1...21
		for y in 1...21
			a[x][y] = a[x - 1][y] + a[x][y - 1]
		end
	end
	return a
end

for x in countPaths
	print "#{x} \n"
end