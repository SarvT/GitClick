import requests
from datetime import datetime
import json
import os
from typing import List, Dict, Optional
import yaml

class GitHubProfileGenerator:
    def __init__(self, username: str, theme: str = "radical"):
        self.username = username
        self.theme = theme
        self.github_stats = self._fetch_github_stats()
        
    def _fetch_github_stats(self) -> Dict:
        """Fetch real GitHub statistics if possible"""
        try:
            response = requests.get(f"https://api.github.com/users/{self.username}")
            if response.status_code == 200:
                return response.json()
            return {}
        except:
            return {}

    def generate_snake_animation(self) -> str:
        """Generate GitHub contribution snake animation"""
        return f"""
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{self.username}/{self.username}/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{self.username}/{self.username}/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/{self.username}/{self.username}/output/github-contribution-grid-snake.svg">
</picture>
"""

    def generate_metrics_cards(self) -> str:
        """Generate various GitHub metrics cards"""
        return f"""
<details>
  <summary>📊 GitHub Stats</summary>
  <div align="center">
    <img src="https://github-readme-stats.vercel.app/api?username={self.username}&show_icons=true&theme={self.theme}" alt="GitHub Stats" />
    <img src="https://github-readme-streak-stats.herokuapp.com/?user={self.username}&theme={self.theme}" alt="GitHub Streak" />
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={self.username}&layout=compact&theme={self.theme}" alt="Top Languages" />
  </div>
</details>
"""

    def generate_tech_section(self, tech_stacks: Dict[str, List[str]]) -> str:
        """Generate technology stack section with categorized badges"""
        sections = []
        for category, techs in tech_stacks.items():
            badges = []
            for tech in techs:
                tech_slug = tech.lower().replace(' ', '-')
                badge = f"![{tech}](https://img.shields.io/badge/{tech_slug}-black?style=for-the-badge&logo={tech_slug}&logoColor=white)"
                badges.append(badge)
            
            sections.append(f"""
<details>
  <summary>{category}</summary>
  <div align="center">
    {' '.join(badges)}
  </div>
</details>
""")
        return '\n'.join(sections)

    def generate_activity_graph(self) -> str:
        """Generate GitHub activity graph"""
        return f"""
<details>
  <summary>📈 Contribution Graph</summary>
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={self.username}&theme=github-compact" alt="Contribution Graph" />
</details>
"""

    def generate_trophy_section(self) -> str:
        """Generate GitHub trophy section"""
        return f"""
<details>
  <summary>🏆 GitHub Trophies</summary>
  <div align="center">
    <img src="https://github-profile-trophy.vercel.app/?username={self.username}&theme={self.theme}&column=4&margin-w=15&margin-h=15" alt="GitHub Trophies" />
  </div>
</details>
"""

    def generate_spotify_section(self, spotify_username: Optional[str] = None) -> str:
        """Generate Spotify Now Playing section"""
        if spotify_username:
            return f"""
<details>
  <summary>🎵 Now Playing</summary>
  <div align="center">
    <img src="https://spotify-github-profile.vercel.app/api/view?uid={spotify_username}&cover_image=true&theme=novatorem" alt="Spotify Now Playing" />
  </div>
</details>
"""
        return ""

    def generate_profile(self, config: Dict) -> str:
        """Generate the complete GitHub profile README"""
        intro_gifs = {
            'coder': 'https://media.giphy.com/media/SWoSkN6DxTszqIKEqv/giphy.gif',
            'developer': 'https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif',
            'designer': 'https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif'
        }

        readme = f"""
<div align="center">
  <img src="{intro_gifs.get(config.get('profile_type', 'coder'))}" width="450" />
</div>

<h1 align="center">
    {config.get('greeting', f"Hi 👋, I'm {self.username}")}
</h1>

<h3 align="center">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2196F3&center=true&vCenter=true&width=435&lines={';'.join(config.get('typing_text', ['Passionate+Developer', 'Open+Source+Enthusiast', 'Always+Learning']))}" alt="Typing SVG" />
</h3>

{self.generate_snake_animation() if config.get('show_snake', True) else ''}

### 🛠️ Technology Stack
{self.generate_tech_section(config['tech_stacks'])}

{self.generate_metrics_cards()}

{self.generate_activity_graph() if config.get('show_activity_graph', True) else ''}

{self.generate_trophy_section() if config.get('show_trophies', True) else ''}

{self.generate_spotify_section(config.get('spotify_username')) if config.get('spotify_username') else ''}

### 🌱 Current Focus
```yaml
{yaml.dump(config.get('current_focus', {
    'learning': ['New Technologies', 'Best Practices'],
    'working_on': ['Open Source Projects', 'Personal Portfolio'],
    'collaborating_on': ['Exciting Projects', 'Community Initiatives']
}), default_flow_style=False)}
```

### 📫 Connect With Me
<div align="center">
{self._generate_social_links(config.get('social_links', {}))}
</div>

{self._generate_custom_sections(config.get('custom_sections', {}))}

<div align="center">
    <img src="https://komarev.com/ghpvc/?username={self.username}&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</div>
"""
        return readme

    def _generate_social_links(self, social_links: Dict[str, str]) -> str:
        """Generate social media links with icons"""
        badges = []
        for platform, url in social_links.items():
            badges.append(f'<a href="{url}"><img src="https://img.shields.io/badge/{platform}-black?style=for-the-badge&logo={platform.lower()}&logoColor=white" alt="{platform}"/></a>')
        return '\n'.join(badges)

    def _generate_custom_sections(self, custom_sections: Dict[str, str]) -> str:
        """Generate custom markdown sections"""
        return '\n\n'.join([f"### {title}\n{content}" for title, content in custom_sections.items()])

def save_readme(content: str, filename: str = "README.md") -> None:
    """Save the generated README to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# Example usage
if __name__ == "__main__":
    # Example configuration
    username = input("Enter your GitHub username: ")
    config = {
        'profile_type': 'developer',  # 'coder', 'developer', or 'designer'
        'greeting': "Hi 👋, I'm John Doe",
        'typing_text': [
            'Full+Stack+Developer',
            'Open+Source+Enthusiast',
            'Problem+Solver'
        ],
        'tech_stacks': {
            '💻 Languages': ['Python', 'JavaScript', 'TypeScript', 'Java'],
            '🌐 Frontend': ['React', 'Vue', 'Angular', 'Tailwind'],
            '⚙️ Backend': ['Node.js', 'Django', 'FastAPI', 'Spring'],
            '🛢️ Database': ['MongoDB', 'PostgreSQL', 'Redis'],
            '🔧 Tools': ['Docker', 'Git', 'AWS', 'Linux']
        },
        'current_focus': {
            'learning': ['Rust', 'Web3', 'Machine Learning'],
            'working_on': ['Personal Blog', 'Open Source Projects'],
            'interests': ['System Design', 'Cloud Architecture']
        },
        'social_links': {
            'LinkedIn': 'https://linkedin.com/in/username',
            'Twitter': 'https://twitter.com/username',
            'Dev.to': 'https://dev.to/username'
        },
        'spotify_username': 'your_spotify_username',  # Optional
        'show_snake': True,
        'show_activity_graph': True,
        'show_trophies': True,
        'theme': 'radical',  # GitHub theme for stats cards
        'custom_sections': {
            '📚 Latest Blog Posts': """
- [How to Build a REST API with FastAPI](https://example.com)
- [Understanding Docker Compose](https://example.com)
- [Advanced Git Workflows](https://example.com)
"""
        }
    }

    generator = GitHubProfileGenerator(username=username)
    readme_content = generator.generate_profile(config)
    save_readme(readme_content)
    print("Enhanced README.md has been generated successfully!")