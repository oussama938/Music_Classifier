pipeline{
   agent any
   stages{
      stage('Checkout'){
         steps{
            checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/oussama938/Music_Classifier']])
         }
      }
      stage('Unit Tests') {
         steps {
            // sh 'cd svm_service && pytest tests/test_svm_service.py'
            // sh 'cd vgg19_service && pytest tests/test_vgg19_service.py'
            // sh 'cd front_service && pytest tests/test/front_service.py'
            // sh 'ls'
            // sh 'docker-compose build'
            sh 'docker-compose test_runner'
         }
      }

      stage('Building & Running Containers'){
         steps{
            sh '''
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
