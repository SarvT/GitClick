# import requests
# from datetime import datetime

# def generate_github_profile(username, tech_stacks):
#     """
#     Generate a GitHub profile README with dynamic content and styling
    
#     Parameters:
#     username (str): GitHub username
#     tech_stacks (list): List of technologies/skills
#     """
    
#     # Format tech stack badges
#     tech_badges = []
#     for tech in tech_stacks:
#         # Convert spaces to hyphens and lowercase
#         tech_slug = tech.lower().replace(' ', '-')
#         badge = f"![{tech}](https://img.shields.io/badge/{tech_slug}-black?style=flat-square&logo={tech_slug})"
#         tech_badges.append(badge)
    
#     # Generate the README content
#     readme = f"""
# <h1 align="center">Hi 👋, I'm {username}</h1>
# <h3 align="center">A passionate developer crafting digital solutions</h3>

# <p align="center">
#     <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2196F3&center=true&width=435&lines=Always+learning+new+things;Building+the+future+with+code" alt="Typing SVG" />
# </p>

# ### 🚀 Quick Stats
# <p align="center">
#     <img src="https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=radical" alt="GitHub Stats" />
# </p>

# <p align="center">
#     <img src="https://github-readme-streak-stats.herokuapp.com/?user={username}&theme=radical" alt="GitHub Streak" />
# </p>

# ### 💻 Tech Stack
# <p align="center">
#     {' '.join(tech_badges)}
# </p>

# ### 🌱 Currently Working On
# - Building awesome projects that matter
# - Learning and growing every day
# - Contributing to open source

# ### 📫 How to reach me
# <p align="center">
#     <a href="https://github.com/{username}">
#         <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
#     </a>
#     <a href="https://linkedin.com/in/{username}">
#         <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
#     </a>
# </p>

# ### 📊 Weekly Development Breakdown
# ```text
# JavaScript   4 hrs 32 mins   ███████░░░░░░░░   35.5%
# Python       3 hrs 45 mins   ██████░░░░░░░░░   29.3%
# React        2 hrs 12 mins   ████░░░░░░░░░░░   17.2%
# Other        2 hrs 18 mins   ████░░░░░░░░░░░   18.0%
# ```

# <p align="center">
#     <img src="https://komarev.com/ghpvc/?username={username}&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
# </p>
# """
#     return readme

# def save_readme(content, filename="README.md"):
#     """Save the generated README to a file"""
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write(content)

# # Example usage
# if __name__ == "__main__":
#     username = input("Enter your GitHub username: ")
#     tech_stacks = input("Enter your tech stack (comma-separated): ").split(",")
#     tech_stacks = [tech.strip() for tech in tech_stacks]
    
#     readme_content = generate_github_profile(username, tech_stacks)
#     save_readme(readme_content)
#     print("README.md has been generated successfully!")