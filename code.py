import random

f=open("sequence.fasta","r")
genome=f.readlines()
seq1=""
for n in range(1,len(genome)):
    s=genome[n].rstrip()
    seq1= seq1+s
    
print("The nucleotide sequence is",seq1)
print("The length of the genome sequence is",len(seq1))
print()                                    

def kmer_finder(seq,k):  
  n=k-1
  kmer=[]
  for i in range(len(seq)-n):
    dat=seq[i:i+k]
    kmer.append(dat)
  return(kmer)

seqfi=[]
roll_list=[1]                         ## Starting index , input a list of different numbers to find kmers for different start positions
for roll in roll_list:
  print('For first 15 neucleotides,')
  s=seq1[roll:roll+15]                ## Chnage the length of sequence by adjusting this line
  print('The sequence is :',s)
  seqf=kmer_finder(s,3)
  seqfi=[]
  for j in seqf:
    seqfi.append(j)
  seqfi.sort()
  print('The 3-mers for the sequence are :',seqfi)

  #---

  t=0
  d=0
  c=1
  i=0
  g=[]
  u=1
  o=0
  m=0
  x=1

  while m<x:
   
    seq = []
    for j in seqfi:
      seq.append(j)
    seq.sort()
    x=len(seq)
    k=len(seq[0])
    for kmer in seq:
      
      seq = []
      for j in seqfi:
        seq.append(j)
      a=kmer
      seq[seq.index(a)] ='b'
      
      
      while True:
        i=i+1
        t=t+1
        p=random.choice(seq)
        q=p[:k-1]
        b=a[c:]
        
        if (b==q):
          q=p[k-1]
          a=a+q
          c=c+1
          seq.remove(p)
        
        if(i>x*10):
          i=0
          c=1
          p=''
          q=''
          
          seq = []
          for j in seqfi:
            seq.append(j)
          a=kmer
          seq.remove(kmer)

        if(t>x*100):
          t=0
          c=1
          p=''
          q=''
          break
          
        if(len(a)==x+2):
          g.append(a)
          c=1
          i=0
          break
    m=m+1
  final=[]
  print('')
  final=list(set(g))
  ab=1
  for ele in final:
    print('Longest -',ab,ele)
    ab=ab+1
  print('')
  print('################################################')
  print('')
