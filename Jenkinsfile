pipeline {
    agent any
    stages {
        stage('1. Checkout') {
            steps {
                // Jenkins 會自動把這裡的程式碼抓下來
                echo 'Checking out source code...'
            }
        }
        stage('2. Build test-app') {
            steps {
                sh 'docker build -t test-app .'
            }
        }
        stage('3. Run App') {
            steps {
                sh "docker run --rm -v ${env.WORKSPACE}:/app test-app pytest -v --junitxml=test-results.xml"
            }
        }
    }
    post {
        always {
            echo 'Collecting test report...'
            junit 'test-results.xml'
            
            echo 'Cleaning up workspace...'
            sh 'docker rmi test-app || true'
        }
    }
}
