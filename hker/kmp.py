data=raw_input().strip()
pattern=raw_input().strip()
def kmp_table(pattern):
	kmp_failure_function=[0]*len(pattern)
	i=1
	j=0
	m=len(pattern)
	while i<m:
		if pattern[i]==pattern[j]:
			j=j+1
			kmp_failure_function[i]=j
			i=i+1
		else:
			if j!=0:
				j=kmp_failure_function[j-1]
			else:
				kmp_failure_function[i]=0
				i=i+1
	return kmp_failure_function
print kmp_table(pattern)

		