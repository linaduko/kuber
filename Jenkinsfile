pipeline {
    agent {
        node 'kuber-ssh'
    }
    tools {
        maven 'Maven'
    }
    stages {
        stage('Build'){
            steps {
                sh 'echo BUILDING...'
                sh 'echo BUILD ID - ${BUILD_ID}'
                sh 'echo BUILD 200OK'
                sh 'mvn install'
            }
        }
        stage('Test'){
            steps {
                sh 'echo TESTING...'
                junit 'target/surefire-reports/TEST-*.xml'
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
