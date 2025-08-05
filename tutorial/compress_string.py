a = "aabcccccaaa"
for i in a:
   print(a.count(i),end="")

print("\n")
for i in a:
   if i in a:
      print(i,end="")

c=""
print("\n")
for i in a:
   if i not in c:
      c+= i
      c += str(a.count(i))
print("c:",c)

# Function for 
print("\n")
def compress_string(z):
  k=""
  l=0
  for i in z:
   if i not in k:
      k+= i
      k += str(z.count(i))
      for i in k:
         l+= k.count(i)
         if len(k) == l:
            k=z
         
  print("k",k)
    
     

compress_string("aaabbccc")  # Output: "a3b2c3"
compress_string("abc")       # Output: "abc" (compressed is "a1b1c1" → not shorter)
compress_string("aabb")      # Output: "aabb"
compress_string("aabcccccaaa")  # Output: "a2b1c5a3"
