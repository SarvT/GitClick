from flask import Flask, render_template, request, jsonify
import yaml
from github_profile_generator import GitHubProfileGenerator 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexold.html')

@app.route('/generate', methods=['POST'])
def generate_readme():
    data = request.form.to_dict(flat=True)
    
    config = {
        'profile_type': data.get('profile_type', 'developer'),
        'greeting': data.get('greeting', "Hi 👋, I'm User"),
        'typing_text': data.get('typing_text', 'Full+Stack+Developer,Open+Source+Enthusiast').split(','),
        'tech_stacks': yaml.safe_load(data.get('tech_stacks', '{}')),
        'current_focus': yaml.safe_load(data.get('current_focus', '{}')),
        'social_links': yaml.safe_load(data.get('social_links', '{}')),
        'spotify_username': data.get('spotify_username', ''),
        'show_snake': data.get('show_snake', 'false') == 'true',
        'show_activity_graph': data.get('show_activity_graph', 'false') == 'true',
        'show_trophies': data.get('show_trophies', 'false') == 'true',
        'theme': data.get('theme', 'radical'),
        'custom_sections': yaml.safe_load(data.get('custom_sections', '{}')),
    }
    
    generator = GitHubProfileGenerator(username=data.get('username', 'user'))
    readme_content = generator.generate_profile(config)
    
    with open("./results/README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    return jsonify({"message": "README.md generated successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
