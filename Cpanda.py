import pandas as panda

data = {
	'test 1 scores' : [100, 99, 60, 92, 84, 91 ,73],
	'test 2 scores' : [99, 70, 72, 81, 92, 79, 80],
	'Final Exam Scores': [90, 89, 72, 61, 84, 91, 89]
}
TestScores = panda.DataFrame(data)
print(TestScores)

TestScores.replace([100,99,92,91,90,89,84,79,73,72,70,61,60],['Perfect','A+','A','A-','A-','A-','B','B-','C','C-','C-','F','F'])
print(TestScores)