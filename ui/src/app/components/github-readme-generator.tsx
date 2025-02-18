"use client"

import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import ReactMarkdown from "react-markdown"
import yaml from "js-yaml"

const defaultConfig = {
  profile_type: "developer",
  greeting: "Hi 👋, I'm John Doe",
  typing_text: ["Full+Stack+Developer", "Open+Source+Enthusiast"],
  tech_stacks: {},
  current_focus: {
    learning: ["Rust", "Web3", "Machine Learning"],
    working_on: ["Personal Blog", "Open Source Projects"],
    interests: ["System Design", "Cloud Architecture"],
  },
  social_links: { 
    LinkedIn: "https://linkedin.com/in/username",
    Twitter: "https://twitter.com/username",
    "Dev.to": "https://dev.to/username",
  },
  spotify_username: "",
  show_snake: true,
  show_activity_graph: false,
  show_trophies: false,
  theme: "radical",
  custom_sections: {},
}

export default function GitHubReadmeGenerator() {
  const [config, setConfig] = useState(defaultConfig)
  const [readmeContent, setReadmeContent] = useState("")
  const [isEditing, setIsEditing] = useState(false)

  useEffect(() => {
    generateReadme(config)
  }, [config])

  const generateReadme = (cfg:typeof defaultConfig) => {
    let content = `# ${cfg.greeting}\n\n`

    if (cfg.typing_text.length > 0) {
      content += `<h3 align="center">I'm a ${cfg.typing_text.join(", ")}</h3>\n\n`
    }

    if (Object.keys(cfg.current_focus).length > 0) {
      content += "## 🚀 About Me\n\n"
      for (const [key, values] of Object.entries(cfg.current_focus)) {
        if (Array.isArray(values)) 
        content += `- ${key.charAt(0).toUpperCase() + key.slice(1)}: ${values.join(", ")}\n`
      }
      content += "\n"
    }

    if (Object.keys(cfg.social_links).length > 0) {
      content += "## 🔗 Connect with me\n\n"
      for (const [platform, url] of Object.entries(cfg.social_links)) {
        content += `[![${platform}](https://img.shields.io/badge/${platform}-0077B5?style=for-the-badge&logo=${platform.toLowerCase()}&logoColor=white)](${url})\n`
      }
      content += "\n"
    }

    if (cfg.show_snake) {
      content += "## 🐍 My Contributions\n\n"
      content +=
        "![Snake animation](https://github.com/{username}/github-readme-snake-svg/blob/output/github-contribution-grid-snake.svg)\n\n"
    }

    if (cfg.show_activity_graph) {
      content += "## 📊 My GitHub Stats\n\n"
      content += `[![{username}'s github activity graph](https://activity-graph.herokuapp.com/graph?username={username}&theme=${cfg.theme})](https://github.com/{username})\n\n`
    }

    if (cfg.show_trophies) {
      content += "## 🏆 GitHub Trophies\n\n"
      content += `[![trophy](https://github-profile-trophy.vercel.app/?username={username}&theme=${cfg.theme})](https://github.com/ryo-ma/github-profile-trophy)\n\n`
    }

    setReadmeContent(content)
  }

  const handleConfigChange = (e:React.ChangeEvent<HTMLTextAreaElement>) => {
    try {
      const newConfig = yaml.load(e.target.value)
      if (typeof newConfig === "object" && newConfig !== null) 
      setConfig({ ...defaultConfig, ...newConfig })
    } catch (error) {
      console.error("Invalid YAML:", error)
    }
  }

  const handleReadmeEdit = (e:React.ChangeEvent<HTMLTextAreaElement>) => {
    setReadmeContent(e.target.value)
  }

  const handleDownload = () => {
    const element = document.createElement("a")
    const file = new Blob([readmeContent], { type: "text/plain" })
    element.href = URL.createObjectURL(file)
    element.download = "README.md"
    document.body.appendChild(element)
    element.click()
    document.body.removeChild(element)
  }

  const handleShare = () => {
    navigator.clipboard.writeText(readmeContent).then(() => {
      alert("README content copied to clipboard!")
    })
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">GitHub README Generator</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Card>
          <CardHeader>
            <CardTitle>Configuration</CardTitle>
          </CardHeader>
          <CardContent>
            <Textarea className="w-full h-64" value={yaml.dump(config)} onChange={handleConfigChange} />
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Preview</CardTitle>
          </CardHeader>
          <CardContent>
            {isEditing ? (
              <Textarea className="w-full h-64" value={readmeContent} onChange={handleReadmeEdit} />
            ) : (
              <div className="prose dark:prose-invert">
                <ReactMarkdown>{readmeContent}</ReactMarkdown>
              </div>
            )}
          </CardContent>
          <CardFooter className="flex justify-between">
            <Button onClick={() => setIsEditing(!isEditing)}>{isEditing ? "View Preview" : "Edit README"}</Button>
            <div>
              <Button onClick={handleShare} className="mr-2">
                Share
              </Button>
              <Button onClick={handleDownload}>Download</Button>
            </div>
          </CardFooter>
        </Card>
      </div>
    </div>
  )
}

