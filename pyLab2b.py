def rev_words(string):
	words=list(string.split(' '))
	ra=[]
	for w in words:
		ra.insert(0,w)
	#print(ra)
	return ' '.join(ra)
	
def rev_letters(string):
	 words=list(string.split(' '))
	 rev_arr=[w[::-1] for w in words]
	 return " ".join(rev_arr)
	 
string=input("enter a sentence: ")
print('Reversed words: ', rev_words(string))
print('Reversed letters: ', rev_letters(string)) 
