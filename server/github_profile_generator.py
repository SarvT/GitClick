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
        try:
            response = requests.get(f"https://api.github.com/users/{self.username}")
            if response.status_code == 200:
                return response.json()
            return {}
        except:
            return {}

    def generate_snake_animation(self) -> str:
        return f"""
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{self.username}/{self.username}/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{self.username}/{self.username}/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/{self.username}/{self.username}/output/github-contribution-grid-snake.svg">
</picture>
"""

    def generate_metrics_cards(self) -> str:
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

    def generate_profile(self, config: Dict) -> str:
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

{self.generate_snake_animation() if config.get('show_snake', True) else ''}

{self.generate_metrics_cards()}

### 🌱 Current Focus
```yaml
{yaml.dump(config.get('current_focus', {
    'learning': ['New Technologies', 'Best Practices'],
    'working_on': ['Open Source Projects', 'Personal Portfolio'],
    'collaborating_on': ['Exciting Projects', 'Community Initiatives']
}), default_flow_style=False)}
```

### 💌 Connect With Me
<div align="center">
{self._generate_social_links(config.get('social_links', {}))}
</div>
"""
        return readme

    def _generate_social_links(self, social_links: Dict[str, str]) -> str:
        badges = []
        for platform, url in social_links.items():
            badges.append(f'<a href="{url}"><img src="https://img.shields.io/badge/{platform}-black?style=for-the-badge&logo={platform.lower()}&logoColor=white" alt="{platform}"/></a>')
        return '\n'.join(badges)


def save_readme(content: str, filename: str = "README.md") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    username = input("Enter your GitHub username: ")
    config = {
        'profile_type': 'developer',
        'greeting': "Hi 👋, I'm John Doe",
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
        'show_snake': True,
        'theme': 'radical'
    }

    generator = GitHubProfileGenerator(username=username)
    readme_content = generator.generate_profile(config)
    save_readme(readme_content)
    print("Enhanced README.md has been generated successfully!")
