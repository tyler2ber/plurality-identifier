
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

# ALLIANCE
alliance = input("Enter alliance (combine multiple w/ group1+group5): ").split("+")
print(f"alliance: {alliance}\n")
# verify all groups
for group in alliance:
	if group not in groups:
		print("ERROR: alliance contains unknown group")

# CALCULATE
# totals→percent

# get total of alliance
alliance_total = 0
for alliance_group in alliance:
	alliance_total += groups[alliance_group]
print(f"alliance_total: {alliance_total}")

# get total of groups
group_total = 0
for group in groups:
	group_total += groups[group]
print(f"group_total: {group_total}")

print("----")

# get percents
alliance_percent = round((alliance_total / group_total) * 100, 2)
print(f"{alliance}: {alliance_percent}% ({alliance_total}/{group_total})")
for alliance_group in alliance:
	alliance_group_percent = round((groups[alliance_group] / group_total) * 100, 2)
	print(f"{alliance_group}: {alliance_group_percent}% ({groups[alliance_group]}/{group_total})")