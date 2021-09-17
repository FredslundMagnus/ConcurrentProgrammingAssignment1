import matplotlib.pyplot as plt
# data_uden_warmup = [0.212975, 0.174472, 0.152527, 0.143930, 0.151221, 0.158211, 0.052915, 0.056080, 0.174958, 0.035867, 0.035641, 0.198618, 0.036725, 0.036281, 0.164042, 0.035632, 0.035314, 0.252750, 0.054047, 0.055133, 0.054456, 0.270833, 0.035526, 0.035689, 0.035712, 0.295864, 0.036604, 0.036659, 0.036165, 0.253618, 0.035586, 0.035273, 0.035436, 0.228434, 0.087285, 0.069701, 0.076515, 0.291319, 0.035509, 0.035267, 0.036243, 0.035281, 0.226859, 0.035588, 0.036879, 0.036349, 0.035470, 0.232586, 0.037855, 0.036242, 0.035504, 0.181810, 0.071426, 0.060176, 0.056568, 0.059156, 0.169686, 0.035356, 0.035713, 0.036220, 0.035240, 0.143114, 0.035612, 0.036310, 0.036103, 0.036290, 0.178495, 0.036316, 0.035474, 0.035189, 0.034996, 0.184261, 0.054259, 0.054409, 0.055066, 0.055134, 0.194244, 0.035546, 0.035313, 0.035770, 0.035252, 0.036234, 0.156307, 0.035343, 0.035610, 0.035480, 0.035948, 0.035123, 0.197573, 0.035245, 0.035861, 0.035846, 0.035458, 0.163210, 0.054041, 0.055246, 0.054969, 0.039240, 0.035314, 0.035199]

# [0.210100, 0.172824, 0.149149, 0.151445, 0.142680, 0.150652, 0.053695, 0.056129, 0.168423, 0.037253, 0.036286, 0.171982, 0.036208, 0.036222, 0.171257, 0.056967, 0.036649, 0.217195, 0.055091, 0.053870, 0.053299, 0.286071, 0.035918, 0.037440, 0.036495, 0.261881, 0.037560, 0.037376, 0.036053, 0.290983, 0.036354, 0.035871, 0.035481, 0.203407, 0.052571, 0.053533, 0.054489, 0.167781, 0.036436, 0.036772, 0.036935, 0.035957, 0.190683, 0.036152, 0.035891, 0.036830, 0.036258, 0.227145, 0.035952, 0.036318, 0.036275, 0.151808, 0.060970, 0.055316, 0.058087, 0.057695, 0.211721, 0.039244, 0.036892, 0.035931, 0.037262, 0.160350, 0.038508, 0.036512, 0.037072, 0.035943, 0.151582, 0.040458, 0.036614, 0.037194, 0.036993, 0.036881, 0.229521, 0.057788, 0.056169, 0.058197, 0.059052, 0.196557, 0.038524, 0.035811, 0.035263, 0.036998, 0.164132, 0.036222, 0.036597, 0.037418, 0.036185, 0.290315, 0.037162, 0.036350, 0.036866, 0.037596, 0.186488, 0.058778, 0.055962, 0.057152, 0.037378, 0.036189, 0.154922, 0.038006]

data_uden_warmup = [0.071208, 0.076072, 0.036135, 0.035931, 0.035929, 0.035828, 0.035991, 0.035846, 0.035779, 0.035838, 0.036056, 0.036857, 0.036987, 0.036890, 0.036483, 0.036633, 0.036615, 0.037141, 0.038525, 0.036773, 0.036768, 0.036673, 0.036252, 0.035837, 0.035794, 0.036264, 0.036982, 0.036272, 0.036628, 0.036643, 0.036748, 0.037149, 0.036687, 0.036746, 0.036709, 0.037203, 0.036690, 0.036668, 0.036770, 0.036769, 0.036644, 0.036698, 0.036764, 0.036710, 0.036658, 0.036709, 0.036670, 0.036729, 0.036689, 0.036458, 0.035901, 0.036006, 0.035976, 0.035764, 0.035764, 0.035720, 0.035725, 0.035958, 0.035889, 0.035927, 0.035953, 0.035869, 0.035876, 0.035947, 0.035793, 0.035762, 0.035836, 0.035747, 0.035723, 0.035709, 0.035752, 0.035680, 0.035724, 0.035736, 0.035786, 0.035718, 0.035803, 0.035856, 0.035937, 0.035906, 0.036014, 0.035821, 0.035819, 0.035843, 0.035786, 0.035783, 0.035769, 0.035759, 0.035796, 0.035770, 0.035769, 0.035857, 0.035873, 0.035822, 0.035799, 0.035827, 0.035804, 0.035931, 0.036024, 0.035750]
plt.plot(data_uden_warmup)
plt.title("Data without warmup")
plt.xlabel("Run number")
plt.ylabel("Time used")
plt.ylim(0, 0.1)
plt.show()

# data_med_warmup = [0.034043, 0.156196, 0.035006, 0.034551, 0.149085, 0.035379, 0.035815, 0.194780, 0.052405, 0.053229, 0.052648, 0.286280, 0.036541, 0.034793, 0.034691, 0.248357, 0.034977, 0.034857, 0.034638, 0.239770, 0.034603, 0.034438, 0.034769, 0.202390, 0.053852, 0.051952, 0.052590, 0.160135, 0.034777, 0.034644, 0.034507, 0.034786, 0.153302, 0.037990, 0.038093, 0.035133, 0.034621, 0.237810, 0.034601, 0.035039, 0.034939, 0.153307, 0.054377, 0.052937, 0.052407, 0.052147, 0.184519, 0.037653, 0.037487, 0.035076, 0.034520, 0.130491, 0.036564, 0.035962, 0.035719, 0.036909, 0.152262, 0.035139, 0.035151, 0.035051, 0.034223, 0.034726, 0.179313, 0.054484, 0.052073, 0.052272, 0.053131, 0.049795, 0.225421, 0.035480, 0.035120, 0.034826, 0.034832, 0.149016, 0.034398, 0.034435, 0.034687, 0.034477, 0.034883, 0.238061, 0.036239, 0.035414, 0.034888, 0.034924, 0.130374, 0.058083, 0.055655, 0.054646, 0.038286, 0.035027, 0.034708, 0.195417, 0.035366, 0.034704, 0.035498, 0.037927, 0.036112, 0.176814, 0.034816, 0.035398]

# [0.035246, 0.162305, 0.037611, 0.035229, 0.152381, 0.036491, 0.034936, 0.243561, 0.053046, 0.053301, 0.053463, 0.275273, 0.034740, 0.034732, 0.035859, 0.261714, 0.036340, 0.036247, 0.036363, 0.266772, 0.036028, 0.035496, 0.036511, 0.337484, 0.052800, 0.052928, 0.052343, 0.288694, 0.035230, 0.035042, 0.035934, 0.034998, 0.153642, 0.034739, 0.034726, 0.035281, 0.035018, 0.218525, 0.045610, 0.035420, 0.035376, 0.153175, 0.051872, 0.053154, 0.053158, 0.052064, 0.194558, 0.038916, 0.035339, 0.034915, 0.034739, 0.247466, 0.035708, 0.035685, 0.035099, 0.035341, 0.199714, 0.035477, 0.035321, 0.035493, 0.034747, 0.269677, 0.054646, 0.055469, 0.053283, 0.056764, 0.179253, 0.036197, 0.035806, 0.035980, 0.034967, 0.147534, 0.035557, 0.035171, 0.034972, 0.034901, 0.034920, 0.227790, 0.036402, 0.035638, 0.035113, 0.035376, 0.182977, 0.055264, 0.055899, 0.046147, 0.035067, 0.168669, 0.038052, 0.035806, 0.035085, 0.035328, 0.155241, 0.038602, 0.036511, 0.034902, 0.034834, 0.034605, 0.208266, 0.034975]

data_med_warmup = [0.035943, 0.036787, 0.037468, 0.036651, 0.036852, 0.036796, 0.036723, 0.036658, 0.036726, 0.036514, 0.035810, 0.036717, 0.037222, 0.036676, 0.036700, 0.036784, 0.036308, 0.036577, 0.036681, 0.036739, 0.036617, 0.036669, 0.036626, 0.036618, 0.036697, 0.036687, 0.036726, 0.036702, 0.036667, 0.036654, 0.036604, 0.036709, 0.036669, 0.036669, 0.036656, 0.036705, 0.036710, 0.036617, 0.036616, 0.036229, 0.035859, 0.035977, 0.036043, 0.035740, 0.035779, 0.035923, 0.035782, 0.035803, 0.035781, 0.035838, 0.035751, 0.035752, 0.035776, 0.035834, 0.035749, 0.035763, 0.035730, 0.035748, 0.035672, 0.035861, 0.035789, 0.035751, 0.035797, 0.035856, 0.035809, 0.036284, 0.035861, 0.035853, 0.035795, 0.035795, 0.035929, 0.035787, 0.035874, 0.035916, 0.035766, 0.035822, 0.035895, 0.035914, 0.035795, 0.035867, 0.035833, 0.035798, 0.035825, 0.035910, 0.035834, 0.035804, 0.035734, 0.036222, 0.035797, 0.035776, 0.035830, 0.035959, 0.035982, 0.035814, 0.035908, 0.035899, 0.035977, 0.037467, 0.036208, 0.035844]
plt.plot(data_med_warmup)
plt.title("Data with warmup")
plt.xlabel("Run number")
plt.ylabel("Time used")
plt.ylim(0, 0.1)
plt.show()

plt.hist(data_med_warmup)
plt.title("Data with warmup")
plt.xlabel("Time")
plt.ylabel("Number of occurrences")
plt.show()

# N = 10

# Using 10 tasks: Run no.  0: 2605 occurrences found in 0, 000438 s
# Using 10 tasks: Run no.  1: 2605 occurrences found in 0, 000644 s
# Using 10 tasks: Run no.  2: 2605 occurrences found in 0, 000384 s
# Using 10 tasks: Run no.  3: 2605 occurrences found in 0, 000420 s
# Using 10 tasks: Run no.  4: 2605 occurrences found in 0, 000420 s
# Using 10 tasks: Run no.  5: 2605 occurrences found in 0, 000407 s
# Using 10 tasks: Run no.  6: 2605 occurrences found in 0, 000424 s
# Using 10 tasks: Run no.  7: 2605 occurrences found in 0, 000448 s
# Using 10 tasks: Run no.  8: 2605 occurrences found in 0, 000405 s
# Using 10 tasks: Run no.  9: 2605 occurrences found in 0, 000401 s
# Using 10 tasks: Run no. 10: 2605 occurrences found in 0, 000358 s
# Using 10 tasks: Run no. 11: 2605 occurrences found in 0, 002007 s
# Using 10 tasks: Run no. 12: 2605 occurrences found in 0, 000235 s
# Using 10 tasks: Run no. 13: 2605 occurrences found in 0, 000260 s
# Using 10 tasks: Run no. 14: 2605 occurrences found in 0, 000260 s
# Using 10 tasks: Run no. 15: 2605 occurrences found in 0, 000251 s
# Using 10 tasks: Run no. 16: 2605 occurrences found in 0, 000206 s
# Using 10 tasks: Run no. 17: 2605 occurrences found in 0, 000210 s
# Using 10 tasks: Run no. 18: 2605 occurrences found in 0, 000207 s
# Using 10 tasks: Run no. 19: 2605 occurrences found in 0, 000217 s
# Using 10 tasks: Run no. 20: 2605 occurrences found in 0, 000529 s
# Using 10 tasks: Run no. 21: 2605 occurrences found in 0, 000224 s
# Using 10 tasks: Run no. 22: 2605 occurrences found in 0, 000196 s
# Using 10 tasks: Run no. 23: 2605 occurrences found in 0, 000186 s
# Using 10 tasks: Run no. 24: 2605 occurrences found in 0, 000182 s
# Using 10 tasks: Run no. 25: 2605 occurrences found in 0, 000206 s
# Using 10 tasks: Run no. 26: 2605 occurrences found in 0, 000269 s
# Using 10 tasks: Run no. 27: 2605 occurrences found in 0, 000275 s
# Using 10 tasks: Run no. 28: 2605 occurrences found in 0, 000301 s
# Using 10 tasks: Run no. 29: 2605 occurrences found in 0, 000235 s
# Using 10 tasks: Run no. 30: 2605 occurrences found in 0, 001233 s
# Using 10 tasks: Run no. 31: 2605 occurrences found in 0, 000224 s
# Using 10 tasks: Run no. 32: 2605 occurrences found in 0, 000229 s
# Using 10 tasks: Run no. 33: 2605 occurrences found in 0, 000183 s
# Using 10 tasks: Run no. 34: 2605 occurrences found in 0, 000167 s
# Using 10 tasks: Run no. 35: 2605 occurrences found in 0, 000233 s
# Using 10 tasks: Run no. 36: 2605 occurrences found in 0, 000161 s
# Using 10 tasks: Run no. 37: 2605 occurrences found in 0, 000166 s
# Using 10 tasks: Run no. 38: 2605 occurrences found in 0, 000271 s
# Using 10 tasks: Run no. 39: 2605 occurrences found in 0, 000162 s
# Using 10 tasks: Run no. 40: 2605 occurrences found in 0, 000167 s
# Using 10 tasks: Run no. 41: 2605 occurrences found in 0, 000222 s
# Using 10 tasks: Run no. 42: 2605 occurrences found in 0, 000203 s
# Using 10 tasks: Run no. 43: 2605 occurrences found in 0, 000180 s
# Using 10 tasks: Run no. 44: 2605 occurrences found in 0, 000194 s
# Using 10 tasks: Run no. 45: 2605 occurrences found in 0, 000176 s
# Using 10 tasks: Run no. 46: 2605 occurrences found in 0, 000161 s
# Using 10 tasks: Run no. 47: 2605 occurrences found in 0, 000158 s
# Using 10 tasks: Run no. 48: 2605 occurrences found in 0, 000161 s
# Using 10 tasks: Run no. 49: 2605 occurrences found in 0, 000151 s
# Using 10 tasks: Run no. 50: 2605 occurrences found in 0, 000156 s
# Using 10 tasks: Run no. 51: 2605 occurrences found in 0, 000249 s
# Using 10 tasks: Run no. 52: 2605 occurrences found in 0, 000159 s
# Using 10 tasks: Run no. 53: 2605 occurrences found in 0, 000151 s
# Using 10 tasks: Run no. 54: 2605 occurrences found in 0, 000146 s
# Using 10 tasks: Run no. 55: 2605 occurrences found in 0, 000154 s
# Using 10 tasks: Run no. 56: 2605 occurrences found in 0, 000159 s
# Using 10 tasks: Run no. 57: 2605 occurrences found in 0, 000170 s
# Using 10 tasks: Run no. 58: 2605 occurrences found in 0, 000154 s
# Using 10 tasks: Run no. 59: 2605 occurrences found in 0, 000150 s
# Using 10 tasks: Run no. 60: 2605 occurrences found in 0, 000202 s
# Using 10 tasks: Run no. 61: 2605 occurrences found in 0, 000264 s
# Using 10 tasks: Run no. 62: 2605 occurrences found in 0, 000161 s
# Using 10 tasks: Run no. 63: 2605 occurrences found in 0, 000153 s
# Using 10 tasks: Run no. 64: 2605 occurrences found in 0, 000280 s
# Using 10 tasks: Run no. 65: 2605 occurrences found in 0, 000205 s
# Using 10 tasks: Run no. 66: 2605 occurrences found in 0, 000157 s
# Using 10 tasks: Run no. 67: 2605 occurrences found in 0, 000159 s
# Using 10 tasks: Run no. 68: 2605 occurrences found in 0, 000141 s
# Using 10 tasks: Run no. 69: 2605 occurrences found in 0, 000158 s
# Using 10 tasks: Run no. 70: 2605 occurrences found in 0, 000151 s
# Using 10 tasks: Run no. 71: 2605 occurrences found in 0, 000155 s
# Using 10 tasks: Run no. 72: 2605 occurrences found in 0, 000148 s
# Using 10 tasks: Run no. 73: 2605 occurrences found in 0, 000145 s
# Using 10 tasks: Run no. 74: 2605 occurrences found in 0, 000217 s
# Using 10 tasks: Run no. 75: 2605 occurrences found in 0, 000181 s
# Using 10 tasks: Run no. 76: 2605 occurrences found in 0, 000235 s
# Using 10 tasks: Run no. 77: 2605 occurrences found in 0, 000207 s
# Using 10 tasks: Run no. 78: 2605 occurrences found in 0, 000196 s
# Using 10 tasks: Run no. 79: 2605 occurrences found in 0, 000159 s
# Using 10 tasks: Run no. 80: 2605 occurrences found in 0, 000222 s
# Using 10 tasks: Run no. 81: 2605 occurrences found in 0, 000221 s
# Using 10 tasks: Run no. 82: 2605 occurrences found in 0, 000142 s
# Using 10 tasks: Run no. 83: 2605 occurrences found in 0, 000135 s
# Using 10 tasks: Run no. 84: 2605 occurrences found in 0, 000288 s
# Using 10 tasks: Run no. 85: 2605 occurrences found in 0, 000208 s
# Using 10 tasks: Run no. 86: 2605 occurrences found in 0, 000154 s
# Using 10 tasks: Run no. 87: 2605 occurrences found in 0, 000158 s
# Using 10 tasks: Run no. 88: 2605 occurrences found in 0, 000173 s
# Using 10 tasks: Run no. 89: 2605 occurrences found in 0, 000193 s
# Using 10 tasks: Run no. 90: 2605 occurrences found in 0, 000278 s
# Using 10 tasks: Run no. 91: 2605 occurrences found in 0, 000196 s
# Using 10 tasks: Run no. 92: 2605 occurrences found in 0, 000371 s
# Using 10 tasks: Run no. 93: 2605 occurrences found in 0, 000851 s
# Using 10 tasks: Run no. 94: 2605 occurrences found in 0, 000172 s
# Using 10 tasks: Run no. 95: 2605 occurrences found in 0, 000144 s
# Using 10 tasks: Run no. 96: 2605 occurrences found in 0, 000143 s
# Using 10 tasks: Run no. 97: 2605 occurrences found in 0, 000155 s
# Using 10 tasks: Run no. 98: 2605 occurrences found in 0, 000159 s
# Using 10 tasks: Run no. 99: 2605 occurrences found in 0, 000163 s

# Using 10 tasks(avg.): 0, 000259 s


# Average speedup: 0.71


# N = 100

# Using 100 tasks: Run no.  0: 2605 occurrences found in 0, 000664 s
# Using 100 tasks: Run no.  1: 2605 occurrences found in 0, 000688 s
# Using 100 tasks: Run no.  2: 2605 occurrences found in 0, 000552 s
# Using 100 tasks: Run no.  3: 2605 occurrences found in 0, 000547 s
# Using 100 tasks: Run no.  4: 2605 occurrences found in 0, 000422 s
# Using 100 tasks: Run no.  5: 2605 occurrences found in 0, 000382 s
# Using 100 tasks: Run no.  6: 2605 occurrences found in 0, 000420 s
# Using 100 tasks: Run no.  7: 2605 occurrences found in 0, 000320 s
# Using 100 tasks: Run no.  8: 2605 occurrences found in 0, 000369 s
# Using 100 tasks: Run no.  9: 2605 occurrences found in 0, 000413 s
# Using 100 tasks: Run no. 10: 2605 occurrences found in 0, 002496 s
# Using 100 tasks: Run no. 11: 2605 occurrences found in 0, 000341 s
# Using 100 tasks: Run no. 12: 2605 occurrences found in 0, 000327 s
# Using 100 tasks: Run no. 13: 2605 occurrences found in 0, 000256 s
# Using 100 tasks: Run no. 14: 2605 occurrences found in 0, 000251 s
# Using 100 tasks: Run no. 15: 2605 occurrences found in 0, 000655 s
# Using 100 tasks: Run no. 16: 2605 occurrences found in 0, 000345 s
# Using 100 tasks: Run no. 17: 2605 occurrences found in 0, 000762 s
# Using 100 tasks: Run no. 18: 2605 occurrences found in 0, 000214 s
# Using 100 tasks: Run no. 19: 2605 occurrences found in 0, 000455 s
# Using 100 tasks: Run no. 20: 2605 occurrences found in 0, 000208 s
# Using 100 tasks: Run no. 21: 2605 occurrences found in 0, 000237 s
# Using 100 tasks: Run no. 22: 2605 occurrences found in 0, 000221 s
# Using 100 tasks: Run no. 23: 2605 occurrences found in 0, 000188 s
# Using 100 tasks: Run no. 24: 2605 occurrences found in 0, 000195 s
# Using 100 tasks: Run no. 25: 2605 occurrences found in 0, 000209 s
# Using 100 tasks: Run no. 26: 2605 occurrences found in 0, 000192 s
# Using 100 tasks: Run no. 27: 2605 occurrences found in 0, 000206 s
# Using 100 tasks: Run no. 28: 2605 occurrences found in 0, 000212 s
# Using 100 tasks: Run no. 29: 2605 occurrences found in 0, 000210 s
# Using 100 tasks: Run no. 30: 2605 occurrences found in 0, 000216 s
# Using 100 tasks: Run no. 31: 2605 occurrences found in 0, 000220 s
# Using 100 tasks: Run no. 32: 2605 occurrences found in 0, 000374 s
# Using 100 tasks: Run no. 33: 2605 occurrences found in 0, 000294 s
# Using 100 tasks: Run no. 34: 2605 occurrences found in 0, 000210 s
# Using 100 tasks: Run no. 35: 2605 occurrences found in 0, 000234 s
# Using 100 tasks: Run no. 36: 2605 occurrences found in 0, 000205 s
# Using 100 tasks: Run no. 37: 2605 occurrences found in 0, 000250 s
# Using 100 tasks: Run no. 38: 2605 occurrences found in 0, 000219 s
# Using 100 tasks: Run no. 39: 2605 occurrences found in 0, 000209 s
# Using 100 tasks: Run no. 40: 2605 occurrences found in 0, 001250 s
# Using 100 tasks: Run no. 41: 2605 occurrences found in 0, 000202 s
# Using 100 tasks: Run no. 42: 2605 occurrences found in 0, 000194 s
# Using 100 tasks: Run no. 43: 2605 occurrences found in 0, 000206 s
# Using 100 tasks: Run no. 44: 2605 occurrences found in 0, 000184 s
# Using 100 tasks: Run no. 45: 2605 occurrences found in 0, 000294 s
# Using 100 tasks: Run no. 46: 2605 occurrences found in 0, 000210 s
# Using 100 tasks: Run no. 47: 2605 occurrences found in 0, 000213 s
# Using 100 tasks: Run no. 48: 2605 occurrences found in 0, 000189 s
# Using 100 tasks: Run no. 49: 2605 occurrences found in 0, 000204 s
# Using 100 tasks: Run no. 50: 2605 occurrences found in 0, 000199 s
# Using 100 tasks: Run no. 51: 2605 occurrences found in 0, 000258 s
# Using 100 tasks: Run no. 52: 2605 occurrences found in 0, 000227 s
# Using 100 tasks: Run no. 53: 2605 occurrences found in 0, 000893 s
# Using 100 tasks: Run no. 54: 2605 occurrences found in 0, 000553 s
# Using 100 tasks: Run no. 55: 2605 occurrences found in 0, 000352 s
# Using 100 tasks: Run no. 56: 2605 occurrences found in 0, 000215 s
# Using 100 tasks: Run no. 57: 2605 occurrences found in 0, 000186 s
# Using 100 tasks: Run no. 58: 2605 occurrences found in 0, 000266 s
# Using 100 tasks: Run no. 59: 2605 occurrences found in 0, 000409 s
# Using 100 tasks: Run no. 60: 2605 occurrences found in 0, 000279 s
# Using 100 tasks: Run no. 61: 2605 occurrences found in 0, 000223 s
# Using 100 tasks: Run no. 62: 2605 occurrences found in 0, 000171 s
# Using 100 tasks: Run no. 63: 2605 occurrences found in 0, 000162 s
# Using 100 tasks: Run no. 64: 2605 occurrences found in 0, 000164 s
# Using 100 tasks: Run no. 65: 2605 occurrences found in 0, 000201 s
# Using 100 tasks: Run no. 66: 2605 occurrences found in 0, 000157 s
# Using 100 tasks: Run no. 67: 2605 occurrences found in 0, 000164 s
# Using 100 tasks: Run no. 68: 2605 occurrences found in 0, 000202 s
# Using 100 tasks: Run no. 69: 2605 occurrences found in 0, 000179 s
# Using 100 tasks: Run no. 70: 2605 occurrences found in 0, 000273 s
# Using 100 tasks: Run no. 71: 2605 occurrences found in 0, 000261 s
# Using 100 tasks: Run no. 72: 2605 occurrences found in 0, 000307 s
# Using 100 tasks: Run no. 73: 2605 occurrences found in 0, 000752 s
# Using 100 tasks: Run no. 74: 2605 occurrences found in 0, 000904 s
# Using 100 tasks: Run no. 75: 2605 occurrences found in 0, 000318 s
# Using 100 tasks: Run no. 76: 2605 occurrences found in 0, 000151 s
# Using 100 tasks: Run no. 77: 2605 occurrences found in 0, 000181 s
# Using 100 tasks: Run no. 78: 2605 occurrences found in 0, 000185 s
# Using 100 tasks: Run no. 79: 2605 occurrences found in 0, 000164 s
# Using 100 tasks: Run no. 80: 2605 occurrences found in 0, 000181 s
# Using 100 tasks: Run no. 81: 2605 occurrences found in 0, 000166 s
# Using 100 tasks: Run no. 82: 2605 occurrences found in 0, 000172 s
# Using 100 tasks: Run no. 83: 2605 occurrences found in 0, 000177 s
# Using 100 tasks: Run no. 84: 2605 occurrences found in 0, 000222 s
# Using 100 tasks: Run no. 85: 2605 occurrences found in 0, 000174 s
# Using 100 tasks: Run no. 86: 2605 occurrences found in 0, 000214 s
# Using 100 tasks: Run no. 87: 2605 occurrences found in 0, 000336 s
# Using 100 tasks: Run no. 88: 2605 occurrences found in 0, 000172 s
# Using 100 tasks: Run no. 89: 2605 occurrences found in 0, 000445 s
# Using 100 tasks: Run no. 90: 2605 occurrences found in 0, 000183 s
# Using 100 tasks: Run no. 91: 2605 occurrences found in 0, 000217 s
# Using 100 tasks: Run no. 92: 2605 occurrences found in 0, 000164 s
# Using 100 tasks: Run no. 93: 2605 occurrences found in 0, 000186 s
# Using 100 tasks: Run no. 94: 2605 occurrences found in 0, 000236 s
# Using 100 tasks: Run no. 95: 2605 occurrences found in 0, 000215 s
# Using 100 tasks: Run no. 96: 2605 occurrences found in 0, 000225 s
# Using 100 tasks: Run no. 97: 2605 occurrences found in 0, 000226 s
# Using 100 tasks: Run no. 98: 2605 occurrences found in 0, 000233 s
# Using 100 tasks: Run no. 99: 2605 occurrences found in 0, 000240 s

# Using 100 tasks(avg.): 0, 000319 s


# Average speedup: 0.58
