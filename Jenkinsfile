pipeline{
   agent any
   stages{
      stage('Checkout'){
         steps{
            checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/oussama938/Music_Classifier']])
         }
      }
      stage('install req'){
         steps{
            // sh 'sudo apt install -y python3.9 python3-pip'
         }
      }
      stage('Unit Tests') {
         steps {
                            // Build Docker images for your services
            sh 'docker-compose -f docker-compose.yml build'

            // Run unit tests for each service
            sh 'docker-compose -f docker-compose.yml run --rm svm_service pytest tests/'
            sh 'docker-compose -f docker-compose.yml run --rm vgg19_service pytest tests/'
            sh 'docker-compose -f docker-compose.yml run --rm front_service pytest tests/'
            // sh 'ls'
            // sh 'pwd'
            // sh 'ls svm_service'
            // sh 'docker-compose up'
            sh 'python -m pip install pytest'
            sh 'cd svm_service && pytest tests/'
            sh 'cd vgg19_service && pytest tests/'
            sh 'cd front_service && pytest tests/'
            // sh 'ls'
            // sh 'docker-compose build'
            // sh 'docker-compose run test_runner'
         }
      }

      stage('Building & Running Containers'){
         steps{
            sh '''
            sh -c "pytest svm_service/tests/ vgg19_service/tests/ front_service/tests/
            docker-compose up
            '''
         }
      }
      stage('Run Unit Tests') {
            steps {
                script {
                    // Run unit tests for each service
                    sh 'docker-compose exec svm_service pytest svm_service/tests'
                    sh 'docker-compose exec vgg19_service pytest vgg19_service/tests'
                    sh 'docker-compose exec front_service pytest front_service/tests'
                }
            }
        }
   }
   post {
      always {
         script {
      // Clean up Docker Compose services
         sh 'docker-compose down'
         }
      }
   }  
}
