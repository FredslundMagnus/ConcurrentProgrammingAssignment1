javac Search.java
FOR %%A IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 300, 400, 1000, 10000) DO java Search -W 10 -R 100 Chromosome.txt ATATGTTTT %%A >> tasks-%%A.txt

wsl
grep -r --include=*.{txt} "Average speedup:" . > all.txt