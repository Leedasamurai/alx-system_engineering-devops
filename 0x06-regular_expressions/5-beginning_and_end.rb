#!/usr/bin/env ruby
# The regular expression must start with h and end with n

puts ARGV[0].scan(/h.n/).join
