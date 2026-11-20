pipeline {
    agent any

    stages {
        stage('Fetch') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/harathiyadhav123-hue/nxttrendz.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t nxttrendz-backend ./backend'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}