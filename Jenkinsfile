pipeline{
    agent any
    stages {
    
        stage('Setup Python Virtual ENV'){
       
      steps  {
            sh '''
            chmod +x envsetup.sh
            ./envsetup.sh
            '''}
        }
    }
}
