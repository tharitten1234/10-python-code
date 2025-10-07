"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

#get_temperatures
def get_temperatures():
    temp = [23,14,20,35,21,22,27] #[] มันคือเครื่องหมายของ list ถ้าจะกำหนดเลขใส่เลขไปได้เลย [23,14,20,35,21,22,27]
    return temp
    
#analyze_temps
def analyze_temps(temp_list): #temp_list คือ list ของ temp 
    avg = 0 #avg = sum(temp_list) / (temp_list) 
    highest = max(temp_list)
    lowest = min(temp_list)
    #return avg, highest, lowest

    sum = 0
    for temp in temp_list:
        sum = sum + temp
    avg = sum / len(temp_list)
    return (avg, highest, lowest)



#display_analysis
def display_analysis(avg, high, low):
    print("Temperature Analysis for the week: ")
    print("Average: %.2f C" % (avg))
    print(f"Highest: {high} C")
    print("Lowest: {low} C")

my_temp = get_temperatures()
analyzed_temp = analyze_temps(my_temp)
display_analysis(analyzed_temp[0], analyzed_temp[1], analyzed_temp[2])