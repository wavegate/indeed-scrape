import pandas
from bs4 import BeautifulSoup
import re

stack = {
    "full-stack": [r'full[-\s]?stack', 0],
    "front-end": [r'front[-\s]?end', 0],
    "back-end": [r'back[-\s]?end', 0],
    "UI/UX": [r'ui/ux', 0],
    "DevOps": [r'devops', 0]
}

experience = {
    "junior": [r'(junior)|(entry)', 0],
    "mid-level": [r'mid', 0],
    "senior": [r'senior', 0]
}

education = {
    "Bachelor's": [r'(bachelor[\']?s)|(\bba\b)|(\bbs\b)', 0],
    "Master's": [r'(master[\']?s)|(\bms\b)', 0],
    "PhD": [r'(phd)|(doctor)', 0]
}

language = {
    "HTML": [r'html', 0],
    "CSS": [r'css', 0],
    "JavaScript": [r'(javascript)|(js)', 0],
    "TypeScript": [r'typescript', 0],
    "PHP": [r'php', 0],
    "Java": [r'\bjava\b', 0],
    "Python": [r'python', 0],
    "Kotlin": [r'kotlin', 0],
    "Swift": [r'swift', 0],
    "Dart": [r'dart', 0],
    "C#": [r'c#', 0],
    "C": [r'\bc\b', 0],
    "C++": [r'c\+\+', 0],
    "R": [r'\br\b', 0],
    "Lua": [r'lua', 0],
    "Go": [r'[.\s]go[.\s]', 0],
    "Rust": [r'rust', 0],
    "Ruby": [r'ruby', 0],
    "Perl": [r'perl', 0],
    "Clojure": [r'clojure', 0],
    "Scala": [r'\bscala\b', 0],
}

frontend_framework = {
    "React": [r'react', 0],
    "Angular": [r'angular', 0],
    "Vue": [r'vue', 0],
    "Ember": [r'\bember', 0],
    "Svelte": [r'svelte', 0],
    "jQuery": [r'jquery', 0],
    "WebAssembly": [r'(web\s?assembly)|(wasm)', 0],
    "Next": [r'next.js', 0],
    "Gatsby": [r'gatsby', 0]
}

backend_framework = {
    "Django": [r'django', 0],
    "Flask": [r'flask', 0],
    "Ruby on Rails": [r'rails', 0],
    "ASP.net": [r'(asp.net)|(\b.net\b)', 0],
    "Spring": [r'spring', 0],
    "Express": [r'express', 0],
    "Laravel": [r'laravel', 0]
}

database = {
    "Oracle": [r'oracle', 0],
    "MySQL": [r'mysql', 0],
    "PostgreSQL": [r'postgresql', 0],
    "MS SQL": [r'(ms\s?sql)|(microsoft sql)', 0],
    "SQLite": [r'sqlite', 0],
    "MongoDB": [r'mongodb', 0],
    "Redis": [r'redis', 0],
    "MariaDB": [r'maria', 0],
    "Firebase": [r'firebase', 0],
    "Cassandra": [r'cassandra', 0],
    "DB2": [r'db2', 0],
    "Elasticsearch": [r'elasticsearch', 0],
    "GraphQL": [r'graphql', 0]
}

css = {
    "Bootstrap": [r'bootstrap', 0],
    "Tailwind": [r'tailwind', 0],
    "Material": [r'material', 0],
    "SASS": [r'(scss)|(sass)', 0],
    "LESS": [r'\bless\b', 0],
}

cms = {
    "Wordpress": [r'wordpress', 0],
    "Drupal": [r'drupal', 0],
    "Joomla": [r'joomla', 0],
    "Magento": [r'magento', 0],
}

module_bundler = {
    "Webpack": [r'webpack', 0],
    "Parcel": [r'parcel', 0],
    "Rollup": [r'rollup', 0],
    "Browserify": [r'browserify', 0],
}

cloud = {
    "AWS": [r'aws', 0],
    "Google cloud": [r'google cloud', 0],
    "Azure": [r'azure', 0],
    "Heroku": [r'heroku', 0],
}

container = {
    "Docker": [r'docker', 0],
    "Kubernetes": [r'kubernetes', 0]
}

testing = {
    "Jest": [r'jest', 0],
    "Mocha": [r'mocha', 0],
    "Cypress": [r'cypress', 0],
    "Enzyme": [r'enzyme', 0]
}

bigArray = {"stack":stack, "experience":experience, "language":language, "frontend":frontend_framework, "backend":backend_framework, "education":education, "database":database, "css_framework":css, "CMS":cms, "bundler": module_bundler, "cloud":cloud, "container":container, "testing_framework":testing}

data = pandas.read_csv('alldata.csv')
for info in data['description']:
    soup = BeautifulSoup(info, 'html.parser')
    results = {}
    for name, topic in bigArray.items():
        for key, value in topic.items():
            found = soup.find(text=re.compile(value[0], re.IGNORECASE))
            if found:
                value[1] = value[1] + 1

print(bigArray)