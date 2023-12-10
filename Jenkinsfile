pipeline{
   agent any
   stages{
      stage('Checkout'){
         steps{
            checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/oussama938/Music_Classifier']])
         }
      }
      stage('Building Containers'){
         steps{
            sh'docker-compose build'
         }
      }
      stage('Testing and Running Containers'){
         steps{
            sh 'docker-compose up -d'

            def serviceName = 'test_service'
            def exitCode = sh(script: "docker-compose ps -q ${serviceName} | xargs docker inspect --format='{{.State.ExitCode}}'", returnStatus: true).trim() 
            echo "Exit code of ${serviceName}: ${exitCode}"

            if(exitCode == 0){
               echo 'Containers are Working !'
               sh 'docker-compose down'
               sh 'docker-compose up'

            }
            else{
               echo 'Containers DOWN !'
               sh 'docker-compose down'

            }
            
         }
      }
   }
}
