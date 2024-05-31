import os

files = os.listdir("images")
counter1 = 0

for image in files:
	if os.path.getsize(f"images/{image}") == 0:
		os.remove(f"images/{image}")
		counter1 += 1

print(f"Deleted {counter1} empty files")
