pipeline {
    agent any

    environment {
        PYTHON = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']], 
                    extensions: [], 
                    userRemoteConfigs: [[url: 'https://github.com/IbekweVictor/Database-Testing.git']]
                )
            }
        }

        stage('Build (Install dependencies)') {
            steps {
                bat "${env.PYTHON} -m pip install --upgrade pip"
                bat "${env.PYTHON} -m pip install -r requirements.txt"
                bat "${env.PYTHON} -m pip install pytest-html pytest-merger"
            }
        }

        stage('Test') {
            parallel {
                stage('Test Schema') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testschema --junitxml=schema_results.xml --html=schema_report.html"
                    }
                }

                stage('Test Constraint') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testconst --junitxml=constraint_results.xml --html=constraint_report.html"
                    }
                }

                stage('Test Crud') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testcrud --junitxml=crud_results.xml --html=crud_report.html"
                    }
                }

                stage('Test Integrity') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testintegrity --junitxml=integrity_results.xml --html=integrity_report.html"
                    }
                }
            }
        }

        stage('Report') {
            steps {
                // Aggregate JUnit XML results
                junit '**/*results.xml'

                // Merge HTML reports into one
                bat "${env.PYTHON} -m pytest_merger --input schema_report.html constraint_report.html crud_report.html integrity_report.html --output merged_report.html"

                // Archive final merged report
                archiveArtifacts artifacts: 'merged_report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build and test successful!'
        }
        failure {
            echo 'Pipeline failed - check logs and reports.'
        }
    }
}
