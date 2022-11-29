pipeline {
    agent {
        node 'kuber-ssh'
    }
    stages {
        stage('Build'){
            steps {
                sh 'echo BUILDING...'
                sh 'ls -la' 
                sh 'echo BUILD 200OK'
            }
        }
        stage('Test'){
            steps {
                sh 'echo TESTING...'
                sh 'echo TEST 200OK'
            }
        }
        stage('Deploy'){
            steps {
                sh 'echo DEPLOYING...'
                sh 'envsubst < ${WORKSPACE}/wordpress-deployment.yaml'
                sh 'kubectl apply -k ./'
                sh 'echo DEPLOY 200OK'
            }
        }
    }
}
