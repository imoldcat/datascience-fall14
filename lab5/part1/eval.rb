require 'pp'
require 'set'

results = %x(cut -f 1,2,3 -d , products_out.csv)

pairs =  {}
results.split.map do |x| 
	cid, source, id = x.split(',') 
	pairs[cid] ||= {}
	# groups the ids in a cluster into two while parsing
	pairs[cid][source] ||= [] 
	pairs[cid][source] << id 
end

result = Set.new
pairs.keys.each do |cid|
	# only one source cluster
	next if pairs[cid].size < 2
	# cartersian product the two id groups
	pairs[cid]['amazon'].each do |a_id|
		pairs[cid]['google'].each do |g_id|
			result << "\"#{a_id}\",\"#{g_id}\""
		end
	end
end

puts "found pairs: #{result.size}"

ground = Set.new
open("product_mapping.csv") do |file|
	file.each_line do |line|
		next if file.lineno < 2 
		ground << line.strip
	end
end

precision = (result.intersection ground).size.to_f / result.size.to_f
recall = (result.intersection ground).size.to_f / ground.size.to_f


puts "precision: #{precision}"
puts "recall: #{recall}"
