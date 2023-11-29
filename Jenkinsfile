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
            docker-compose up -d
            '''
         }
      }
      stage('Run Tests') {
         steps {
            script {
                    // Identify services dynamically
               def servicesCommand = "docker-compose config --services"
               def services = sh(script: servicesCommand, returnStdout: true).trim().split("\n")

                    // Run pytest for each service
               for (service in services) {
                  echo "Running tests for $service"
                  def testCommand = "docker-compose run --rm $service pytest"

                        // Run tests and check the exit code
                  def result = sh script: testCommand, returnStatus: true
                  if (result != 0) {
                     echo "Tests failed for $service, stopping Docker Compose"
                     sh 'docker-compose down'
                     error 'Tests failed, stopping build'
                  }
               }
            }
         }
      }
   }
}
