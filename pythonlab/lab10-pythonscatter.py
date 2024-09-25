import csv
import matplotlib.pyplot as plt


male_height = []
male_weight = []
female_height = []
female_weight = []


with open('Height_Weight_Ratio.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  

    
    for row in reader:
        gender = row[0]
        height = float(row[1])
        weight = float(row[2])

       
        if gender == 'Male':
            male_height.append(height)
            male_weight.append(weight)
        elif gender == 'Female':
            female_height.append(height)
            female_weight.append(weight)

plt.scatter(male_height, male_weight, color='blue', label='Male')
plt.scatter(female_height, female_weight, color='red', label='Female')


plt.xlabel('Height (inches)')
plt.ylabel('Weight (lbs)')
plt.title('Relation between Height and Weight in Adult Male and Female')


plt.legend()


plt.show()
