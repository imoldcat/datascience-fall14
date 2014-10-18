cat cmsc.txt | awk '/^CMSC/ {course = $0}
	 /^[0-9]+/ {section=$0}
	 /^[a-zA-Z.:]+ [a-zA-Z.:]+/ {gsub(" $",""); teacher=$0;}
	 /: [0-9]+/ {seat=substr($3,1,length($3)-1); open=substr($5,1,length($5)-1); wait=substr($7,1,length($7)-1);}
	 /[a-zA-Z]+ [0-9]+:[0-9]/ {date=$1; time=$2$3$4;}
	 /^[A-Z]+  [0-9]+$/ {bldg=$1; room=$2; print course", "section", "teacher", "seat", "open", "wait", "date", "time", "bldg", "room;}
	 '