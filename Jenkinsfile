pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo '********** BUILD STEP STARTED!!! ************'
                sh 'python3.7 src/main.py'
                echo '*********************************************'
            }
        }
        stage('Deploy') {
            steps {
                sh 'aws s3 cp src s3://my-code --revursive'
            }
        }
    }
}