FOR %%A IN (20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 300, 400, 1000) DO java Search -W 10 -R 100 Chromosome.txt A %%A >> ../data/Problem3/batch-%%A.txt