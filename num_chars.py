# Write code to count the number of characters in original_str using the accumulation pattern and assign 
# the answer to a variable num_chars
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars=0
for i in range(len(original_str)):
    num_chars=num_chars+1
print(num_chars)

