pipeline{
   agent any
   stages{
      stage('Checkout'){
         steps{
            checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/oussama938/Music_Classifier']])
         }
      }
      stage('Building & Running Containers'){
         steps{
            sh '''
            docker-compose up
            '''
         }
      }
   }
}
