
print("\n---- PLURALITY IDENTIFIER ----")
print("provide the counts, get the plurality\n\n")

# GROUPS
print("GROUPS")
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

# ISOLATED_GROUPS
isolated_groups = input("Enter isolated_groups (or combine multiple w/ group1+group5): ").split("+")
print(f"isolated_groups: {isolated_groups}\n")
# verify all groups
for group in isolated_groups:
	if group not in groups:
		print("ERROR: isolated_groups contains unknown group")

# CALCULATE
# totals→percent

# get total of groups
group_total = 0
for group in groups:
	group_total += groups[group]
print(f"group_total: {group_total}")

# get total of isolated_groups
isolatedgroup_total = 0
for isolated_group in isolated_groups:
	isolatedgroup_total += groups[isolated_group]
print(f"isolatedgroup_total: {isolatedgroup_total}")

print("----")

# get percents
isolated_groups_percent = round((isolatedgroup_total / group_total) * 100, 2)
print(f"{isolated_groups}: {isolated_groups_percent}%")
for isolated_group in isolated_groups:
	isolated_group_percent = round((groups[isolated_group] / group_total) * 100, 2)
	print(f"{isolated_group}: {isolated_group_percent}%")