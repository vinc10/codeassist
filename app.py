from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# TO DO: Move this?
from flask import jsonify, request
import gpt_call

@app.route('/improve-code', methods=['POST'])
def improve_code():
    try:
        code_to_improve = request.json['code']
        response = gpt_call.get_improved_code(code_to_improve)

        # Convert Markdown code blocks to HTML
        improved_text = response.choices[0].message.content.replace("```python", "<pre><code>").replace("```", "</code></pre>")
        
        return jsonify(improved_code=improved_text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify(error=str(e)), 500




if __name__ == '__main__':
    app.run(debug=True)

