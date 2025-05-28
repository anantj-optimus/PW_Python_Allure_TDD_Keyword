pipeline {
    agent any

    tools {
        // No Python tool here because we avoid the deprecated Python plugin
    }

    environment {
        // Optional: Define your Python virtual environment directory
        VENV_DIR = "venv"
    }

    stages {
        stage('Setup') {
            steps {
                bat """
                echo ==== Python Version ====
                python --version
                echo ==== Creating Virtual Environment ====
                python -m venv %VENV_DIR%
                call %VENV_DIR%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call %VENV_DIR%\\Scripts\\activate
                pytest --alluredir=allure-results
                """
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat """
                allure generate allure-results --clean -o allure-report
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'allure-report',
                    reportFiles: 'index.html',
                    reportName: 'Allure Test Report',
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }
    }
}
