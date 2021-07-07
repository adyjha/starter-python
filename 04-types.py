# 1 string
# we use back slash before quotation. this is called espcaping. 
ady='He said,"aren\'t you going to school today"?'
print(ady)
# To use more than 1 line of text in string we use 3 single quote.
ayu='''I am not going to school today. 
I will go to shopping mall with dad.'''
print(ayu)
# We use %s to embed a string variable
TotalScore=100
MyScore=90 
message='I scored %s out of %s'
print(message % (MyScore,TotalScore))
# Multiplying strings
print(10 * 'a')
print(9 * 'Ady is the best')