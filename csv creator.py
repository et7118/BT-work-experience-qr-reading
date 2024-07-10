import csv
with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['name', 'email', 'is_speaker', 'uids', 'arrived'])
    spamwriter.writerow(['Callum Bird','icallumbird@icloud.com','FALSE','6946ea84-957d-4c3a-8aff-7471b55c55bc','FALSE'])
    spamwriter.writerow(['George Jones',	'gorgonus@hotmail.com','TRUE','5146c505-94c9-4d97-9dd7-0f806319aa12','FALSE'])
    spamwriter.writerow(['Tedward Omlinson','e79234@gmail.com','FALSE','c64c9bd0-3984-4edb-9415-6e7490ded8fc','FALSE'])