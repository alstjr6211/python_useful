import os

#프로젝트 파일 구조
project_structure = {
    "frontend": {
        "index.html": "",
        "signup.html": "",
        "dashboard.html": "",
        "settings.html": "",
        "mail_input.html": "",
        "assets": {
            "styles.css": "",
            "dashboard.css": "",
        },
        "js": {
            "app.js": "",
            "firebase.js": "",
        },
    },
    "backend": {
        "scraping": {
            "scraper.py": "",
            "gmail_scraper.py": "",
            "naver_scraper.py": "",
        },
        "firebase_functions": {
            "index.js": "",
        },
        "utils": {
            "db.py": "",
            "config.py": "",
        },
    },
    "README.md": "# 프로젝트 설명\n",
    "requirements.txt": "# Python 패키지 목록\n",
}

def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # 디렉토리 생성
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            # 파일 생성
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)


project_root = "project name"

create_project_structure(project_root, project_structure)

print(f"'{project_root}' 디렉토리와 파일 구조가 성공적으로 생성되었습니다.")
