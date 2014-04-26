#!/usr/bin/ruby

def fibonacci
	fib = Array[1, 1]
	while (fib[-1].to_s).length < 1000
		fib << fib[-1] + fib[-2]
	end
	return fib.length
end

puts fibonacci