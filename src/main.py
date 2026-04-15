
print("\n---- PLURALITY IDENTIFIER ----")
print("provide the counts, get the plurality\n\n")

# GROUPS w/ COUNTS
print("GROUPS w/ COUNTS")
groups = {}
while True:

	# get group_name and group_count
	group_name = input("\ngroup_name: ")
	while True:
		try:
			group_count = int(input("group_count: "))
			break
		except ValueError:
			print(f"--> error: enter a number for {group_name}")

	# add group_name and group_count to groups
	groups[group_name] = group_count

	if input("--> another entry? ('n'): ") == "n":
		print("\n")
		break

# ISOLATED
isolated = input("Enter isolated (or combine multiple w/ group1+group5): ")
print(f"isolated: {isolated}\n")
# verify all groups
for group in isolated.split("+"):
	if group not in groups:
		print("ERROR: isolated contains unknown group")