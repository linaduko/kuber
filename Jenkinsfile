pipeline {
    agent {
        node 'kuber-ssh'
    }
    stages {
        stage('Build'){
            steps {
                sh 'echo BUILDING...'
                sh 'echo BUILD ID - ${BUILD_ID}'
                git url: 'https://github.com/cyrille-leclerc/multi-module-maven-project'
                withMaven {
                sh "mvn clean verify"
                sh 'echo BUILD 200OK'
            }
        }
        stage('Test'){
            steps {
                sh 'echo TESTING...'
                sh 'apt install -y npm'
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
