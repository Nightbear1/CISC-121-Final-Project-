# CISC-121-Final-Project
Final Project for CISC-121, implementing Binary Search
The algorithm that I have chosen to implement and visualize is the Binary Search algorithm. As an algorithm that is both easier to understand, and better to create a more visually applealing example


## Decomposition
For the binary search algorithm, starting with a sorted list and a target value, calculate a middle index of the list, and compare it to target value. If target value is smaller, search the left half. If target value is larger, then search the right half. Repeat until the value has been found, or all values have been accounted for.

## Pattern Recognition:
Binary search utilizes a repeating pattern of comparing targets with values with the middle index, halving the search space with every refinement. That is why binary search has a time complexity of O(log n).

## Abstraction
Goal for this app is to demonstrate binary search, to someone who does not need to know a lot about algorithms. Eliminating common edge cases, such as input array of length 0, or non-interger target values being selected was achieved. For this app, Gradio was used to simplify visual output.

## Algorithm Design
Input list will be auto generated, while selected target value will be on a slider. 
Output will show whether or not target value is found in list, it's index, and the steps taken to achieve it

# How to Run - Online
1. Generate list using "Generate New Random List" button
2. Use slider to select target value
3. Click "Search" button

# How to Run - Offline
```
git clone https://github.com/Nightbear1/CISC-121-Final-Project-.git
```
then, install gradio
```
pip install gradio
```
Finally, run app.py
```
python app.py
```


# Tests
Below are the following possible cases that were tested
Here lies a valid target in example Array:
    ![Alt text](/Files/TRUE.png?raw=true "Correct Implementation")
Here lies a target not in example Array
    ![Alt text](/Files/FALSE.png?raw=true "Incorrect Implementation")

Here lies example without generated Array
    ![Alt text](/Files/NoArray.png?raw=true "Correct Implementation")

# Hugging Face Link
https://huggingface.co/spaces/25xjw1/BinarySearch
# Acknowledgement
Most of the code for implementing the Gradio API utilized level 3 and level 4 AI usage.
