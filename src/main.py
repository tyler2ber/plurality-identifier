
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

# ALLIANCES
print("\nALLIANCES (example: group1+group2, group3, group4+group5)")
for group in groups:
	print(f"- {group}:{groups[group]}")
alliances = input("\nalliances: ").split(",")

# print("\nISOLATED (list_groups_and_alliances_here)")