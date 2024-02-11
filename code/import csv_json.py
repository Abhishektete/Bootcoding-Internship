import csv
import json

csvfile = open("D:\Bootcoding task\LeetScrape-main\quesquestions.csv", 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("QID",	"title",	"titleSlug",	"difficulty",	"acceptanceRate",	"topicTags",	"categorySlug")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)