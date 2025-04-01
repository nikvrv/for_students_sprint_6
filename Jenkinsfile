pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'develop', url: 'https://github.com/nikvrv/for_students_sprint_6.git'
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }
    }
}
