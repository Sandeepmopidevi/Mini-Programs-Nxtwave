full_str=input()
subseq=input()
subseq_ind=0
subseq_len=len(subseq)

for char in full_str:
    if char==subseq[subseq_ind]:
        subseq_ind+=1
        if subseq_ind==subseq_len:
            break
if subseq_ind==subseq_len:
    print("Yes")
else:
    print("No")
