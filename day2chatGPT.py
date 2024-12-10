
def is_safe(report):
    """Check if a report is safe based on the original rules."""
    if all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report)-1)):
        return True  # Increasing
    if all(-3 <= report[i+1] - report[i] <= -1 for i in range(len(report)-1)):
        return True  # Decreasing
    return False

def is_safe_with_removal(report):
    """Check if a report can be made safe by removing a single level."""
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove one level
        if is_safe(modified_report):
            return True
    return False

# Read and parse the input
with open("inputFiles/02_1.txt") as f:
    reports = [list(map(int, line.split())) for line in f]

# Count safe reports considering the Problem Dampener
safe_count = 0
for report in reports:
    if is_safe(report) or is_safe_with_removal(report):
        safe_count += 1

print(f"Number of safe reports: {safe_count}")
