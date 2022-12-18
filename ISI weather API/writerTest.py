import csv

# Open the CSV file in write mode
with open('data.csv', 'w', newline='') as csv_file:
  # Create a CSV writer object
  csv_writer = csv.writer(csv_file)

  # Write the data to the file
  csv_writer.writerow(['Name', 'Age', 'Country'])
  csv_writer.writerow(['Alice', 25, 'USA'])
  csv_writer.writerow(['Bob', 30, 'Canada'])