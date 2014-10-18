cat worldcup.txt | sed 's/-/\n/g' | awk '/fb\|/ {split($0,a,"{"); country=substr(a[3],4,3);rank=0}
	 /(sort dash)|\|[1-4]/ {
	 		rank=rank+1; 
		 	if(rank < 5) {
		 		if (match($0, /[0-9]+/)) {
		 			size = split($0, yh, "]");
		 			for (i = 1; i <= size; i++)
		 				if (match(yh[i], /\|[0-9]+/))
				 			print country", "rank", "substr(yh[i],length(yh[i])-3,4);
			 	}
		 	}
	 	}
	 '