from flask import Flask, render_template, request, jsonify
from github_profile_generator import GitHubProfileGenerator
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_readme():
    try:
        data = request.json
        generator = GitHubProfileGenerator(username=data['username'])
        readme_content = generator.generate_profile(data['config'])
        return jsonify({
            'status': 'success',
            'readme': readme_content
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)