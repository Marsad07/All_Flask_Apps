# Import necessary modules from Flask
from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def index():
    # Render the index.html template when the user visits the root URL
    return render_template('index.html')

# Define the route to handle form submission from the dropdown
@app.route('/mood', methods=['POST'])
def mood():
    # Get the selected mood from the form data
    selected_mood = request.form['moods']

    # Match the selected mood to a description and background color
    if selected_mood == 'Sad':
        message = (
            "When you're sad, you feel unhappy. If you've ever experienced the death of a pet you loved deeply, "
            "you know exactly what it means to feel sad. You might use the adjective sad informally to describe "
            "something that's pathetic or that you feel scornful or disdainful about."
        )
        color = "#87CEFA"  # Light blue for sadness
    elif selected_mood == 'Happy':
        message = (
            "Happy is a feeling of joy, pleasure, or good fortune — it's how you'd feel if you learned that you "
            "won the lottery or got accepted into your number one choice of colleges."
        )
        color = "#00FF00"  #  Green for happiness
    elif selected_mood == 'Annoyed':
        message = (
            "Being annoyed means feeling or showing mild to moderate anger, irritation, or displeasure caused by "
            "someone or something that is bothersome or frustrating. For example, you are waiting for the bus and "
            "the bus you need to get on arrives but it drives past you — you'd be annoyed they ignored you."
        )
        color = "#FF6347"  # Red for annoyance
    elif selected_mood == 'Tired':
        message = (
            "Being tired means having a lack of energy, whether it is physical or mental. For example, you are tired "
            "which leads to a strong need for rest or sleep."
        )
        color = "#D1C1F2"  # Purple for tiredness
    else:
        # Fallback message and color if mood is not recognized
        message = "Mood not recognized."
        color = "#A9A9A9"  # Gray for unknown mood

    # Render the mood.html template with the mood message and background color
    return render_template('mood.html', message=message, color=color)

# Run the Flask app in debug mode when this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)

# End of program