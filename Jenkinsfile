pipeline {
    agent {
        docker {
            image 'boisvert/python-build'
            args '-v /var/run/docker.sock:/var/run/docker.sock -u root'
        }
    }
    environment {
        TOKEN = credentials('ultrabot-token')
    }
    stages {
        stage('build') {
            steps {
                // debug if necessary
                // sh 'printenv'

                echo "Building"

                sh 'docker build -t combinesoldier14/ultrabot .'

            }
        }
        stage('deploy') {
            steps {
                // conditionally deploy
                sh "docker container stop ultrabot || true"
                sh "docker container rm ultrabot || true"
                sh "docker run -d --name ultrabot -e TOKEN=$TOKEN --restart=unless-stopped combinesoldier14/ultrabot"
            }
        }
    }
}
