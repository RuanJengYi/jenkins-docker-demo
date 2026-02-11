pipeline {
    agent any
    stages {
        stage('1. Checkout SCM') {
            steps {
                // Jenkins 會自動把這裡的程式碼抓下來
                echo 'Checking out source code...'
            }
        }
        stage('2. Build Docker Image') {
            steps {
                sh '''
                    echo "FROM python:3.9-slim" > Dockerfile
                    echo "CMD python -c, \\"print('Hello from GitHub Jenkinsfile!')\\"" >> Dockerfile
                    docker build -t my-github-test .
                '''
            }
        }
        stage('3. Run Test') {
            steps {
                // 跑起來！
                sh 'docker run --rm my-github-test'
            }
        }
    }
}
