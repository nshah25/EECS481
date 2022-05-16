import sys
import os


def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def DD(P, C, command):
	# if n = 1 then return {c1} 
	if len(C) == 1:
		return C
	# let P1 = {c1, … cn/2}
	P1 = C[:int(len(C)/2)]
	# let P2 = {cn/2+1, …, cn}
	P2 = C[int(len(C)/2):]
	# if Interesting(P u P1) = Yes then return DD(P,P1)
	full_command = command
	for num in Union(P, P1):
		full_command += " " + str(num)
	if os.system(full_command) != 0:
		return DD(P,P1, command)

	# if Interesting(P u P2) = Yes then return DD(P,P2)
	full_command = command
	for num in Union(P, P2):
		full_command += " " + str(num)
	# print(full_command)
	if os.system(full_command) != 0:
		return DD(P,P2, command)

	# else return DD(P u P2, P1) u DD(P u P1, P2)
	return Union(DD(Union(P, P2), P1, command), DD(Union(P, P1), P2, command))


n = int(sys.argv[1])
n_list = [i for i in range(n)]

command = ""
for i in range(2,len(sys.argv)):
	command += sys.argv[i] + " "
command = command[:-1]
out = DD([], n_list, command)
out.sort()
print(out)




