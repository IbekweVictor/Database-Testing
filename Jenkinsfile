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
                bat "${env.PYTHON} -m pip install pytest-html"
            }
        }

        stage('Test') {
            parallel {
                stage('Test Schema') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testschema --junitxml=schema_results.xml --html=schema_report.html"
                    }
                    post {
                        always {
                            junit 'schema_results.xml'
                            archiveArtifacts artifacts: 'schema_report.html', fingerprint: true
                        }
                    }
                }

                stage('Test Constraint') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testconst --junitxml=constraint_results.xml --html=constraint_report.html"
                    }
                    post {
                        always {
                            junit 'constraint_results.xml'
                            archiveArtifacts artifacts: 'constraint_report.html', fingerprint: true
                        }
                    }
                }

                stage('Test Crud') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testcrud --junitxml=crud_results.xml --html=crud_report.html"
                    }
                    post {
                        always {
                            junit 'crud_results.xml'
                            archiveArtifacts artifacts: 'crud_report.html', fingerprint: true
                        }
                    }
                }

                stage('Test Integrity') {
                    steps {
                        bat "${env.PYTHON} -m pytest -v -s -m testintegrity --junitxml=integrity_results.xml --html=integrity_report.html"
                    }
                    post {
                        always {
                            junit 'integrity_results.xml'
                            archiveArtifacts artifacts: 'integrity_report.html', fingerprint: true
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Build and tests successful!'
        }
        failure {
            echo 'Pipeline failed - check logs and reports.'
        }
    }
}
