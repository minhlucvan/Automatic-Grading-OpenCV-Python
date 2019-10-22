import csv

def loadTest(file):	
	results = []
	with open(file, newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		for row in reader:
			results.append(row)
	return results

def evaluate(templates, answers):
	point = 0
	total = sum(int(a[2]) for a in templates)
	for index, answer in enumerate(templates):
		if(answers[index] == answer[1]):
			point += int(answer[2])

	return point, total