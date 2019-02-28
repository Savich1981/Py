def collatz(n):

    seq = []
    seq.append(n)

    while n > 1:

     if n % 2 != 0:

      n = int(n * 3) + 1
      seq.append(n)

     else:

      n = int(n/2)
      seq.append(n)

    if len(seq) < seq[ 0 ]:
     return len(seq)

    else:

     return seq[ 1 ]
