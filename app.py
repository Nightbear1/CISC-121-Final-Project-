import gradio as gr
import random

#Binary Search

def generate_list(size=10):
  lowerbound = 0
  upperbound = 50
  randomlist = random.sample(range(lowerbound, upperbound),10) #Creating random list
  return sorted(randomlist)

def binary(s, target, low, high, steps):
    if low > high: #Range wrong
        steps.append("Range wrong")
        return None
    mid = (low + high) // 2
    steps.append(f"Checking index {mid} in range ({low}, {high})")

    if s[mid] == target:
        steps.append(f"Target {target} found at index {mid}")
        return mid
    elif target < s[mid]:
        steps.append(f"As {target} < {s[mid]}, we search the left half")
        return binary(s, target, low, mid - 1, steps)
    else:
        steps.append(f"As {target} > {s[mid]}, we search the right half")
        return binary(s, target, mid + 1, high, steps)

def binarysearch(s,target):
  steps = [] #Taking into account steps
  result = binary(s,target,0,len(s)-1, steps)
  return result, steps
#Gradio helperr functions
def create_new_list_ui():
    new_list = generate_list()
    return new_list, f"**Current List:** {new_list}"

def update_search(target, current_list):
    if not current_list:
        return "Please generate a list first!", []

    if target is None:
        return "Please enter a valid number.", []

    result, steps = binarysearch(current_list, int(target))

    # Convert steps into table rows
    table_rows = []
    for i, step in enumerate(steps, start=1):
        table_rows.append([i, step])

    if result is None:
        message = f"###  Target {target} not found."
    else:
        message = f"###  Target {target} found at index {result}."

    return message, table_rows
#Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("Binary Search Visualization")
    list_state = gr.State([])
#list generation
    with gr.Row():
        with gr.Column(scale=12):
            generatebutton = gr.Button(
                  "Generate New Random List",
                  variant = "primary",
                  size = "lg"
            )
    with gr.Column(scale=12):
        listdisplay = gr.Markdown("Click to Start")
#Search Settings
    with gr.Row():
        with gr.Column(scale=5):
            target_input = gr.Slider( #Utilizing a slider forces inputs to be intergers)
                minimum=0,
                maximum=50,
                step=1,
                label="Target number"
            )
            searchbutton = gr.Button(
                "Search",
                variant = "secondary",
                size="lg"
            )
        with gr.Column(scale=3):
            result_display = gr.Markdown("Ready to search")
    # --- Step Log Section ---
    gr.Markdown("Step-by-Step Execution Log")

    steps_output = gr.Dataframe(
        headers=["Step", "Explanation"],
        datatype=["number", "str"],
        interactive=False,
        wrap=True
    )

    # --- Event Listeners ---
    generatebutton.click(
        fn=create_new_list_ui,
        inputs=None,
        outputs=[list_state, listdisplay]
    )

    searchbutton.click(
        fn=update_search,
        inputs=[target_input, list_state],
        outputs=[result_display, steps_output]
    )

# Launch with theme
demo.launch(theme=gr.themes.Glass())
