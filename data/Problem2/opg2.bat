javac Search.java
FOR %%A IN (10, 50, 100) DO java Search -W 10 -R 100 Chromosome.txt ATATGTTTT %%A >> tasks-%%A.txt