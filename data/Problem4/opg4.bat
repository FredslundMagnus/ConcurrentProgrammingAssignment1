javac Search.java
FOR %%A IN (1,2,4,8,16) DO FOR %%B IN (10,100,1000) DO java Search -W 10 -R 100 Chromosome.txt "ATATGTTTT" %%B %%A >> threads-%%A-tasks-%%B.txt

wsl
grep -r --include=*.{txt} "Average speedup:" . > all.txt