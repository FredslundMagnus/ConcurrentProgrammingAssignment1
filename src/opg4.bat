FOR %%A IN (1,2,4,8,16) DO FOR %%B IN (10,100,1000) DO java Search -W 10 -R 100 Chromosome.txt "ATATGTTTT" %%B %%A >> ../data/Problem4/threads-%%A-batch-%%B.txt