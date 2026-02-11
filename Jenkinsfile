pipeline {
    agent any
    stages {
        stage('1. Checkout') {
            steps {
                // Jenkins 會自動把這裡的程式碼抓下來
                echo 'Checking out source code...'
            }
        }
        stage('2. Build Image') {
            steps {
                sh 'docker build -t test-app .'
            }
        }
        stage('3. Run App') {
            steps {
                sh 'docker run --rm test-app'
            }
        }
    }
    post {
        always {
            echo 'Cleaning up workspace...'
            sh 'docker rmi test-app || true'
        }
    }
}
