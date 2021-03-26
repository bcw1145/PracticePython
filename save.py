import csv

def save_to_file(jobs):
  file= open("jobs.csv", mode="w")
  writer= csv.writer(file)
  writer.writerow(["title" , "company" ,"location", "link"])
  print(jobs)
  for job in jobs:
    if job is not None:
      writer.writerow(list(job.values()))
  return 